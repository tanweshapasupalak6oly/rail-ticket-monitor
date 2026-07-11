from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TicketResult:
    train_name: str
    train_number: str
    travel_class: str
    fare: int
    availability: str


def check_tickets(origin: str, destination: str) -> list[TicketResult]:
    # Real ticket data source is not wired yet.
    print(f"Checking tickets for {origin} -> {destination}")
    return []


def choose_best_offer(results: list[TicketResult]) -> Optional[TicketResult]:
    if not results:
        return None
    return min(results, key=lambda item: item.fare)
