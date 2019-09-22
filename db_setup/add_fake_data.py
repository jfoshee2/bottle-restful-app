from service import user_service


def add_data():
    user_service.create_user("user1", "somepassword", 3000)
    user_service.create_user("user2", "pass1234", 4000)
    user_service.create_user("user3", "pass5678", 5000)
