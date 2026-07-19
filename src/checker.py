from __future__ import annotations

import os
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
    """Return ticket offers for a route.

    This repository does not yet have a live rail data source wired in.
    For now, the route is read from environment variables so the project
    can be configured without code changes.
    """
    source = os.getenv("RAIL_ORIGIN", origin)
    target = os.getenv("RAIL_DESTINATION", destination)
    print(f"Checking tickets for {source} -> {target}")
    return []


def choose_best_offer(results: list[TicketResult]) -> Optional[TicketResult]:
    if not results:
        return None
    return min(results, key=lambda item: item.fare)
