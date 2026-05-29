from flask import Blueprint, render_template

invoice_bp = Blueprint("invoice", __name__)

@invoice_bp.route("/preview")
def preview():
    return render_template("invoice/professional_invoice.html")
