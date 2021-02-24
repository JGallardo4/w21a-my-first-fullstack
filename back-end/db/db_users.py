from .db_utils import get, put

def createUser(username, password):
    put("INSERT INTO Users (Username, Password_String) VALUES (?, ?)", [username, password])

def login(username, password):
    return get("SELECT * FROM Users WHERE Username = (?) and Password_String = (?)", [username, password])