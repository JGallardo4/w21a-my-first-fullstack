import sys
from datetime import date

from flask import jsonify
from mariadb import connect

import dbcreds

connection = None
cursor = None

def db_connect():
    return connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )

def get(command, arguments=[]):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
        row_headers=[x[0] for x in cursor.description]
        row_values = cursor.fetchall()
        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers,result)))
        result = jsonify(json_data)
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()
        return result

def put(command, arguments=[]):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
        connection.commit()
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()

def getPosts():
    return get("SELECT * FROM Posts")

def getPost(_id):
    return get("SELECT * FROM Posts WHERE Id = (?)", [_id])  

def createPost(user, content):
    today = date.today().strftime("%Y/%m/%d")
    put("INSERT INTO Posts (User_Id, Content, Created_At) VALUES (?, ?, ?)", [user, content, today])

def login(username, password):
    return get("SELECT * FROM Users WHERE Username = ? and Password_String = ?", [username, password])

def createUser(username, password):
    put("INSERT INTO Users (Username, Password_String) VALUES (?, ?)", [username, password])
