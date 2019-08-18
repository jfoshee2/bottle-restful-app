import sqlite3

from db_access import util


def get_all_users():
    conn = sqlite3.connect("../db.sqlite")

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT *        "
        "  FROM Users    "
    ).fetchall()

    conn.close()

    results = []

    for row in rows:
        results.append(util.map_row(cursor, row))

    return results


def create_user(username, monthly_salary):
    conn = sqlite3.connect("../db.sqlite", isolation_level=None)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO USERS(Username, MonthlySalary)"
        "VALUES(?, ?)", (username, monthly_salary),
    )

    conn.close()
