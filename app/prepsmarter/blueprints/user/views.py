from flask import Blueprint, render_template, request, jsonify
from prepsmarter.extensions import conn
from prepsmarter.blueprints.user.validators import * 
from prepsmarter.blueprints.user.services import UserRepository, UserService

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/register')
def login():
    return render_template('register.html')


@user.route('/new-user',methods = ['POST'])
def register_user():
    user_repository = UserRepository(conn, 'userss')
    user_service = UserService()
    foo_user = user_service.register_user('pierre@gmail.com',
                                     '200799jtm1',
                                     '2020-01-12',
                                     True,
                                     13,
                                     '2021-02-21',
                                     '2021-02-20')

    user_repository.add_user(foo_user)
    user_repository.save()
    return "ok"
