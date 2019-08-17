

def map_row(cursor, row):
    columns = [d[0].lower() for d in cursor.description]
    return dict(zip(columns, row))
