-- =========================
-- CREATE TABLE
-- =========================

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    wallet_balance DECIMAL(10,2)
);

CREATE TABLE orders (
    queue_id INT PRIMARY KEY,
    menu VARCHAR(100),
    total_price DECIMAL(10,2),
    status VARCHAR(20)
);

-- =========================
-- INSERT DATA (อย่างน้อย 3 รายการ)
-- =========================

INSERT INTO users (user_id, name, wallet_balance)
VALUES 
(1, 'Bas', 200.00),
(2, 'Aom', 150.00),
(3, 'Ken', 300.00);

INSERT INTO orders (queue_id, menu, total_price, status)
VALUES 
(101, 'Pad Thai', 50.00, 'Pending'),
(102, 'Fried Rice', 60.00, 'Pending'),
(103, 'Noodle Soup', 45.00, 'Ready');

-- =========================
-- UPDATE STATUS
-- =========================

UPDATE orders
SET status = 'Ready'
WHERE status = 'Pending' AND queue_id = 101;

-- =========================
-- SELECT QUERY (เฉพาะ Pending)
-- =========================

SELECT *
FROM orders
WHERE status = 'Pending';