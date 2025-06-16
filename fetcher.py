# fetcher.py
import requests
import feedparser
from config import settings

def get_entries() -> list[dict]:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    resp = requests.get(settings.afr_rss_url, headers=headers, timeout=10)
    resp.raise_for_status()
    feed = feedparser.parse(resp.content)
    entries = []
    for e in feed.entries:
        entries.append({
            "guid": getattr(e, "id", e.link),
            "title": e.title,
            "link": e.link,
            "summary": e.get("summary", "")
        })
    return entries