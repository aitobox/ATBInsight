import os
import re
import hashlib
import base64
import requests
import sqlite3
import logging
from src.db import is_image_downloaded, save_image_record

logger = logging.getLogger("ai_insight")

POSTS_IMAGES_DIR = "docs/blog/posts/images"


def unwrap_proxy_url(url: str) -> str:
    """
    If url is a Miniflux proxy URL (e.g. http://localhost/proxy/token/aHR0cHM6...),
    extract and base64-decode the original image URL.
    """
    if "/proxy/" in url:
        parts = url.rstrip("/").split("/")
        last_part = parts[-1]
        try:
            # Fix base64 padding
            padded = last_part + "=" * (-len(last_part) % 4)
            decoded = base64.urlsafe_b64decode(padded).decode("utf-8")
            if decoded.startswith("http://") or decoded.startswith("https://"):
                return decoded
        except Exception:
            pass
    return url


def localize_images(markdown_content: str, output_dir: str, conn: sqlite3.Connection) -> str:
    """
    Downloads remote images found in markdown content (or HTML tags) to a local 'images' directory
    under output_dir AND docs/blog/posts/images, updates DB cache, and replaces image URLs with local relative paths.
    Unwraps Miniflux proxy URLs (http://localhost/proxy/...) to download real images.
    """
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(POSTS_IMAGES_DIR, exist_ok=True)

    # 1. Extract markdown image URLs: ![alt](url) or ![alt](url "title")
    raw_md_urls = re.findall(r'!\[.*?\]\((https?://[^\s\)]+)(?:\s+["\'].*?["\'])?\)', markdown_content)
    # 2. Extract HTML img src URLs: <img ... src="url" ...>
    raw_html_urls = re.findall(r'<img[^>]+src=["\'](https?://[^"\']+)["\']', markdown_content)

    img_urls = set(raw_md_urls + raw_html_urls)

    for orig_url in img_urls:
        download_target_url = unwrap_proxy_url(orig_url)

        cached_path = is_image_downloaded(conn, orig_url) or is_image_downloaded(conn, download_target_url)
        if cached_path:
            markdown_content = markdown_content.replace(orig_url, cached_path)
            if download_target_url != orig_url:
                markdown_content = markdown_content.replace(download_target_url, cached_path)
            continue

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            resp = requests.get(download_target_url, headers=headers, timeout=15)
            if resp.status_code == 200:
                sha256 = hashlib.sha256(resp.content).hexdigest()[:12]
                content_type = resp.headers.get("Content-Type", "").lower()
                
                if "webp" in content_type or download_target_url.endswith(".webp"):
                    ext = "webp"
                elif "png" in content_type or download_target_url.endswith(".png"):
                    ext = "png"
                elif "gif" in content_type or download_target_url.endswith(".gif"):
                    ext = "gif"
                elif "svg" in content_type or download_target_url.endswith(".svg"):
                    ext = "svg"
                else:
                    ext = "jpg"
                    
                filename = f"{sha256}.{ext}"
                local_file_path = os.path.join(images_dir, filename)
                posts_file_path = os.path.join(POSTS_IMAGES_DIR, filename)

                # Write to origin backup images dir
                with open(local_file_path, "wb") as f:
                    f.write(resp.content)

                # Write to docs/blog/posts/images dir
                with open(posts_file_path, "wb") as f:
                    f.write(resp.content)

                rel_path = f"./images/{filename}"
                save_image_record(conn, orig_url, rel_path, sha256)
                if download_target_url != orig_url:
                    save_image_record(conn, download_target_url, rel_path, sha256)

                markdown_content = markdown_content.replace(orig_url, rel_path)
                if download_target_url != orig_url:
                    markdown_content = markdown_content.replace(download_target_url, rel_path)
                
                logger.info(f"Successfully localized image: {download_target_url} -> {rel_path}")
            else:
                logger.warning(f"Failed to download image {download_target_url}, status code: {resp.status_code}")
        except Exception as e:
            logger.error(f"Error downloading image {download_target_url}: {e}")

    return markdown_content
