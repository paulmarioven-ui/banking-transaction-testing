# Banking Transaction Testing

## Project Overview

A banking transaction data validation and automated testing project designed to validate transaction records and identify invalid banking data.

The project uses Python, pytest, CSV data and SQL database scripts to demonstrate automated validation and testing of banking transactions.

## Objectives

- Validate banking transaction records
- Identify invalid transaction amounts
- Validate transaction currencies
- Validate transaction types
- Validate transaction statuses
- Identify pending and reversed transactions
- Automate validation using pytest
- Run automated tests through GitHub Actions

## Technologies Used

- Python
- pytest
- SQL
- CSV
- Git
- GitHub
- GitHub Actions

## Project Structure

```text
banking-transaction-testing/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── scripts/
│   └── validate_transactions.py
│
├── tests/
│   ├── data/
│   │   └── transaction.csv
│   ├── test_invalid_transactions.py
│   ├── test_transaction_csv.py
│   └── test_transactions.py
│
└── README.md
