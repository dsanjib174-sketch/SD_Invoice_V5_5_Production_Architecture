from flask import Blueprint, render_template

superadmin_bp = Blueprint("superadmin", __name__)

@superadmin_bp.route("/clients")
def clients():
    return render_template("superadmin/clients.html")

@superadmin_bp.route("/plans")
def plans():
    return render_template("superadmin/plans.html")

@superadmin_bp.route("/updates")
def updates():
    return render_template("superadmin/updates.html")
