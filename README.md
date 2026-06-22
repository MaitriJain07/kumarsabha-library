# 📚 Shri Badabazar Kumar Sabha Library

[![Flask](https://img.shields.io/badge/Flask-2.3+-black)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.11-slim)](https://python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue)](https://sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)](https://getbootstrap.com/)
[![HTMX](https://img.shields.io/badge/HTMX-1.9+-green)](https://htmx.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-cyan)](https://docker.com/)
[![AWS](https://img.shields.io/badge/AWS-EC2-orange)](https://aws.amazon.com/)

A bilingual, searchable library catalogue for a historic 1918 library in Kolkata. Built from scratch with live search, responsive design, and smart Hindi-to-Hinglish transliteration.

📅 Internship Project – Summer 2026 | [Maitri Jain](https://github.com/MaitriJain07)

---

## 🎯 The Problem

The **Shri Badabazar Kumar Sabha Pustakalaya** (established 1918) had:
- A static, non-responsive website
- No searchable book catalogue
- Historical content scattered across old pages
- No way for staff to manage or update book records
- 27,000+ books only available in scanned paper registers

## ✨ The Solution

A modern, bilingual web platform that:
- Provides a searchable, filterable book catalogue (title, author, category, year)
- Implements smart Hindi-to-Hinglish transliteration
- Displays books with detailed pages, related books, and rare book badges
- Restores historical content (library history, award lists, office bearers 1987–2016)
- Works perfectly on mobile, tablet, and desktop

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
- 📚 Custom Admin Dashboard – add/edit/delete books and categories
- 📤 Bulk Excel Upload – import 1000+ books at once (planned)
- 🖼️ Photo Gallery Management – upload and display library events (planned)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask 2.3+ (Python 3.11+) |
| Database | SQLite with SQLAlchemy ORM |
| Frontend | Bootstrap 5, Jinja2, HTMX, Alpine.js |
| Authentication | Flask-Login |
| Search & Filters | Custom Python logic + Hinglish transliteration |
| Containerization | Docker + Docker Compose |
| Cloud Deployment | AWS EC2 (t3.micro, Ubuntu 26.04 LTS) |
| Version Control | Git + GitHub |

---
## 🐳 Docker & AWS Deployment

### Docker Deployment (Single Container)
```bash
docker build -t kumarsabha-library .
docker run -d -p 80:5000 --name kumar-app -v /home/ubuntu/kumarsabha-data:/app/instance kumarsabha-library
```
### Docker Compose (Multi-Container Orchestration)
```bash
docker compose up -d
docker compose ps
```
### Live Deployments
- Docker (Port 80): http://52.66.235.213 — Single-container deployment
- Docker Compose (Port 8080): http://52.66.235.213:8080 — Multi-container orchestration demo
### AWS Configuration
- EC2 Instance: t3.micro (Ubuntu 22.04)
- Security Groups: SSH (22), HTTP (80), Custom (8080)
- Persistent Volume: SQLite database mounted on host
- Container Lifecycle: Managed with Docker + Docker Compose

## 📂 Project Structure
```
kumarsabha-library/
├── app/
│   ├── blueprints/
│   │   ├── __init__.py
│   │   ├── books.py
│   │   └── main.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── books.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── auth/
│   │   │   └── login.html
│   │   ├── books/
│   │   │   ├── _book_card.html
│   │   │   ├── _book_grid.html
│   │   │   ├── _filters.html
│   │   │   ├── _suggestions.html
│   │   │   ├── catalogue.html
│   │   │   ├── detail.html
│   │   │   └── rare.html
│   │   ├── main/
│   │   │   └── index.html
│   │   ├── pages/
│   │   │   ├── activities.html
│   │   │   ├── contact.html
│   │   │   ├── executive_committee.html
│   │   │   ├── history.html
│   │   │   ├── introduction.html
│   │   │   ├── photo_gallery.html
│   │   │   └── publications.html
│   │   ├── partials/
│   │   │   ├── footer.html
│   │   │   └── navbar.html
│   │   └── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── auth.py
│   ├── extensions.py
│   ├── forms.py
│   └── models.py
├── .github/
│   └── workflows/
│       └── deploy.yml
├── instance/
├── Dockerfile
├── docker-compose.yml
├── categorize_books.py
├── config.py
├── eng_data.csv
├── import_from_csv.py
├── requirements.txt
├── run.py
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
source venv/bin/activate  #On Windows: venv\Scripts\activate

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

### 5. Run the Application
```bash
python run.py
```
The app will create the database automatically on first run.

### 6. Import Book Data
```bash
python import_from_csv.py
python categorize_books.py
```

### 7. Visit the App
- Open http://127.0.0.1:5000 in your browser.

---
## 📈 Roadmap

**Phase 1 (Complete):**
- ✅ Live searchable catalogue (300+ books digitized)
- ✅ Docker + AWS EC2 deployment
- ✅ Docker Compose multi-container orchestration
- ✅ Linux system monitoring with cron automation

### Phase 2:

- Full admin dashboard with CRUD operations
- **Bulk import of remaining 27,000+ books from digitized registers**
- Bulk Excel upload for staff
- Photo gallery for events

### Phase 3:
- Executive committee dynamic pages
- Contact form with email integration
- Full-text search with SQLite FTS5
- Advanced analytics for rare books and user engagement

---

## 📄 License

This project is licensed under the **GNU General Public License v3 (GPL v3)**.

---

## 👩‍💻 Author

**Maitri Jain**
B.Tech CSE + IIT Madras BS in Data Science

[GitHub](https://github.com/MaitriJain07) | [Project Repo](https://github.com/MaitriJain07/kumarsabha-library)

---

This project was built from scratch during a summer internship – from requirements gathering to functional prototype, with clean Git history and deployed code.

Last updated: June 16, 2026
