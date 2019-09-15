from db_access import util


def get_purchases_by_user_id(user_id):

    return util.get_query_result_list(
        "SELECT *           "
        "  FROM Purchases   "
        " WHERE UserID=?    ", user_id,
    )


def add_purchase_to_user(user_id, purchase_cost):

    last_id = util.insert_row(
        "INSERT INTO Purchases(UserID, PurchaseDate, Cost)"
        "VALUES(?, CURRENT_TIMESTAMP, ?)", user_id, purchase_cost,
    )

    return util.get_query_single_row(
        "SELECT *                           "
        "  FROM Purchases                   "
        " WHERE ID=?                        ", last_id,
    )


def get_amount_spent_for_current_month(user_id):

    return util.get_query_single_result(
        "SELECT SUM(Cost) AS sum                                           "
        "  FROM Purchases                                                  "
        " WHERE UserID=?                                                   "
        "   AND PurchaseDate < DATE('now', 'start of month', '+1 month')   "
        "   AND PurchaseDate > DATE('now', 'start of month', '-1 day')     ", user_id,
    )


def get_month_purchases(user_id, month, year):

    return util.get_query_result_list(
        "SELECT *                                        "
        "  FROM Purchases                                "
        " WHERE UserID=?                                 "
        "   AND STRFTIME('%m', PurchaseDate)=?           "
        "   AND STRFTIME('%Y', PurchaseDate)=?           ", user_id, month, year,
    )


def get_month_purchases_cost(user_id, month, year):

    return util.get_query_single_result(
        "SELECT SUM(Cost) AS sum                         "
        "  FROM Purchases                                "
        " WHERE UserID=?                                 "
        "   AND STRFTIME('%m', PurchaseDate)=?           "
        "   AND STRFTIME('%Y', PurchaseDate)=?           ", user_id, month, year,
    )
