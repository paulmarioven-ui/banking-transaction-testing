-- Sample Banking Transaction Data

INSERT INTO customers (customer_name, account_number)
VALUES
('John Smith', 'ACC10001'),
('Sarah Johnson', 'ACC10002'),
('Michael Brown', 'ACC10003'),
('Emma Wilson', 'ACC10004');

INSERT INTO transactions
(customer_id, transaction_type, amount, currency, transaction_status, transaction_date, reference)
VALUES
(1, 'DEPOSIT', 1500.00, 'GBP', 'COMPLETED', '2026-09-01 09:15:00', 'TXN10001'),
(2, 'TRANSFER', 250.00, 'GBP', 'COMPLETED', '2026-09-01 10:30:00', 'TXN10002'),
(3, 'PAYMENT', 75.50, 'GBP', 'COMPLETED', '2026-09-02 11:00:00', 'TXN10003'),
(4, 'WITHDRAWAL', 100.00, 'GBP', 'PENDING', '2026-09-02 14:20:00', 'TXN10004'),
(1, 'TRANSFER', 500.00, 'GBP', 'FAILED', '2026-09-03 15:45:00', 'TXN10005'),
(2, 'DEPOSIT', 2000.00, 'GBP', 'COMPLETED', '2026-09-04 08:30:00', 'TXN10006');