from flask import Blueprint, render_template, request
from prepsmarter.extensions import conn

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/login')
def login():
    return render_template('login.html')