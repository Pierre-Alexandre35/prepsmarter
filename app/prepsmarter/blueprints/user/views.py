from flask import Blueprint, render_template, request, jsonify
from prepsmarter.extensions import conn
from prepsmarter.blueprints.user.validators import * 
from prepsmarter.blueprints.user.services import UserRepository, UserService
from datetime import datetime

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/register')
def login():
    return render_template('register.html')


@user.route('/new-user',methods = ['POST'])
def register_user():
    registration_form_data = request.form.to_dict()
    today_date = datetime.today().strftime('%Y-%m-%d')
    user_repository = UserRepository(conn, 'users')
    user_service = UserService()
    foo_user = user_service.register_user(
        registration_form_data('email'),
        registration_form_data('password'),
        datetime.today().strftime('%Y-%m-%d'),
        1,
        1, 
        today_date,
        today_date)
    user_repository.add_user(foo_user)
    user_repository.save()
    return "ok"
