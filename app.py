from json import dumps, loads

from bottle import route, run, template, get, request, post, response
from os import environ

from db_setup import create_tables, add_fake_data, drop_tables
from db_access import db_users, db_purchases


@get('/api/users')
def get_users():
    response.content_type = 'application/json'
    return dumps(db_users.get_all_users())


@post('/api/users')
def add_user():
    request_body = loads(request.body.read())
    db_users.create_user(request_body['username'], int(request_body['salary']))


@get('api/<user_id>/purchases')
def get_user_purchases(user_id):
    response.content_type = 'application/json'
    return dumps(db_purchases.get_purchases_by_user_id(user_id))


@post('api/purchases/<user_id>')
def add_user_purchase(user_id):
    request_body = loads(request.body.read())
    db_purchases.add_purchase_to_user(user_id, int(request_body['cost']))


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
