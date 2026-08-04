import logging
import requests

logger = logging.getLogger("ai_insight")


def fetch_miniflux_entries(
    url: str,
    username: str,
    password: str,
    days: int = 7,
    target_date: str | None = None,
    limit: int = 500,
) -> list[dict]:
    api_url = f"{url.rstrip('/')}/v1/entries?order=created_at&direction=desc&limit={limit}"
    logger.info(f"Fetching RSS entries from Miniflux: {api_url}")
    resp = requests.get(api_url, auth=(username, password), timeout=15)
    resp.raise_for_status()
    data = resp.json()
    entries = data.get("entries", [])
    logger.info(f"Fetched {len(entries)} entries in total from Miniflux.")

    if target_date:
        filtered = []
        for entry in entries:
            pub_at = entry.get("published_at") or ""
            created_at = entry.get("created_at") or ""
            if pub_at.startswith(target_date) or created_at.startswith(target_date):
                filtered.append(entry)
        logger.info(f"Filtered {len(filtered)} entries matching date '{target_date}'.")
        return filtered

    if days > 0:
        import datetime
        cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
        filtered = []
        for entry in entries:
            # Use created_at as primary timestamp for RSS ingestion date filtering
            date_str = entry.get("created_at") or entry.get("published_at") or ""
            if date_str and not (date_str.startswith("0001-01-01") or date_str.startswith("1970-01-01")):
                try:
                    dt = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                    if dt >= cutoff:
                        filtered.append(entry)
                except ValueError:
                    filtered.append(entry)
            else:
                filtered.append(entry)
        logger.info(f"Filtered {len(filtered)} entries created/published within past {days} days (since {cutoff.strftime('%Y-%m-%d %H:%M:%S UTC')}).")
        return filtered

    return entries


