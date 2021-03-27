class User():
    def __init__(self, email, password, registration_date, active, sign_in_count, current_sign_in_on, last_sign_in_on):
        self.email = email
        self.password = password
        self.registration_date = registration_date
        self.active = active

        # Activity tracking
        self.confirmed = False
        self.sign_in_count = sign_in_count
        self.current_sign_in_on = current_sign_in_on
        self.last_sign_in_on = last_sign_in_on

    def __str__(self):
        user_attributes = vars(self)
        return (', '.join("%s: %s" % item for item in user_attributes.items()))
