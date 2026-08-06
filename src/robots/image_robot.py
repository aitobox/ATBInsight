import os
import re
import hashlib
import requests
import sqlite3
from src.db import is_image_downloaded, save_image_record

def localize_images(markdown_content: str, output_dir: str, conn: sqlite3.Connection) -> str:
    """
    Downloads remote images found in markdown content (or HTML tags) to a local 'images' directory
    under output_dir, updates the DB cache, and replaces image URLs with local relative paths.
    """
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    img_urls = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', markdown_content)
    img_urls += re.findall(r'<img[^>]+src=["\'](https?://[^"\']+)["\']', markdown_content)

    for url in set(img_urls):
        cached_path = is_image_downloaded(conn, url)
        if cached_path:
            markdown_content = markdown_content.replace(url, cached_path)
            continue

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            resp = requests.get(url, headers=headers, timeout=10)
            if resp.status_code == 200:
                sha256 = hashlib.sha256(resp.content).hexdigest()[:12]
                content_type = resp.headers.get("Content-Type", "")
                if "webp" in content_type or url.endswith(".webp"):
                    ext = "webp"
                elif "png" in content_type or url.endswith(".png"):
                    ext = "png"
                elif "gif" in content_type or url.endswith(".gif"):
                    ext = "gif"
                else:
                    ext = "jpg"
                    
                filename = f"{sha256}.{ext}"
                local_file_path = os.path.join(images_dir, filename)

                with open(local_file_path, "wb") as f:
                    f.write(resp.content)

                rel_path = f"./images/{filename}"
                save_image_record(conn, url, rel_path, sha256)
                markdown_content = markdown_content.replace(url, rel_path)
        except Exception:
            pass

    return markdown_content
