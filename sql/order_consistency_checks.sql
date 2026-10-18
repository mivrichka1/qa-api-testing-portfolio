-- Illustrative checks for a conventional shop schema (orders, order_items, products).
-- SauceDemo does not expose its production database; these queries are examples for
-- a local/test database with the columns described below, not executed against SauceDemo.

-- 1. Find orders whose stored total differs from the sum of their line items.
SELECT
    o.id AS order_id,
    o.total_amount AS stored_total,
    SUM(oi.quantity * oi.unit_price) AS calculated_total
FROM orders AS o
JOIN order_items AS oi ON oi.order_id = o.id
GROUP BY o.id, o.total_amount
HAVING ABS(o.total_amount - SUM(oi.quantity * oi.unit_price)) > 0.01;

-- 2. Find order items that reference a missing product.
SELECT oi.order_id, oi.product_id
FROM order_items AS oi
LEFT JOIN products AS p ON p.id = oi.product_id
WHERE p.id IS NULL;

-- 3. Find orders with no line items.
SELECT o.id AS order_id
FROM orders AS o
LEFT JOIN order_items AS oi ON oi.order_id = o.id
WHERE oi.order_id IS NULL;

-- 4. Check for negative quantities or prices.
SELECT order_id, product_id, quantity, unit_price
FROM order_items
WHERE quantity <= 0 OR unit_price < 0;
