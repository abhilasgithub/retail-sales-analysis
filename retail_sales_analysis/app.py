import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ── use your Supabase / Neon connection string via env var ──
# export DATABASE_URL="postgresql://user:pass@host:5432/dbname"

@st.cache_resource
def get_conn():
    import psycopg2
    return psycopg2.connect(os.environ["DATABASE_URL"])

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")
st.title("🛒 Retail Sales Analysis Dashboard")

conn = get_conn()

# Monthly Revenue
df_monthly = pd.read_sql("""
    SELECT TO_CHAR(sale_date, 'YYYY-MM') AS month,
           SUM(quantity * unit_price) AS total_revenue
    FROM sales GROUP BY month ORDER BY month
""", conn)
fig1 = px.line(df_monthly, x='month', y='total_revenue',
               title='Monthly Revenue Trend', markers=True)
st.plotly_chart(fig1, use_container_width=True)

col1, col2 = st.columns(2)

# Category Breakdown
with col1:
    df_cat = pd.read_sql("""
        SELECT category, SUM(quantity * unit_price) AS revenue
        FROM sales GROUP BY category
    """, conn)
    fig2 = px.pie(df_cat, names='category', values='revenue',
                  title='Revenue by Category')
    st.plotly_chart(fig2, use_container_width=True)

# Region Table
with col2:
    df_region = pd.read_sql("""
        SELECT region,
               SUM(quantity * unit_price) AS total_revenue,
               COUNT(*) AS transactions
        FROM sales GROUP BY region ORDER BY total_revenue DESC
    """, conn)
    fig3 = px.bar(df_region, x='region', y='total_revenue',
                  title='Revenue by Region', color='region')
    st.plotly_chart(fig3, use_container_width=True)

st.subheader("Raw Data")
df_all = pd.read_sql("SELECT * FROM sales ORDER BY sale_date", conn)
st.dataframe(df_all, use_container_width=True)
