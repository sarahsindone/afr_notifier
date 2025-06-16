# state_store.py
import json
import os

SEEN_FILE = "seen.json"

def _load_seen() -> set[str]:
    if not os.path.exists(SEEN_FILE):
        return set()
    with open(SEEN_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))

def _save_seen(seen: set[str]) -> None:
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen), f, indent=2)

_seen = _load_seen()

def has_seen(guid: str) -> bool:
    return guid in _seen

def mark_seen(guid: str) -> None:
    _seen.add(guid)
    _save_seen(_seen)