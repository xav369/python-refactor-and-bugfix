from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal


Status = Literal["paid", "pending", "failed"]


@dataclass(frozen=True)
class Record:
    amount: float
    status: Status


def summarize(records: Iterable[Record]) -> dict:
    counts = {"paid": 0, "pending": 0, "failed": 0}
    total_paid = 0.0

    for r in records:
        counts[r.status] += 1
        if r.status == "paid":
            total_paid += r.amount

    return {
        "total_paid": round(total_paid, 2),
        "counts": counts,
    }


if __name__ == "__main__":
    sample = [
        Record(amount=100.0, status="paid"),
        Record(amount=50.0, status="pending"),
        Record(amount=10.0, status="failed"),
    ]
    print(summarize(sample))
