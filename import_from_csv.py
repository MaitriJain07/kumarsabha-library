import csv
from app import create_app
from app.extensions import db
from app.models import Book, Category

def import_books(csv_path="books_data.csv"):
    app = create_app()
    with app.app_context():
        # Get or create a default category (e.g., "General")
        default_cat = Category.query.filter_by(name="General").first()
        if not default_cat:
            default_cat = Category(name="General", slug="general")
            db.session.add(default_cat)
            db.session.commit()

        count = 0
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row.get('PUSTAK', '').strip()
                author = row.get('author', '').strip()
                year_str = row.get('DATE', '').strip()

                # Skip rows without title or author
                if not title or not author:
                    continue

                # Parse year (handle "-----" or empty)
                year = None
                if year_str and year_str.isdigit():
                    year = int(year_str)

                # Avoid duplicates (simple check by title+author)
                existing = Book.query.filter_by(title=title, author=author).first()
                if existing:
                    print(f"Skipping duplicate: {title} by {author}")
                    continue

                book = Book(
                    title=title,
                    author=author,
                    year=year,
                    category_id=default_cat.id,
                    description="",          # you can add later
                    tags="",                 # you can add later
                    is_rare=False
                )
                db.session.add(book)
                count += 1

        db.session.commit()
        print(f"✅ Imported {count} new books into the database.")

if __name__ == "__main__":
    import_books()