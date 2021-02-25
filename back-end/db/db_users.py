from .db_utils import get, put

def db_create_user(public_id, username, password):
    put("INSERT INTO Users (Public_Id, Username, Password_Hash) VALUES (?, ?, ?)", [public_id, username, password])

def db_get_all_users():
    return get("SELECT * FROM Users")

def db_get_one_user(public_id):
    return get("SELECT * FROM Users WHERE Public_Id = (?)", [public_id])

def login(username, password):
    return get("SELECT * FROM Users WHERE Username = (?) and Password_String = (?)", [username, password])

def db_get_user_by_username(username):
    return get("SELECT * FROM Users WHERE Username = (?)", [username])