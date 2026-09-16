import csv
from pathlib import Path

import pytest


CSV_FILE = Path(__file__).parent / "data" / "transaction.csv"


def load_transactions():
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@pytest.mark.parametrize("transaction", load_transactions())
def test_transaction_from_csv(transaction):
    assert transaction["transaction_id"]
    assert transaction["customer_id"]
    assert transaction["transaction_type"] in [
        "DEPOSIT",
        "TRANSFER",
        "PAYMENT",
        "WITHDRAWAL",
    ]
    assert float(transaction["amount"]) > 0
    assert transaction["currency"] == "GBP"
    assert transaction["status"] in [
        "COMPLETED",
        "PENDING",
        "FAILED",
    ]