import sqlite3


def add_data():
    conn = sqlite3.connect("../db.sqlite", isolation_level=None)

    conn.cursor().execute(
        "INSERT INTO Users(Username, MonthlySalary)"
        "VALUES ('user1', 3000),"
        "('user2', 2000),"
        "('user3', 1000);"
    )

    rows = conn.cursor().execute(
        "SELECT *        "
        "  FROM Users    "
    ).fetchall()

    conn.close()

    print(rows)


