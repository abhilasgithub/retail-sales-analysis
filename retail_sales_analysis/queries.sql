-- Monthly Revenue Trend
SELECT 
  TO_CHAR(sale_date, 'YYYY-MM') AS month,
  SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Top Performing Categories
SELECT 
  category,
  SUM(quantity * unit_price) AS revenue,
  SUM(quantity) AS units_sold
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- Region-wise Performance
SELECT 
  region,
  COUNT(*) AS transactions,
  SUM(quantity * unit_price) AS total_revenue,
  ROUND(AVG(quantity * unit_price), 2) AS avg_order_value
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
