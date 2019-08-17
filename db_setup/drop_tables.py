import sqlite3


def drop_users():
    conn = sqlite3.connect("../db.sqlite", isolation_level=None)
    conn.cursor().execute("DROP TABLE Users")
    conn.close()


def drop_purchases():
    conn = sqlite3.connect("../db.sqlite", isolation_level=None)
    conn.cursor().execute("DROP TABLE Purchases")
    conn.close()


drop_users()
drop_purchases()
