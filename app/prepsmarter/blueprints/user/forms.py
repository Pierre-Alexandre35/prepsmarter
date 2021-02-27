class RegisterForm():
    def __init__(self, form_data):
        self.email = form_data.get("email")
        self.password = form_data.get("psw")
        self.password_two = form_data.get("psw-repeat-two")
        print(form_data)
        
    def is_new_user():
        #if self.email already in the database.users then return False
        return True 
    
    def both_password_match():
        if password != password_two:
            return False 
        return True
        
    def is_password_strong_enough():
        if len(self.password) < 8:
            return False
        elif re.search('[0-9]',self.password) is None:
            return False
        elif re.search('[A-Z]',self.password) is None: 
            return False
        return True
                   
    def validate_new_user():
        if self.is_new_user and self.both_password_match and self.is_password_strong_enough:
            ## register new user 
        

    
    
# password equality 
# email not already used 
#password strong enough