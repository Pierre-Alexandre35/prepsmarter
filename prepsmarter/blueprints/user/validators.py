import re 
from email_validator import validate_email, EmailNotValidError
from prepsmarter.extensions import conn

def is_strong_password(password: str) -> bool:
    is_long = len(password) >= 8
    has_digits = bool(re.search(r"\d", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    return is_long and has_digits and has_upper
    
def is_email_formated_correctly(email: str) -> bool:
    is_correct = True
    try:
        validate_email(email)
    except EmailNotValidError:
        is_correct = False
    return is_correct

def password_matching(pwd_1: str, pwd_2: str) -> bool:
    return pwd_1 == pwd_2

    
def email_already_in_use(email: str) -> bool:
    sql = "SELECT CASE WHEN EXISTS ( SELECT * FROM users WHERE email = (%s)) THEN 1 ELSE 0 END;"
    cursor = conn.cursor()
    cursor.execute(sql, (email))
    res = cursor.fetchall()
    return res == 1 

    
    
    
