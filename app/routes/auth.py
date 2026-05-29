from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def client_login():
    if request.method == "POST":
        # TODO: Validate client email, branch, user ID and password
        return redirect(url_for("dashboard.client_dashboard"))
    return render_template("auth/client_login.html")

@auth_bp.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        # TODO: Validate superadmin login
        return redirect(url_for("dashboard.superadmin_dashboard"))
    return render_template("auth/admin_login.html")

@auth_bp.route("/forgot-password")
def forgot_password():
    return "Forgot password module will be connected with OTP/email."
