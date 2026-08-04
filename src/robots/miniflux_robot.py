import requests


def fetch_miniflux_entries(
    url: str,
    username: str,
    password: str,
    days: int = 7,
    target_date: str | None = None,
) -> list[dict]:
    """Fetch unread entries from a Miniflux RSS server, optionally filtered by published date.

    Args:
        url: Base URL of Miniflux server.
        username: Miniflux username.
        password: Miniflux password.
        days: Number of past days to consider (default: 7).
        target_date: Specific target date (YYYY-MM-DD) to filter entries by.

    Returns:
        List of entry dictionaries returned by Miniflux API.
    """
    api_url = f"{url.rstrip('/')}/v1/entries?status=unread"
    resp = requests.get(api_url, auth=(username, password), timeout=10)
    resp.raise_for_status()
    data = resp.json()
    entries = data.get("entries", [])

    if target_date:
        filtered = []
        for entry in entries:
            pub_at = entry.get("published_at") or ""
            if pub_at.startswith(target_date):
                filtered.append(entry)
        return filtered

    if days > 0:
        import datetime
        cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
        filtered = []
        for entry in entries:
            pub_at = entry.get("published_at") or ""
            if pub_at:
                try:
                    dt = datetime.datetime.fromisoformat(pub_at.replace("Z", "+00:00"))
                    if dt >= cutoff:
                        filtered.append(entry)
                except ValueError:
                    filtered.append(entry)
            else:
                filtered.append(entry)
        return filtered

    return entries


