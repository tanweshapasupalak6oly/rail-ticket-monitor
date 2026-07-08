import json
from pathlib import Path

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
    save_previous(previous)


if __name__ == "__main__":
    main()
