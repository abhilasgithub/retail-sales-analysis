
# 🛒 Retail Sales Analysis Dashboard

A data analytics dashboard built with **Python** and **Streamlit** that connects
to a **PostgreSQL database** to visualise and explore retail sales data in real time.

## 📌 What This Project Does

This dashboard allows users to:
- Explore retail sales data interactively through charts and filters
- Analyse sales trends over time (daily, monthly, yearly)
- Break down revenue by product category, region, and customer segment
- Identify top-performing products and underperforming areas
- Query live data from a PostgreSQL database on every page load

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit (Python) |
| Backend / Data | Python, Pandas, SQLAlchemy |
| Database | PostgreSQL (Neon / Supabase) |
| Visualisation | Plotly / Matplotlib |
| Language | Python 3 |

## 📁 Project Structure
```
retail-sales-analysis/
├── app.py              ← Main Streamlit dashboard
├── schema.sql          ← Database schema + sample data
├── requirements.txt    ← Python dependencies
└── README.md
```

## 🗄️ Database Schema

The project uses a single `sales` table with fields including:
- `order_id` — unique transaction ID
- `order_date` — date of sale
- `product_category` — category of item sold
- `region` — geographic sales region
- `quantity` — units sold
- `unit_price` — price per unit
- `total_revenue` — auto-calculated total

## 📊 Dashboard Features

- **Sales Overview** — KPI cards for total revenue, orders, and average order value
- **Time Series Chart** — revenue trend over selected date range
- **Category Breakdown** — pie/bar chart by product category
- **Regional Analysis** — sales performance by region
- **Top Products** — ranked table of best-selling items
- **Filters** — interactive date range, category, and region filters

## 🔧 Dependencies
```
streamlit
pandas
sqlalchemy
psycopg2-binary
plotly
python-dotenv
```

## 💡 Key Concepts Demonstrated

- Connecting Python to a live PostgreSQL database using SQLAlchemy
- Writing optimised SQL queries for aggregation and filtering
- Building interactive data visualisations with Plotly
- Structuring a clean Streamlit multi-section dashboard
- Environment-based configuration using `.env` / secrets
- 
