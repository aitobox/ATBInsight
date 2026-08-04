import logging
import requests

logger = logging.getLogger("ai_insight")


def fetch_miniflux_entries(
    url: str,
    username: str,
    password: str,
    days: int = 7,
    target_date: str | None = None,
) -> list[dict]:
    api_url = f"{url.rstrip('/')}/v1/entries?status=unread"
    logger.info(f"Fetching RSS entries from Miniflux: {api_url}")
    resp = requests.get(api_url, auth=(username, password), timeout=10)
    resp.raise_for_status()
    data = resp.json()
    entries = data.get("entries", [])
    logger.info(f"Fetched {len(entries)} unread entries in total from Miniflux.")

    if target_date:
        filtered = [e for e in entries if (e.get("published_at") or "").startswith(target_date)]
        logger.info(f"Filtered {len(filtered)} entries matching date '{target_date}'.")
        return filtered

    if days > 0:
        import datetime
        cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
        filtered = []
        for entry in entries:
            pub_at = entry.get("published_at") or ""
            # Fallback to created_at if published_at is empty or default zero-date string
            if not pub_at or pub_at.startswith("0001-01-01") or pub_at.startswith("1970-01-01"):
                pub_at = entry.get("created_at") or ""

            if pub_at and not (pub_at.startswith("0001-01-01") or pub_at.startswith("1970-01-01")):
                try:
                    dt = datetime.datetime.fromisoformat(pub_at.replace("Z", "+00:00"))
                    if dt >= cutoff:
                        filtered.append(entry)
                except ValueError:
                    filtered.append(entry)
            else:
                filtered.append(entry)
        logger.info(f"Filtered {len(filtered)} entries published/created within past {days} days (since {cutoff.strftime('%Y-%m-%d %H:%M:%S UTC')}).")
        return filtered

    return entries


