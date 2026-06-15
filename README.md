# 📚 Shri Badabazar Kumar Sabha Library

[![Flask](https://img.shields.io/badge/Flask-2.3+-black)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.13.1-blue)](https://python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue)](https://sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)](https://getbootstrap.com/)
[![HTMX](https://img.shields.io/badge/HTMX-1.9+-green)](https://htmx.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-cyan)](https://docker.com/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

A bilingual, searchable library catalogue for a historic 1918 library in Kolkata. Built from scratch with live search, responsive design, and smart Hindi-to-Hinglish transliteration.

📅 Internship Project – Summer 2026 | [Maitri Jain](https://github.com/MaitriJain07)

---

## 🎯 The Problem

The **Shri Badabazar Kumar Sabha Pustakalaya** (established 1918) had:
- A static, non-responsive website
- No searchable book catalogue
- Historical content scattered across old pages
- No way for staff to manage or update book records
- 500+ books only available in scanned paper registers

## ✨ The Solution

A modern, bilingual web platform that:
- Provides a searchable, filterable book catalogue (title, author, category, year)
- Implements smart Hindi-to-Hinglish transliteration – so searching "kela prasad" finds "केला प्रसाद" without broken Google Translate nonsense
- Displays books with detailed pages, related books, and rare book badges
- Restores historical content (library history, award lists, office bearers 1987–2016)
- Works perfectly on mobile, tablet, and desktop
- Built with clean, version-controlled code (30+ Git commits showing iterative development)

---

## 🚀 Features (Completed & Live)

### For Visitors
- 🔍 Live Search & Filters – search by title, author, category, year with instant results (no page reloads via HTMX)
- 📖 Book Detail Pages – full descriptions, tags, related books, rare book badges
- 📜 Rare Books Section – highlights historical treasures from the collection
- 🏛️ Static Content – restored history, awards, committee records, activities
- 📱 Fully Responsive – optimised for mobile, tablet, desktop
- 🌐 Bilingual Search – Hinglish keywords intelligently map to Hindi titles using custom transliteration (not automated Google Translate)

### For Library Staff (In Progress)
- 🔐 Secure Admin Login (Flask-Login)
- 📚 Custom Admin Dashboard – add/edit/delete books and categories (under development – 0-20% complete)
- 📤 Bulk Excel Upload – import 100+ books at once (planned)
- 🖼️ Photo Gallery Management – upload and display library events (planned)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask 2.3+ (Python 3.13.1) |
| Database | SQLite with SQLAlchemy ORM |
| Frontend | Bootstrap 5, Jinja2, HTMX, Alpine.js |
| Authentication | Flask-Login |
| Search & Filters | Custom Python logic + Hinglish transliteration |
| Deployment | Docker + AWS (deployment coming soon) |
| Version Control | Git + GitHub |

---

## 📂 Project Structure

```
kumarsabha-library/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Book & Category models
│   ├── auth.py                  # Login logic (Flask-Login)
│   ├── forms.py                 # WTForms
│   ├── blueprints/
│   │   ├── main.py              # Homepage, history, awards
│   │   └── books.py             # Book catalogue, search, filters
│   ├── services/
│   │   ├── search.py            # Search logic + Hinglish transliteration
│   │   └── filters.py           # Category & year filters
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── books/
│       └── partials/
├── instance/
│   └── kumarsabha.db            # SQLite database (ignored by Git)
├── .dockerignore
├── Dockerfile                   # Docker setup for AWS deployment
├── docker-compose.yml
├── config.py                    # Environment variables
├── requirements.txt
├── run.py                       # Entry point
├── import_books.py              # Script to populate DB from CSV
├── books_data.csv               # Bilingual book data (500+ rows)
└── README.md
```

---

## 🧪 Getting Started (Local Development)

### Prerequisites
- Python 3.13.1+
- Git
- Virtual environment (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/MaitriJain07/kumarsabha-library.git
cd kumarsabha-library
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
```

Generate a secret key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Create Database & Tables

```bash
flask shell
```

Inside the Flask shell:
```python
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
    print("Database created!")
exit()
```

### 6. Import Book Data

```bash
python import_books.py
```

### 7. Run the App

```bash
flask run
```

Visit http://127.0.0.1:5000

---

## 🐳 Docker & AWS Deployment (Coming Soon)

This project is Docker-ready for scalable deployment:

```bash
docker build -t kumarsabha-library .
docker run -p 5000:5000 kumarsabha-library
```

**AWS Deployment Plan:**
- Push image to AWS ECR (Elastic Container Registry)
- Deploy on ECS (Elastic Container Service) or App Runner
- Use RDS for PostgreSQL (replacing SQLite in production)
- CloudFront CDN for static assets

Detailed deployment guide coming after core features are finalised.

---

## 📈 Roadmap (What's Next)

**Phase 2 (In Progress):**
- Custom admin dashboard (currently being built)
- Bulk Excel upload for staff
- Photo gallery for events

**Phase 3 (Planned):**
- Executive committee dynamic pages
- Contact form with email integration
- Full-text search with SQLite FTS5
- User analytics & admin reports

---

## 🤔 Why This Project Stands Out

1. Real-world problem – modernising a 1918 library with digitised collection
2. Bilingual intelligence – Hindi-to-Hinglish transliteration without breaking Google Translate
3. Clean code & Git history – 30+ commits showing iterative development
4. Scalable architecture – Flask app factory, modular blueprints, Docker-ready
5. Responsive & accessible – works perfectly on all devices
6. Portfolio-ready – built from requirements to local completion (deployment coming soon)

---

## 📄 License

MIT License – feel free to use, modify, and distribute with attribution.

---

## 👩‍💻 Author

**Maitri Jain**
B.Tech CSE + IIT Madras BS in Data Science

[GitHub](https://github.com/MaitriJain07) | [Project Repo](https://github.com/MaitriJain07/kumarsabha-library)

---

This project was built from scratch during a summer internship – from requirements gathering to functional prototype, with clean Git history and deployed code coming soon.

Last updated: June 2026
