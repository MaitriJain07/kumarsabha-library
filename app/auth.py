from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import UserMixin, login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from config import Config

auth_bp = Blueprint("auth", __name__)


class AdminUser(UserMixin):
    id = "admin"

    @staticmethod
    def get():
        return AdminUser()


@auth_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        password_hash = Config.ADMIN_PASSWORD_HASH

        if (
            username == Config.ADMIN_USERNAME
            and password_hash
            and check_password_hash(password_hash, password)
        ):
            login_user(AdminUser.get())
            next_url = request.args.get("next") or "/admin/"
            return redirect(next_url)

        flash("Invalid username or password.", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
