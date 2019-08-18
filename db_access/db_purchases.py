import sqlite3

from db_access import util


def get_purchases_by_user_id(user_id):
    conn = sqlite3.connect("../db.sqlite")

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT *           "
        "  FROM Purchases   "
        " WHERE UserID=?    ", user_id,
    ).fetchall()

    conn.close()

    results = []

    for row in rows:
        results.append(util.map_row(cursor, row))

    return results


def add_purchase_to_user(user_id, purchase_cost):
    conn = sqlite3.connect("../db.sqlite")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Purchases(UserID, Cost)"
        "VALUES(?, ?)", (user_id, purchase_cost),
    )

    conn.close()
