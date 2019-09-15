from db_access import util


def get_all_users():

    return util.get_query_result_list(
        "SELECT *        "
        "  FROM Users    "
    )


def create_user(username, monthly_salary):

    last_id = util.insert_row(
        "INSERT INTO USERS(Username, MonthlySalary)"
        "VALUES(?, ?)", username, monthly_salary,
    )

    return util.get_query_single_row(
        "SELECT *                    "
        "  FROM USERS                "
        " WHERE ID=?                 ", last_id,
    )


def get_user_monthly_salary(user_id):

    return util.get_query_single_result(
        "SELECT MonthlySalary   "
        "  FROM Users           "
        " WHERE ID=?            ", user_id,
    )
