from flask import Blueprint, render_template, request, jsonify
from prepsmarter.extensions import conn
from prepsmarter.blueprints.user.validators import * 
from prepsmarter.blueprints.user.services import UserRepository, UserService
from prepsmarter.blueprints.user.forms import RegistrationForm

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/register')
def login():
    return render_template('register.html')


@user.route('/new-user',methods = ['POST'])
def register_user():
    form_email = request.form.get('email')
    form_password = request.form.get('psw')
    form_password_repeat = request.form.get('psw-repeat')
    registration_form = RegistrationForm(form_email, form_password, form_password_repeat).validate_registration()
    
    if registration_form:
        new_user = UserService().register_user(form_email, form_password)
        user_repository = UserRepository(conn, 'users')
        user_repository.add_user(new_user)
        user_repository.save()
        return "ok" #will probably change return statements later on
    return "not ok" #will probably change return statements later on
