import csv
from app import create_app
from app.extensions import db
from app.models import Book, Category

# Mapping: list of keywords (in Hindi/English) -> category name and slug
CATEGORY_MAP = [
    (["गीता", "geeta", "gita", "भगवद्गीता"], "Gita & Philosophy", "gita-philosophy"),
    (["कोष", "कोश", "dictionary", "शब्द", "शब्दकोश"], "Dictionary", "dictionary"),
    (["योग", "pranayama", "प्राणायाम", "ध्यान"], "Yoga & Meditation", "yoga-meditation"),
    (["दर्शन", "philosophy", "तत्व", "अद्वैत", "वेदान्त"], "Philosophy", "philosophy"),
    (["उपनिषद", "upanishad", "वेद"], "Upanishads & Vedas", "upanishads-vedas"),
    (["जैन", "jain", "भक्तामर", "जिन"], "Jainism", "jainism"),
    (["बौद्ध", "buddha", "धम्मपद", "buddhist"], "Buddhism", "buddhism"),
    (["कहावत", "मुहावरे", "लोकोक्ति", "proverb"], "Proverbs & Idioms", "proverbs-idioms"),
    (["नीति", "ethic", "morality", "सदाचार"], "Ethics & Morality", "ethics-morality"),
    (["स्वामी", "विवेकानन्द", "रामतीर्थ", "परमहंस"], "Biography & Teachings", "biography-teachings"),
    (["कथा", "उपन्यास", "novel", "चन्द्रकान्त"], "Fiction & Novel", "fiction-novel"),
    (["इतिहास", "history", "सभ्यता", "संस्कृति"], "History & Culture", "history-culture"),
    (["विज्ञान", "science", "जीवन विज्ञान", "मनोविज्ञान"], "Science & Psychology", "science-psychology"),
]

def get_category_for_book(title):
    """Return category name and slug based on keywords in title."""
    title_lower = title.lower()
    for keywords, cat_name, cat_slug in CATEGORY_MAP:
        for kw in keywords:
            if kw in title_lower:
                return cat_name, cat_slug
    # Default category
    return "General", "general"

def add_categories_to_existing_books():
    """Update all existing books with appropriate categories."""
    app = create_app()
    with app.app_context():
        # Make sure all needed categories exist
        cat_cache = {}
        for _, name, slug in CATEGORY_MAP:
            cat = Category.query.filter_by(slug=slug).first()
            if not cat:
                cat = Category(name=name, slug=slug)
                db.session.add(cat)
                cat_cache[slug] = cat
        # Ensure General category exists
        if "general" not in cat_cache:
            gen = Category.query.filter_by(slug="general").first()
            if not gen:
                gen = Category(name="General", slug="general")
                db.session.add(gen)
            cat_cache["general"] = gen
        db.session.commit()

        # Iterate over all books
        books = Book.query.all()
        updated = 0
        for book in books:
            cat_name, cat_slug = get_category_for_book(book.title)
            target_cat = cat_cache.get(cat_slug)
            if target_cat and book.category_id != target_cat.id:
                book.category_id = target_cat.id
                updated += 1
        db.session.commit()
        print(f"✅ Updated categories for {updated} books.")

if __name__ == "__main__":
    add_categories_to_existing_books()