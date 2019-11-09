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


def get_query_result_list(query, *args):
    """
    This utility function is used for getting the result list from a SQL query.

    :param query: SQL query to be executed

    :param args: optional arguments that are used to filter the results

    :return: resulting list from SQL query
    """
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute(query, args).fetchall()
    results = []
    for row in rows:
        results.append(map_row(cursor, row))

    cursor.close()
    conn.close()

    return results


def get_query_single_row(query, *args):
    """
    This utility function is used for getting a single row from an SQL query

    :param query: SQL query to be executed

    :param args: optional arguments to filter the result row

    :return: single result row
    """
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute(query, args).fetchall()

    result = map_row(cursor, rows[0])

    cursor.close()
    conn.close()

    return result


def get_query_single_result(query, *args):
    """
    This utility function is used to get a single result from a SQL query.

    :param query: SQL query to be executed

    :param args: optional arguments that are used to filter the single result

    :return: result from SQL query
    """
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute(query, args).fetchall()

    cursor.close()
    conn.close()

    return rows[0][0]


def insert_row(insert_statement, *args):
    """
    This utility function is used to insert a row into the database.

    :param insert_statement: SQL statement to be executed

    :param args: arguments that are to be passed into SQL statement
    """
    conn = get_connection(None)
    cursor = conn.cursor()

    cursor.execute(insert_statement, args)

    last_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return last_id


def update_row(update_statement, *args):
    """
    This utility function is used to update a row in the database.

    :param update_statement: SQL statement to be executed.

    :param args: arguments that are to be passed into SQL statement

    :return:
    """
    conn = get_connection(None)
    cursor = conn.cursor()

    cursor.execute(update_statement,args)

    cursor.close()
    conn.close()
