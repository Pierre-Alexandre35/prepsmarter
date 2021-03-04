from prepsmarter.blueprints.user.models import User
import datetime
from prepsmarter.blueprints.user.hashers import get_hashed_password
from datetime import datetime

class UserRepository():
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table  
    
    
    def add_user(self, user):
        sql = "INSERT INTO users (email, password, is_active, sign_in_count, current_sign_in_on, last_sign_in_on) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = self.conn.cursor()
        # the is_active column in the DB is a tinyint(1). True = 1 and False = 0
        if user.active == True:
            is_active = 1
        is_active = 0
        cursor.execute(sql, ( user.email, user.password, is_active, user.sign_in_count, user.current_sign_in_on, user.last_sign_in_on))
        resp = cursor.fetchall()
        return resp
    
    def delete_user(self):
        return ""
    
    def get_user(self):
        return ""
    
    def save(self):
        self.conn.commit()
    


class UserService():
    def register_user(self,
                      email,
                      password):
        sign_in_count = 1
        today_date = datetime.today().strftime('%Y-%m-%d')
        active = True
        new_user = User(email, password, today_date, active,
                        sign_in_count, today_date, today_date)
        return new_user

    def desactivate_user(self, User):
        if User.active == False:
            print(f"User {User.email} is already inactive")
        User.active = False

    def reactive_user(self, User):
        if User.active == True:
            print(f"User {User.email} is already active")
        User.active = True

    def is_active(self, User):
        return User.is_active

    def update_activity_tracking(self, User, ip_address):
        User.sign_in_count += 1
        User.last_sign_in_on = User.current_sign_in_on
        User.current_sign_in_on = datetime.datetime.now()

    def update_password(self, User, new_password):
        User.password = get_hashed_password(new_password)

