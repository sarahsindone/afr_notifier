import re
from config import settings

def is_equity_article(entry: dict) -> bool:
    """
    True if any of the configured keywords appears in
    the title or summary (case-insensitive, whole-word).
    """
    text = (entry["title"] + " " + entry["summary"]).lower()
    for kw in settings.keywords_list:
        if re.search(rf"\b{re.escape(kw)}\b", text):
            return True
    return False