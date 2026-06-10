from datetime import datetime

from app.extensions import db


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    books = db.relationship("Book", back_populates="category", lazy="dynamic")

    def __str__(self):
        return self.name


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(200))
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    description = db.Column(db.Text)
    tags = db.Column(db.String(200))
    is_rare = db.Column(db.Boolean, default=False, nullable=False)
    cover_image_url = db.Column(db.String(300))
    pdf_preview_url = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    category = db.relationship("Category", back_populates="books")

    @property
    def tag_list(self):
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(",") if t.strip()]

    def __str__(self):
        return self.title
