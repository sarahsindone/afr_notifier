# filter.py
import re
from config import settings

def is_equity_article(entry: dict) -> bool:
    """
    Return True if any keyword appears in title or summary.
    Case-insensitive, whole-word match.
    """
    text = (entry["title"] + " " + entry["summary"]).lower()
    for kw in settings.keywords:
        # use word boundaries to avoid partial matches
        if re.search(rf"\b{re.escape(kw.lower())}\b", text):
            return True
    return False
