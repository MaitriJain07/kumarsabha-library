"""Load sample categories and books. Run: python seed.py"""
from app import create_app
from app.extensions import db
from app.models import Book, Category

SAMPLE_CATEGORIES = [
    ("Novel", "novel"),
    ("Philosophy", "philosophy"),
    ("Poetry", "poetry"),
    ("History", "history"),
]

SAMPLE_BOOKS = [
    {
        "title": "अहंकार (Ahankar)",
        "author": "Munshi Premchand",
        "year": 1934,
        "category_slug": "novel",
        "description": "प्रेमचंद की प्रसिद्ध कृति।",
        "tags": "fiction, classic",
        "is_rare": True,
    },
    {
        "title": "गीता-परिक्रमा (vol 1)",
        "author": "Vishnukant Shastri",
        "year": 2006,
        "category_slug": "philosophy",
        "description": "गीता पर विश्नुकांत शास्त्री का गहन टीका-टिप्पणी संग्रह।",
        "tags": "philosophy, scripture",
        "is_rare": False,
    },
    {
        "title": "राम प्रताप",
        "author": "Gopal Das",
        "year": 1690,
        "category_slug": "poetry",
        "description": "दुर्लभ ऐतिहासिक काव्य संग्रह।",
        "tags": "poetry, rare manuscript",
        "is_rare": True,
    },
    {
        "title": "भारतीय संस्कृति का इतिहास",
        "author": "Dr. Premshankar Tripathi",
        "year": 1998,
        "category_slug": "history",
        "description": "भारतीय सांस्कृतिक इतिहास पर विस्तृत अध्ययन।",
        "tags": "history, culture",
        "is_rare": False,
    },
    {
        "title": "कविता का सौंदर्य",
        "author": "Indushekhar Tatpurush",
        "year": 2015,
        "category_slug": "poetry",
        "description": "काव्य सौंदर्यशास्त्र पर निबंध संग्रह।",
        "tags": "poetry, aesthetics",
        "is_rare": False,
    },
    {
        "title": "विवेकानन्द: जीवन और विचार",
        "author": "Vishnukant Shastri",
        "year": 2010,
        "category_slug": "philosophy",
        "description": "स्वामी विवेकानन्द पर शास्त्रीय अध्ययन।",
        "tags": "philosophy, biography",
        "is_rare": False,
    },
]


def seed():
    app = create_app()
    with app.app_context():
        if Category.query.first():
            print("Database already seeded. Skipping.")
            return

        slug_to_cat = {}
        for name, slug in SAMPLE_CATEGORIES:
            cat = Category(name=name, slug=slug)
            db.session.add(cat)
            slug_to_cat[slug] = cat
        db.session.flush()

        for data in SAMPLE_BOOKS:
            slug = data.pop("category_slug")
            book = Book(category=slug_to_cat[slug], **data)
            db.session.add(book)

        db.session.commit()
        print(f"Seeded {len(SAMPLE_CATEGORIES)} categories and {len(SAMPLE_BOOKS)} books.")


if __name__ == "__main__":
    seed()
