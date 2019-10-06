from json import dumps, loads

from bottle import route, run, template, get, request, post, response
from os import environ

from db_setup import create_tables, add_fake_data, drop_tables
from db_access import db_users, db_purchases
from service import user_service


@get('/api/users')
def get_users():
    response.content_type = 'application/json'
    return dumps(db_users.get_all_users())


@post('/api/users')
def add_user():
    response.content_type = 'application/json'
    request_body = loads(request.body.read())
    response.set_header(
        'Authorization',
        'Bearer ' + user_service.create_user(
            request_body['username'],
            str(request_body['pw']).encode('utf-8'),
            int(request_body['salary'])
        ).decode()
    )


@get('/api/purchases/<user_id>')
def get_user_purchases(user_id):
    response.content_type = 'application/json'
    return dumps(db_purchases.get_purchases_by_user_id(user_id))


@post('/api/purchases/<user_id>')
def add_user_purchase(user_id):
    response.content_type = 'application/json'
    request_body = loads(request.body.read())
    return dumps(db_purchases.add_purchase_to_user(user_id, int(request_body['cost'])))


@get('/api/remaining/<user_id>')
def get_remaining_salary(user_id):
    response.content_type = 'application/json'
    amount_spent = db_purchases.get_amount_spent_for_current_month(user_id)
    monthly_salary = db_users.get_user_monthly_salary(user_id)
    remaining = int(monthly_salary) - int(amount_spent)
    return dumps({'remaining': remaining})


@get('/api/budget/<user_id>')
def get_savings_by_month(user_id):
    response.content_type = 'application/json'
    month_purchases = db_purchases.get_month_purchases(user_id, request.query['month'], request.query['year'])
    month_cost = db_purchases.get_month_purchases_cost(user_id, request.query['month'], request.query['year'])
    return dumps({'purchases': month_purchases, 'sum': month_cost})


@post('/api/login')
def login():
    request_body = loads(request.body.read())
    try:
        response.set_header(
            'Authorization',
            'Bearer ' + user_service.login_user(
                request_body['username'],
                str(request_body['pw']).encode('utf-8')
            ).decode()
        )
    except IndexError:
        response.status = 401


@route('/')
def main():
    return template('index.html')


# drop_tables.drop_users()
# drop_tables.drop_purchases()
create_tables.create()
add_fake_data.add_data()
if environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
