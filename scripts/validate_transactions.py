import csv


VALID_TRANSACTION_TYPES = {"DEPOSIT", "WITHDRAWAL", "TRANSFER"}
VALID_STATUSES = {"COMPLETED", "PENDING", "FAILED"}
VALID_CURRENCIES = {"GBP", "USD", "EUR"}


def validate_transaction(transaction):
    errors = []

    if not transaction.get("transaction_id"):
        errors.append("Missing transaction ID")

    if not transaction.get("customer_id"):
        errors.append("Missing customer ID")

    if transaction.get("transaction_type") not in VALID_TRANSACTION_TYPES:
        errors.append("Invalid transaction type")

    try:
        amount = float(transaction.get("amount", 0))
        if amount <= 0:
            errors.append("Amount must be greater than zero")
    except (ValueError, TypeError):
        errors.append("Invalid amount")

    if transaction.get("currency") not in VALID_CURRENCIES:
        errors.append("Invalid currency")

    if transaction.get("transaction_status") not in VALID_STATUSES:
        errors.append("Invalid transaction status")

    if not transaction.get("reference"):
        errors.append("Missing transaction reference")

    return errors


def validate_csv(file_path):
    valid_count = 0
    invalid_count = 0

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for transaction in reader:
            errors = validate_transaction(transaction)

            if errors:
                invalid_count += 1
                print(
                    f"Invalid transaction "
                    f"{transaction.get('transaction_id')}: {errors}"
                )
            else:
                valid_count += 1

    print(f"\nValid transactions: {valid_count}")
    print(f"Invalid transactions: {invalid_count}")


if __name__ == "__main__":
    validate_csv("tests/data/transaction.csv")