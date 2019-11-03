import jwt

from db_access import db_purchases


def get_user_purchases(token):
    user = jwt.decode(token.split(' ')[1], 'secret', algorithm='HS256')
    return db_purchases.get_purchases_by_user_id(user['id'])


def add_purchase_to_user(token, purchase_cost):
    user = jwt.decode(token.split(' ')[1], 'secret', algorithm='HS256')
    return db_purchases.add_purchase_to_user(user['id'], purchase_cost)


def get_budget(token, month, year):
    user = jwt.decode(token.split(' ')[1], 'secret', algorithm='HS256')
    purchases = db_purchases.get_month_purchases(user['id'], month, year)
    total = db_purchases.get_month_purchases_cost(user['id'], month, year)
    return {'purchases': purchases, 'sum': total}
