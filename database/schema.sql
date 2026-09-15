-- Banking Transaction Testing Database Schema

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    transaction_status VARCHAR(20) NOT NULL,
    transaction_date TIMESTAMP NOT NULL,
    reference VARCHAR(50) UNIQUE NOT NULL,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT valid_transaction_type
        CHECK (transaction_type IN ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER', 'PAYMENT')),

    CONSTRAINT valid_amount
        CHECK (amount > 0),

    CONSTRAINT valid_status
        CHECK (transaction_status IN ('COMPLETED', 'PENDING', 'FAILED', 'REVERSED'))
);