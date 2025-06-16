from fetcher import get_entries
from filter import is_equity_article
from state_store import has_seen, mark_seen
from notifier import send_email
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    entries = get_entries()
    print(f"Fetched {len(entries)} entries; checking for new equity articles…")
    for e in entries:
        if is_equity_article(e) and not has_seen(e['guid']):
            try:
                send_email(e)
                mark_seen(e['guid'])
                print(f"Email sent & marked seen: {e['title']}")
            except Exception as exc:
                print(f"ERROR sending email for {e['title']}: {exc}")

if __name__ == "__main__":
    # run immediately, then every 60 seconds
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', seconds=60, next_run_time=datetime.now())
    print("Starting scheduler—checking every 60 seconds.")
    scheduler.start()
    