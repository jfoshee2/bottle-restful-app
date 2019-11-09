from json import dumps, loads

from bottle import route, run, template, get, request, post, response, put
from os import environ

from db_setup import create_tables, add_fake_data, drop_tables
from db_access import db_users, db_purchases
from service import user_service, purchase_service


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


@put('/api/salary')
def update_salary():
    response.content_type = 'application/json'
    request_body = loads(request.body.read())
    user_service.update_salary(request.headers['Authorization'], request_body['salary'])


@get('/api/purchases')
def get_user_purchases():
    response.content_type = 'application/json'
    return dumps(purchase_service.get_user_purchases(request.headers['Authorization']))


@post('/api/purchases')
def add_user_purchase():
    response.content_type = 'application/json'
    request_body = loads(request.body.read())
    return dumps(purchase_service.add_purchase_to_user(request.headers['Authorization'], int(request_body['cost'])))


@get('/api/budget')
def get_savings_by_month():
    response.content_type = 'application/json'
    return dumps(
        purchase_service.get_budget(request.headers['Authorization'], request.query['month'], request.query['year'])
    )


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
