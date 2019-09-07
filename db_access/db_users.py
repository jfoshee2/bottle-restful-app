from db_access import util


def get_all_users():
    conn = util.get_connection()

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
    conn = util.get_connection(None)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO USERS(Username, MonthlySalary)"
        "VALUES(?, ?)", (username, monthly_salary),
    )

    conn.close()


def get_user_monthly_salary(user_id):
    conn = util.get_connection()

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT MonthlySalary   "
        "  FROM Users           "
        " WHERE ID=?            ", user_id,
    ).fetchall()

    return rows[0][0]
