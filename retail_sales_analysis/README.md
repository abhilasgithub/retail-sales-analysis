# Retail Sales Analysis Dashboard

## Setup
1. Create a free DB on https://neon.tech or https://supabase.com
2. Run `schema.sql` to create and populate the table
3. Set your connection string: `export DATABASE_URL="your-db-url"`
4. Install deps: `pip install -r requirements.txt`
5. Run: `streamlit run app.py`

## Deploy (Free)
- Push to GitHub
- Go to https://streamlit.io/cloud → New App → connect repo
- Add `DATABASE_URL` in Secrets
