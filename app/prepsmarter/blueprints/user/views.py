from flask import Blueprint, render_template, request, jsonify
from prepsmarter.extensions import conn
from prepsmarter.blueprints.user.forms import (
    RegisterForm)

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/register')
def login():
    return render_template('register.html')


@user.route('/new-user',methods = ['POST'])
def new_user():
    form = RegisterForm(request.form.to_dict())
    print(form.password)
    return "0"