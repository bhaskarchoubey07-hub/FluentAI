# FluentAI

Production-ready AI language learning web app built with Streamlit, OpenAI, SQLAlchemy, and PostgreSQL or SQLite.

## Run locally

1. Install dependencies:

```powershell
pip install -r app/requirements.txt
```

2. Create your environment file:

```powershell
Copy-Item .env.example .env
```

3. Set your API key and database URL in `.env`.

4. Start the app:

```powershell
streamlit run main.py
```

## Aiven PostgreSQL setup

Use your Aiven Postgres connection details and set:

```env
DATABASE_URL=postgresql+psycopg2://avnadmin:your_password@your-host.aivencloud.com:12345/defaultdb?sslmode=require
```

Notes:
- `sslmode=require` is important for Aiven.
- If Aiven gives you a `postgres://...` or `postgresql://...` URL, the app now normalizes it automatically for SQLAlchemy.
- Tables are created automatically on app startup.

## Fallback database

If `DATABASE_URL` is missing, the app falls back to local SQLite:

```env
DATABASE_URL=sqlite:///fluentai.db
```
