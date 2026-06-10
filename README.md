# Shri Badabazar Kumar Sabha Library Website

Modern Flask web app for **श्री बड़ाबाजार कुमारसभा पुस्तकालय** — searchable book catalogue, preserved static content, and admin panel.

## Stack

- Flask 3, SQLAlchemy, SQLite
- Bootstrap 5, Jinja2, HTMX, Alpine.js
- Flask-Admin + Flask-Login

## Quick start

```bash
cd kumar-sabha
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env
```

Generate an admin password hash:

```bash
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('your-password'))"
```

Set `ADMIN_PASSWORD_HASH` in `.env`, then:

```bash
python seed.py
python run.py
```

Open http://127.0.0.1:5000 — Admin: http://127.0.0.1:5000/admin/login

## Routes (spec)

| Route | Description |
|-------|-------------|
| `/` | Homepage |
| `/books` | Catalogue with HTMX filters |
| `/books/filter` | HTMX partial (book grid) |
| `/book/<id>` | Book detail + related books |
| `/rare-books` | Rare books only |
| `/search-suggestions` | Autocomplete (optional) |
| `/admin` | Flask-Admin (login required) |
