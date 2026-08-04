import os
from unittest.mock import patch, MagicMock
from src.db import init_db, save_image_record
from src.robots.image_robot import localize_images

@patch("requests.get")
def test_localize_images_markdown(mock_get, tmp_path):
    conn = init_db(str(tmp_path / "test.db"))
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.content = b"fake-image-bytes"
    mock_resp.headers = {"Content-Type": "image/png"}
    mock_get.return_value = mock_resp

    md = "Here is an image: ![test](http://example.com/test.png)"
    out_dir = str(tmp_path / "docs" / "insight" / "2026-08-04")

    new_md = localize_images(md, out_dir, conn)
    assert "./images/" in new_md
    assert "http://example.com/test.png" not in new_md
    assert os.path.exists(os.path.join(out_dir, "images"))

@patch("requests.get")
def test_localize_images_html_and_cached(mock_get, tmp_path):
    conn = init_db(str(tmp_path / "test.db"))
    # Save a cached image record
    save_image_record(conn, "http://example.com/cached.jpg", "./images/cached123.jpg", "abc123sha")

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.content = b"fake-new-image"
    mock_resp.headers = {"Content-Type": "image/jpeg"}
    mock_get.return_value = mock_resp

    md = (
        'Here is cached: <img src="http://example.com/cached.jpg">\n'
        'Here is new: <img src="http://example.com/new.jpg">'
    )
    out_dir = str(tmp_path / "docs" / "insight" / "2026-08-04")

    new_md = localize_images(md, out_dir, conn)
    assert "./images/cached123.jpg" in new_md
    assert "./images/" in new_md
    assert "http://example.com/cached.jpg" not in new_md
    assert "http://example.com/new.jpg" not in new_md

@patch("requests.get")
def test_localize_images_download_failure(mock_get, tmp_path):
    conn = init_db(str(tmp_path / "test.db"))
    mock_resp = MagicMock()
    mock_resp.status_code = 404
    mock_get.return_value = mock_resp

    md = "Failed image: ![fail](http://example.com/404.png)"
    out_dir = str(tmp_path / "docs" / "insight" / "2026-08-04")

    new_md = localize_images(md, out_dir, conn)
    assert new_md == md
