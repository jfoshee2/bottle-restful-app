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
    conn = sqlite3.connect("../db.sqlite", isolation_level=None)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Purchases(UserID, PurchaseDate, Cost)"
        "VALUES(?, CURRENT_TIMESTAMP, ?)", (user_id, purchase_cost),
    )

    conn.close()


def get_amount_spent_for_current_month(user_id):
    conn = sqlite3.connect("../db.sqlite")

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT SUM(Cost) AS sum                                           "
        "  FROM Purchases                                                  "
        " WHERE UserID=?                                                   "
        "   AND PurchaseDate < DATE('now', 'start of month', '+1 month')   "
        "   AND PurchaseDate > DATE('now', 'start of month', '-1 day')     ", user_id,
    ).fetchall()

    return rows[0][0]
