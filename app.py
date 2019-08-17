from json import dumps

from bottle import route, run, template, get, request, post, response
from os import environ

from db_setup import create_tables, add_fake_data, drop_tables
from db_access import db_users


@get('/api/users')
def get_users():
    response.content_type = 'application/json'
    return dumps(db_users.get_all_users())


@post('/api/users')
def add_user():
    username = request.forms.get('username')
    monthly_salary = request.forms.get('salary')
    db_users.create_user(username, monthly_salary)


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
