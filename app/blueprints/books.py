from flask import Blueprint, abort, render_template, request

from app.extensions import db
from app.models import Book, Category
from app.services.books import filter_books, related_books

books_bp = Blueprint("books", __name__)


@books_bp.route("/books")
def catalogue():
    categories = Category.query.order_by(Category.name).all()
    books = filter_books(request.args)
    return render_template(
        "books/catalogue.html",
        books=books,
        categories=categories,
        filters=request.args,
    )


@books_bp.route("/books/filter")
def filter_fragment():
    books = filter_books(request.args)
    return render_template("books/_book_grid.html", books=books)


@books_bp.route("/book/<int:book_id>")
def detail(book_id):
    book = db.session.get(Book, book_id)
    if not book:
        abort(404)
    related = related_books(book)
    return render_template("books/detail.html", book=book, related_books=related)


@books_bp.route("/rare-books")
def rare_books():
    books = filter_books(request.args, rare_only=True)
    return render_template("books/rare.html", books=books)


@books_bp.route("/search-suggestions")
def search_suggestions():
    q = request.args.get("q", "").strip()
    if len(q) < 2:
        return ""
    term = f"%{q}%"
    titles = (
        Book.query.filter(Book.title.ilike(term)).limit(8).with_entities(Book.title).all()
    )
    return render_template(
        "books/_suggestions.html",
        suggestions=[t[0] for t in titles],
    )
