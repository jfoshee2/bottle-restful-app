from db_access import util


def get_all_users():
    conn = util.get_connection()

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT *        "
        "  FROM Users    "
    ).fetchall()

    results = []

    for row in rows:
        results.append(util.map_row(cursor, row))

    cursor.close()
    conn.close()

    return results


def create_user(username, monthly_salary):
    conn = util.get_connection(None)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO USERS(Username, MonthlySalary)"
        "VALUES(?, ?)", (username, monthly_salary),
    )

    rows = cursor.execute(
        "SELECT * "
        "FROM USERS "
        "WHERE id = ?", (cursor.lastrowid,)
    ).fetchall()

    result = util.map_row(cursor, rows[0])

    cursor.close()
    conn.close()

    return result


def get_user_monthly_salary(user_id):
    conn = util.get_connection()

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT MonthlySalary   "
        "  FROM Users           "
        " WHERE ID=?            ", user_id,
    ).fetchall()

    cursor.close()
    conn.close()

    return rows[0][0]
