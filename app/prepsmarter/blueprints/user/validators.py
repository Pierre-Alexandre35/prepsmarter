import re 
from email_validator import validate_email, EmailNotValidError
from prepsmarter.extensions import conn

def is_strong_password(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None

    return {
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error': uppercase_error
    }
    
def is_email_formated_correctly(email):
    is_correct = True
    try:
        validate_email(email)
    except EmailNotValidError:
        is_correct = False
    return {
        'email_error' : is_correct
    }

def password_matching(pwd_1, pwd_2):
    password_matching = pwd_1 == pwd_2
    return {
        'password_matching' : password_matching
    }
    
def email_already_in_use(email):
    sql = "SELECT * FROM users WHERE email = (%s)"
    cursor = conn.cursor()
    cursor.execute(sql, (email))
    res = cursor.fetchall()
    return {
        res
    }

    
    
    
print(email_already_in_use('dddf'))