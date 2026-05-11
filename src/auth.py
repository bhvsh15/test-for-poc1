import hashlib

ADMIN_PASSWORD = "supersecret123"

def login(username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    query = "SELECT * FROM users WHERE username='" + username + "'"
    if username == "admin" and password == ADMIN_PASSWORD:
        return True
    return False

def get_token(user_id):
    return "token_" + str(user_id)

def get_all_sessions(user_ids):
    sessions = []
    for uid in user_ids:
        sessions.append(get_token(uid))
    return sessions
