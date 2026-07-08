from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class TicketResult:
    train_name: str
    train_number: str
    travel_class: str
    fare: int
    availability: str


def check_tickets(origin: str, destination: str) -> list[TicketResult]:
    # Placeholder implementation until we wire an official data source.
    return [
        TicketResult(
            train_name="Sample Express",
            train_number="00000",
            travel_class="3A",
            fare=1499,
            availability="WL12",
        )
    ]


def choose_best_offer(results: list[TicketResult]) -> TicketResult | None:
    if not results:
        return None
    return min(results, key=lambda item: item.fare)
