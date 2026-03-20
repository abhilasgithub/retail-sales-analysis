CREATE TABLE sales (
  sale_id SERIAL PRIMARY KEY,
  product_name VARCHAR(100),
  category VARCHAR(50),
  region VARCHAR(50),
  quantity INT,
  unit_price DECIMAL(10,2),
  sale_date DATE
);

INSERT INTO sales VALUES
(1, 'Laptop', 'Electronics', 'North', 5, 1200.00, '2024-01-15'),
(2, 'Phone', 'Electronics', 'South', 10, 800.00, '2024-01-20'),
(3, 'Desk', 'Furniture', 'East', 3, 450.00, '2024-02-10'),
(4, 'Chair', 'Furniture', 'West', 7, 200.00, '2024-02-18'),
(5, 'Tablet', 'Electronics', 'North', 4, 600.00, '2024-03-05'),
(6, 'Monitor', 'Electronics', 'South', 6, 400.00, '2024-03-22'),
(7, 'Bookshelf', 'Furniture', 'East', 2, 300.00, '2024-04-01'),
(8, 'Keyboard', 'Electronics', 'West', 15, 100.00, '2024-04-15');
