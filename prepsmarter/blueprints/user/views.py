from flask import Blueprint, render_template, request, jsonify
from prepsmarter.extensions import conn
from prepsmarter.blueprints.user.validators import * 
from prepsmarter.blueprints.user.services import UserRepository, UserService
from prepsmarter.blueprints.user.forms import RegistrationForm
from flask import current_app
from itsdangerous import URLSafeTimedSerializer, \
    TimedJSONWebSignatureSerializer
    
user = Blueprint('user', __name__, template_folder='templates')

def generate_registration_token(email):
    private_key = current_app.config['SECRET_KEY']
    s = URLSafeTimedSerializer(private_key)
    u = s.dumps(email)
    return u


@user.route('/activate/<activation_token>', methods=["GET"])
def activate(activation_token):
    private_key = current_app.config['SECRET_KEY']
    s = URLSafeTimedSerializer(private_key)
    u = s.loads(activation_token)
    return u

def send_registration_email(email):
    from prepsmarter.blueprints.user.tasks import deliver_contact_email
    token = generate_registration_token(email)
    host = current_app.config['HOST']
    activation_url = f"{host}/activate/{token}"
    try:
        deliver_contact_email(email, activation_url)
        return "ok"
    except Exception as e:
        return str(e)
    

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
        send_registration_email(new_user.email)
        return "new user created" #will probably change return statements later on
    return "new uer not created" #will probably change return statements later on
