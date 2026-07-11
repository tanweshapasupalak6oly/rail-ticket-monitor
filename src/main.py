from __future__ import annotations

import json
from pathlib import Path

from checker import choose_best_offer, check_tickets
from notifier import notify

ROUTE = {
    "origin": "KYN",
    "destination": "PURI",
}

DATA_FILE = Path("data/previous.json")


def load_previous() -> dict:
    if not DATA_FILE.exists():
        return {}
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_previous(data: dict) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> None:
    print(f"Rail ticket monitor started for {ROUTE['origin']} -> {ROUTE['destination']}")
    previous = load_previous()
    results = check_tickets(ROUTE["origin"], ROUTE["destination"])
    best = choose_best_offer(results)

    if best:
        current_best = {
            "train_name": best.train_name,
            "train_number": best.train_number,
            "travel_class": best.travel_class,
            "fare": best.fare,
            "availability": best.availability,
        }

        last_best = previous.get("last_best")
        if last_best != current_best:
            notify(
                "Better ticket found: "
                f"{best.train_name} ({best.train_number}) | {best.travel_class} | "
                f"₹{best.fare} | {best.availability}"
            )

        previous["last_best"] = current_best

    save_previous(previous)


if __name__ == "__main__":
    main()
