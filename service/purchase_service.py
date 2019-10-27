import jwt

from db_access import db_purchases


def get_user_purchases(token):
    user = jwt.decode(token.split(' ')[1], 'secret', algorithm='HS256')
    return db_purchases.get_purchases_by_user_id(user['id'])


def add_purchase_to_user(token, purchase_cost):
    user = jwt.decode(token.split(' ')[1], 'secret', algorithm='HS256')
    return db_purchases.add_purchase_to_user(user['id'], purchase_cost)
