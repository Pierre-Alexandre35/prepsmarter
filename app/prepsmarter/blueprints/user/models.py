import datetime
from hashers import get_hashed_password

class User():
    def __init__(self, email, password, registration_date, active, sign_in_count, current_sign_in_on, current_sign_in_ip, last_sign_in_on, last_sign_in_ip):
        self.email = email
        self.password = password
        self.registration_date = registration_date
        self.active = active

        # Activity tracking
        self.sign_in_count = sign_in_count
        self.current_sign_in_on = current_sign_in_on
        self.current_sign_in_ip = current_sign_in_ip
        self.last_sign_in_on = last_sign_in_on
        self.last_sign_in_ip = last_sign_in_ip

    def desactivate_user(self):
        if self.active == False:
            print(f"User {self.email} is already inactive")
        self.active = False

    def reactive_user(self):
        if self.active == True:
            print(f"User {self.email} is already active")
        self.active = True

    def is_active(self):
        return self.active

    def update_activity_tracking(self, ip_address):
        self.sign_in_count += 1
        self.last_sign_in_on = self.current_sign_in_on
        self.last_sign_in_ip = self.current_sign_in_ip
        self.current_sign_in_on = datetime.datetime.now()
        self.current_sign_in_ip = ip_address


    def update_password(self, new_password):
        self.password = get_hashed_password(new_password)

    def __str__(self):
        user_attributes = vars(self)
        return (', '.join("%s: %s" % item for item in user_attributes.items()))
    
    def save(self):
        # commit query should be in another class
        return True

pierre = User('pamousset', 
              'Bonjour', 
              '2021-02-13', 
              False,
              3,
              '2022-10-10',
              '192.1.1',
              '2010-12-10',
              '192.1.1')

print('azerty'.encode('utf-8'))

pierre.update_password('azerty'.encode('utf-8'))
print(pierre.password)

