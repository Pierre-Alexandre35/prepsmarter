from prepsmarter.blueprints.user.validators import email_already_in_use, password_matching

class RegistrationForm():
    def __init__(self, email, pwd_1, pwd_2):
        self.email = email
        self.pwd_1 = pwd_1
        self.pwd_2 = pwd_2

    def validate_registration(self):
        is_valid = email_already_in_use(self.email) and is_strong_password(self.pwd_1) and password_matching(self.pwd_1, self.pwd_2)
        return is_valid
        
        