from .db_utils import get, put

def db_create_user(uuid, username, password):
    put("INSERT INTO Users (Uuid, Username, Password_Hash) VALUES (?, ?, ?)", [uuid, username, password])

def db_get_all_users():
    return get("SELECT Username FROM Users")

def login(username, password):
    return get("SELECT * FROM Users WHERE Username = (?) and Password_String = (?)", [username, password])