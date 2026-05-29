from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def client_dashboard():
    return render_template("dashboard/client_dashboard.html")

@dashboard_bp.route("/admin-dashboard")
def superadmin_dashboard():
    return render_template("dashboard/superadmin_dashboard.html")
