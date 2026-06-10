from flask import redirect, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app.extensions import db
from app.models import Book, Category


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login", next=request.url))


class BookAdmin(SecureModelView):
    column_list = ["title", "author", "year", "category", "is_rare"]
    column_searchable_list = ["title", "author", "tags"]
    column_filters = ["is_rare", "category", "year"]
    form_columns = [
        "title",
        "subtitle",
        "author",
        "year",
        "category",
        "description",
        "tags",
        "is_rare",
        "cover_image_url",
        "pdf_preview_url",
    ]


class CategoryAdmin(SecureModelView):
    column_list = ["name", "slug"]


def init_admin(app):
    admin = Admin(app, name="Kumar Sabha Admin", url="/admin")
    admin.add_view(BookAdmin(Book, db.session, name="Books", endpoint="books_admin"))
    admin.add_view(
        CategoryAdmin(Category, db.session, name="Categories", endpoint="categories_admin")
    )
