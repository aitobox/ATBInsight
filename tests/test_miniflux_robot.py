from unittest.mock import patch, MagicMock
import pytest
import requests
from src.robots.miniflux_robot import fetch_miniflux_entries


@patch("requests.get")
def test_fetch_miniflux_entries_success(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "entries": [
            {
                "id": 1,
                "title": "AI Insight Test",
                "content": "<p>Content</p>",
                "url": "http://example.com",
            }
        ]
    }
    mock_get.return_value = mock_resp

    entries = fetch_miniflux_entries("http://mock-miniflux", "user", "pass", days=7)
    assert len(entries) == 1
    assert entries[0]["title"] == "AI Insight Test"
    mock_get.assert_called_once_with(
        "http://mock-miniflux/v1/entries?status=read,unread",
        auth=("user", "pass"),
        timeout=10,
    )


@patch("requests.get")
def test_fetch_miniflux_entries_trailing_slash_url(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"entries": []}
    mock_get.return_value = mock_resp

    entries = fetch_miniflux_entries("http://mock-miniflux/", "user", "pass", days=7)
    assert entries == []
    mock_get.assert_called_once_with(
        "http://mock-miniflux/v1/entries?status=read,unread",
        auth=("user", "pass"),
        timeout=10,
    )


@patch("requests.get")
def test_fetch_miniflux_entries_http_error(mock_get):
    mock_resp = MagicMock()
    mock_resp.raise_for_status.side_effect = requests.exceptions.HTTPError("401 Unauthorized")
    mock_get.return_value = mock_resp

    with pytest.raises(requests.exceptions.HTTPError):
        fetch_miniflux_entries("http://mock-miniflux", "invalid_user", "invalid_pass")
