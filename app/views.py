from flask import Blueprint, render_template
from flask_login import login_required, login_user, current_user, logout_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)