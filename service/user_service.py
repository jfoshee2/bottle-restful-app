import bcrypt

from db_access import db_users

s = bcrypt.gensalt()  # global variable to store password hashes


def create_user(user_name, password, monthly_salary):
    return db_users.create_user(user_name, bcrypt.hashpw(password, s), monthly_salary)


def login_user(user_name, password):
    return db_users.login_user(user_name, bcrypt.hashpw(password, s))
