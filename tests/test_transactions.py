import pytest


VALID_TRANSACTION_TYPES = [
    "DEPOSIT",
    "WITHDRAWAL",
    "TRANSFER",
    "PAYMENT"
]

VALID_CURRENCIES = [
    "GBP",
    "EUR",
    "USD"
]

VALID_STATUSES = [
    "COMPLETED",
    "PENDING",
    "FAILED",
    "REVERSED"
]


def test_transaction_amount_is_positive():
    transaction = {
        "transaction_type": "DEPOSIT",
        "amount": 1500.00,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["amount"] > 0


def test_transaction_amount_cannot_be_zero():
    transaction = {
        "transaction_type": "DEPOSIT",
        "amount": 0.00,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["amount"] <= 0


def test_transaction_amount_cannot_be_negative():
    transaction = {
        "transaction_type": "WITHDRAWAL",
        "amount": -100.00,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["amount"] <= 0


def test_transaction_currency_is_valid():
    transaction = {
        "transaction_type": "TRANSFER",
        "amount": 250.00,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["currency"] in VALID_CURRENCIES


def test_transaction_currency_is_invalid():
    transaction = {
        "transaction_type": "PAYMENT",
        "amount": 75.50,
        "currency": "XXX",
        "status": "COMPLETED"
    }

    assert transaction["currency"] not in VALID_CURRENCIES


def test_transaction_type_is_valid():
    transaction = {
        "transaction_type": "PAYMENT",
        "amount": 75.50,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["transaction_type"] in VALID_TRANSACTION_TYPES


def test_transaction_type_is_invalid():
    transaction = {
        "transaction_type": "INVALID",
        "amount": 75.50,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["transaction_type"] not in VALID_TRANSACTION_TYPES


def test_transaction_status_is_valid():
    transaction = {
        "transaction_type": "PAYMENT",
        "amount": 75.50,
        "currency": "GBP",
        "status": "COMPLETED"
    }

    assert transaction["status"] in VALID_STATUSES


def test_pending_transaction():
    transaction = {
        "transaction_type": "WITHDRAWAL",
        "amount": 100.00,
        "currency": "GBP",
        "status": "PENDING"
    }

    assert transaction["status"] == "PENDING"


def test_reversed_transaction_is_valid():
    transaction = {
        "transaction_type": "TRANSFER",
        "amount": 500.00,
        "currency": "GBP",
        "status": "REVERSED"
    }

    assert transaction["status"] in VALID_STATUSES