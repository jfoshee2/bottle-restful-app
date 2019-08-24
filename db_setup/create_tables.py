import sqlite3


def create():
    conn = sqlite3.connect("../db.sqlite", isolation_level=None)

    conn.cursor().execute(
        "CREATE TABLE IF NOT EXISTS Users("
        "   ID INTEGER PRIMARY KEY AUTOINCREMENT,"
        "   Username varchar(255),"
        "   MonthlySalary int"
        ");"
    )

    conn.cursor().execute(
        "CREATE TABLE IF NOT EXISTS Purchases("
        "   ID INTEGER PRIMARY KEY AUTOINCREMENT,"
        "   UserID int,"
        "   PurchaseDate Date,"
        "   Cost int"
        ");"
    )

    conn.close()


create()

