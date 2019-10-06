import bcrypt
import jwt

from db_access import db_users

s = bcrypt.gensalt()  # global variable to store password hashes


def create_user(user_name, password, monthly_salary):
    return jwt.encode(
        db_users.create_user(user_name, str(bcrypt.hashpw(password, s)), monthly_salary),
        'secret',
        algorithm='HS256'
    )


def login_user(user_name, password):
    return jwt.encode(
        db_users.login_user(user_name, str(bcrypt.hashpw(password, s))),
        'secret',
        algorithm='HS256'
    )
