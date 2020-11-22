from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    if current_user.user_type == "Patient":
        return render_template('userprofile.html', name=current_user.name,user_type=current_user.user_type)
    elif current_user.user_type == "Doctor":
        return render_template('medprofile.html', name=current_user.name,user_type=current_user.user_type)
    else:
        return "BadResponse", 400
