from sqlalchemy import or_
from app.models import Book

# Simple mapping of common English words to Devanagari
ENGLISH_TO_DEVANAGARI = {
    'geeta': 'गीता',
    'gita': 'गीता',
    'ram': 'राम',
    'rama': 'राम',
    'krishna': 'कृष्ण',
    'yoga': 'योग',
    'veda': 'वेद',
    'vedas': 'वेद',
    'upanishad': 'उपनिषद',
    'upanishads': 'उपनिषद',
    'purana': 'पुराण',
    'mahabharata': 'महाभारत',
    'ramayana': 'रामायण',
    'bhagavad': 'भगवद',
    'bhagavad gita': 'भगवद्गीता',
    'shiva': 'शिव',
    'vishnu': 'विष्णु',
    'darshan': 'दर्शन',
    'philosophy': 'दर्शन',
    'dictionary': 'कोष',
    'kosh': 'कोष',
    'kavita': 'कविता',
    'poetry': 'कविता',
    'katha': 'कथा',
    'story': 'कथा',
    'nitishastra': 'नीतिशास्त्र',
    'ethics': 'नीति',
    'yog': 'योग',
    'pranayam': 'प्राणायाम',
    'buddha': 'बुद्ध',
    'buddhist': 'बौद्ध',
    'jain': 'जैन',
    'mantra': 'मंत्र',
    'tantra': 'तंत्र',
    'ayurveda': 'आयुर्वेद',
    'sanskrit': 'संस्कृत',
    'hindi': 'हिंदी',
}

def to_devanagari(text):
    """Convert common English words to Devanagari. Returns original if no mapping."""
    words = text.lower().split()
    converted = []
    for w in words:
        # Check if whole word maps
        if w in ENGLISH_TO_DEVANAGARI:
            converted.append(ENGLISH_TO_DEVANAGARI[w])
        else:
            # Try partial matches? Not needed for basic search.
            converted.append(w)
    return ' '.join(converted)

def filter_books(args=None, rare_only=False):
    args = args or {}
    search = args.get("search")
    category = args.get("category")
    year_min = args.get("year_min")
    year_max = args.get("year_max")

    q = Book.query

    if rare_only:
        q = q.filter(Book.is_rare.is_(True))

    if search:
        search_term = search.strip()
        # Create a list of possible search variants
        variants = [search_term]
        # Add transliterated version if different
        dev_term = to_devanagari(search_term)
        if dev_term and dev_term != search_term:
            variants.append(dev_term)
        # Build OR conditions across title and author for all variants
        conditions = []
        for variant in variants:
            pattern = f"%{variant}%"
            conditions.append(Book.title.ilike(pattern))
            conditions.append(Book.author.ilike(pattern))
        # Apply filter using OR of all conditions
        q = q.filter(or_(*conditions))

    if category and category != 'all' and category.isdigit():
        q = q.filter(Book.category_id == int(category))

    if year_min and year_min.isdigit():
        q = q.filter(Book.year >= int(year_min))

    if year_max and year_max.isdigit():
        q = q.filter(Book.year <= int(year_max))

    return q.order_by(Book.title).all()

def related_books(book, limit=4):
    same_author = (
        Book.query.filter(Book.author == book.author, Book.id != book.id)
        .limit(limit)
        .all()
    )
    if len(same_author) >= limit:
        return same_author[:limit]

    remaining = limit - len(same_author)
    same_category = (
        Book.query.filter(
            Book.category_id == book.category_id,
            Book.id != book.id,
            Book.id.notin_([b.id for b in same_author]),
        )
        .limit(remaining)
        .all()
    )
    return same_author + same_category