from __future__ import annotations

import os


def notify(message: str) -> None:
    email = os.getenv("ALERT_EMAIL")
    if email:
        print(f"Alert for {email}: {message}")
    else:
        print(message)
