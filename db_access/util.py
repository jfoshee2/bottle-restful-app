import sqlite3


def map_row(cursor, row):
    columns = [d[0].lower() for d in cursor.description]
    return dict(zip(columns, row))


def get_connection(*level):
    """
    This utility function is used for connecting to the database and so that when the time comes
    to upgrade to postgres, mysql, etc. only minor changes should be made.

    :param level: optional isolation level for sqlite so that the database changes are temporarily saved
    when the server is deployed

    :return: connection to database
    """
    if level:
        return sqlite3.connect("../db.sqlite", isolation_level=level[0])
    else:
        return sqlite3.connect("../db.sqlite")
