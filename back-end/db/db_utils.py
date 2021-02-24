from flask import jsonify
from mariadb import connect

from .db_creds import user, password, host, port, database

connection = None
cursor = None

def db_connect():
    return connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
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