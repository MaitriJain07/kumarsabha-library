from sqlalchemy import or_

from app.models import Book


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
        term = f"%{search.strip()}%"
        q = q.filter(or_(Book.title.ilike(term), Book.author.ilike(term)))

    if category:
        q = q.filter(Book.category_id == int(category))

    if year_min:
        q = q.filter(Book.year >= int(year_min))

    if year_max:
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
