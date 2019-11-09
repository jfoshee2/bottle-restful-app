from db_access import util


def get_all_users():

    return util.get_query_result_list(
        "SELECT *        "
        "  FROM Users    "
    )


def create_user(username, pw_hash, monthly_salary):

    last_id = util.insert_row(
        "INSERT INTO USERS(Username, PWHash, MonthlySalary)"
        "VALUES(?, ?, ?)", username, pw_hash, monthly_salary,
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


def login_user(user_name, pw_hash):
    return util.get_query_single_row(
        "SELECT *               "
        "  FROM Users           "
        " WHERE Username=?      "
        "   AND PWHash=?        ", user_name, pw_hash
    )


def update_salary(user_id, salary):
    util.update_row(
        "UPDATE Users           "
        "   SET MonthlySalary=? "
        " WHERE ID=?            ", salary, user_id
    )
