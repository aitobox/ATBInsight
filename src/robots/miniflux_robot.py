import requests


def fetch_miniflux_entries(url: str, username: str, password: str, days: int = 7) -> list[dict]:
    """Fetch unread entries from a Miniflux RSS server.

    Args:
        url: Base URL of Miniflux server.
        username: Miniflux username.
        password: Miniflux password.
        days: Number of past days to consider (default: 7).

    Returns:
        List of entry dictionaries returned by Miniflux API.
    """
    api_url = f"{url.rstrip('/')}/v1/entries?status=unread"
    resp = requests.get(api_url, auth=(username, password), timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data.get("entries", [])

