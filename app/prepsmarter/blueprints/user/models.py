import datetime
from hashers import get_hashed_password


class UserService():
    def register_user(self,
                      email,
                      password,
                      registration_date,
                      active,
                      sign_in_count,
                      current_sign_in_on,
                      last_sign_in_on):
        new_user = User(email, password, registration_date, active,
                        sign_in_count, current_sign_in_on, last_sign_in_on)
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


class User():
    def __init__(self, email, password, registration_date, active, sign_in_count, current_sign_in_on, last_sign_in_on):
        self.email = email
        self.password = password
        self.registration_date = registration_date
        self.active = active

        # Activity tracking
        self.sign_in_count = sign_in_count
        self.current_sign_in_on = current_sign_in_on
        self.last_sign_in_on = last_sign_in_on

    def __str__(self):
        user_attributes = vars(self)
        return (', '.join("%s: %s" % item for item in user_attributes.items()))


user_service = UserService()

user_1 = user_service.register_user('pamousset01@gmail.com',
                                     '200795jtm1',
                                     '2020-01-12',
                                     True,
                                     13,
                                     '2021-02-21',
                                     '2021-02-20')

user_service.desactivate_user(user_1)

print(user_1.__str__())