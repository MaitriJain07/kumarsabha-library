import smtplib
from email.message import EmailMessage

from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

from app.forms import ContactForm
from app.models import Book

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    featured = Book.query.order_by(Book.created_at.desc()).limit(4).all()
    rare = Book.query.filter_by(is_rare=True).limit(4).all()
    return render_template("main/index.html", featured_books=featured, rare_books=rare)


@main_bp.route("/introduction")
def introduction():
    return render_template("pages/introduction.html")


@main_bp.route("/history")
def history():
    return render_template("pages/history.html")


@main_bp.route("/executive-committee")
def executive_committee():
    return render_template("pages/executive_committee.html")


@main_bp.route("/photo-gallery")
def photo_gallery():
    return render_template("pages/photo_gallery.html")


@main_bp.route("/publications")
def publications():
    return render_template("pages/publications.html")


@main_bp.route("/activities")
def activities():
    return render_template("pages/activities.html")


@main_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        sent = _send_contact_email(
            form.name.data,
            form.email.data,
            form.message.data,
        )
        if sent:
            flash("आपका संदेश भेज दिया गया है। धन्यवाद!", "success")
        else:
            flash(
                "संदेश भेजने में समस्या हुई। कृपया सीधे ईमेल या फ़ोन से संपर्क करें।",
                "warning",
            )
        return redirect(url_for("main.contact"))
    return render_template("pages/contact.html", form=form)


def _send_contact_email(name, email, message):
    cfg = current_app.config
    if not cfg.get("MAIL_USERNAME") or not cfg.get("MAIL_PASSWORD"):
        current_app.logger.info(
            "Contact form (mail not configured): %s <%s> — %s", name, email, message
        )
        return False
    msg = EmailMessage()
    msg["Subject"] = f"Kumar Sabha website contact from {name}"
    msg["From"] = cfg["MAIL_USERNAME"]
    msg["To"] = cfg["LIBRARY_EMAIL"]
    msg.set_content(f"From: {name} <{email}>\n\n{message}")
    try:
        with smtplib.SMTP(cfg["MAIL_SERVER"], cfg["MAIL_PORT"]) as server:
            if cfg.get("MAIL_USE_TLS"):
                server.starttls()
            server.login(cfg["MAIL_USERNAME"], cfg["MAIL_PASSWORD"])
            server.send_message(msg)
        return True
    except Exception:
        current_app.logger.exception("Failed to send contact email")
        return False
