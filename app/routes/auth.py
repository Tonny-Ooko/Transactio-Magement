from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required
from ..models import User
from ..extensions import db


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and user.check_password(request.form["password"]):
            login_user(user)
            return redirect("/")
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(username=request.form["username"], role="accountant")
        user.set_password(request.form["password"])
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
