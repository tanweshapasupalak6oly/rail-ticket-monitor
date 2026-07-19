from __future__ import annotations

import os


def notify(message: str) -> None:
    alert_target = os.getenv("ALERT_EMAIL")
    if alert_target:
        print(f"Alert for {alert_target}: {message}")
        return

    print(f"Alert: {message}")
