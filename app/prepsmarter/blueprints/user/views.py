from flask import Blueprint, render_template, request
from prepsmarter.extensions import conn

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/register')
def login():
    return render_template('register.html')


@user.route('/new-user',methods = ['POST'])
def new_user():
    return "dd"