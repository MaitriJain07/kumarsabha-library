import csv
from app import create_app
from app.extensions import db
from app.models import Book, Category

def import_books_enriched(csv_path="eng_data.csv"):
    app = create_app()
    with app.app_context():
        # Get or create default category
        default_cat = Category.query.filter_by(name="General").first()
        if not default_cat:
            default_cat = Category(name="General", slug="general")
            db.session.add(default_cat)
            db.session.commit()
            print("Created 'General' category.")

        count = 0
        skipped = 0
        with open(csv_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            # Expected columns: PUSTAK, author, DATE, books-eng, author-eng
            for row in reader:
                title_hi = row.get('PUSTAK', '').strip()
                author_hi = row.get('author', '').strip()
                year_str = row.get('DATE', '').strip()
                title_en = row.get('books-eng', '').strip()
                author_en = row.get('author-eng', '').strip()

                # Skip rows without Hindi title or author
                if not title_hi or not author_hi:
                    skipped += 1
                    continue

                # Parse year
                year = None
                if year_str and year_str.isdigit():
                    year = int(year_str)
                elif year_str and year_str.replace('-', '').isdigit():
                    year = int(year_str.split('-')[0])  # handle "1981-82" -> 1981

                # Check duplicate
                existing = Book.query.filter_by(title=title_hi, author=author_hi).first()
                if existing:
                    print(f"Skipping duplicate: {title_hi} by {author_hi}")
                    skipped += 1
                    continue

                # Create new book
                book = Book(
                    title=title_hi,
                    author=author_hi,
                    year=year,
                    category_id=default_cat.id,
                    description="",
                    tags="",
                    is_rare=False,
                    title_en=title_en if title_en else None,
                    author_en=author_en if author_en else None
                )
                db.session.add(book)
                count += 1

                if count % 50 == 0:
                    print(f"Imported {count} books...")

        db.session.commit()
        print(f"✅ Imported {count} new books (skipped {skipped}) into the database.")

if __name__ == "__main__":
    import_books_enriched()