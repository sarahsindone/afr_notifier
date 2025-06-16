# main.py
from app import main

# HTTP trigger entry point
def afr_notifier(request):
    """
    Google Cloud Function entry. Ignores the HTTP request
    and just runs your main() notifier logic.
    """
    main()
    return ("OK", 200)
