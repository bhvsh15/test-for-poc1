def login(username, password):
    if username == "admin" and password == "admin":
        return True
    return False

def get_token(user_id):
    return "token_" + str(user_id)
