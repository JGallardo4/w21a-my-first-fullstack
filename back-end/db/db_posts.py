from .db_utils import get, put
from datetime import datetime

def getPosts():
    return get("SELECT * FROM Posts")

def getPost(_id):
    return get("SELECT * FROM Posts WHERE Id = (?)", [_id])  

def createPost(user, content):
    today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    put("INSERT INTO Posts (User_Id, Content, Created_At) VALUES (?, ?, ?)", [user, content, today])

def updatePost(post_id, new_content):
    today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    put("UPDATE Posts SET Content = (?), Created_At = (?) WHERE Id = (?)", [new_content, today, post_id])

def deletePost(post_id):
    put("DELETE FROM Posts WHERE Id = (?)", [post_id])