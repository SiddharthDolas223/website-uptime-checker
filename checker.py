#!/usr/bin/env python3
import sys
import time
from datetime import datetime

import requests


def check_website(url: str, timeout: float = 5.0) -> int:
    """
    Return 0 if site is considered UP, 1 if returned non-success status,
    2 if unreachable / network error.
    """
    try:
        start = time.time()
        resp = requests.get(url, timeout=timeout)
        elapsed = time.time() - start
        status = resp.status_code
        # Consider 2xx and 3xx as UP
        if 200 <= status < 400:
            print(f"✅ {url} is UP — status={status} time={elapsed:.3f}s")
            return 0
        else:
            print(f"⚠️ {url} returned status code {status} (time={elapsed:.3f}s)")
            return 1
    except requests.exceptions.RequestException as exc:
        print(f"❌ {url} is DOWN or unreachable — {exc}")
        return 2


def normalize_url(u: str) -> str:
    u = u.strip()
    # If user omitted scheme, assume https
    if not u.startswith(("http://", "https://")):
        u = "https://" + u
    return u


if __name__ == "__main__":
    try:
        website = input("Enter website URL (example: https://google.com): ").strip()
        if not website:
            print("No URL provided. Exiting.")
            sys.exit(1)
        website = normalize_url(website)
        code = check_website(website)
        sys.exit(code)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(130)
