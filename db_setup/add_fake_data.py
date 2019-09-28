from service import user_service


def add_data():
    user_service.create_user("user1", "somepassword".encode('utf-8'), 3000)
    user_service.create_user("user2", "pass1234".encode('utf-8'), 4000)
    user_service.create_user("user3", "pass5678".encode('utf-8'), 5000)
