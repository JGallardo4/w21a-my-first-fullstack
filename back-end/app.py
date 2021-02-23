import json

import mariadb
from flask import Flask, Response, g, jsonify, make_response, request, session
from flask_cors import CORS

import db

app = Flask(__name__)

CORS(app)


@app.before_request
def before_request():
    g.username = None
    if "username" in session:
        g.username = session["username"]


@app.route("/posts", methods=["GET", "POST", "PATCH", "DELETE"])
def get_posts():    
    if(request.method == "GET"):
        if request.is_json:        
            _id = request.get_json()["post_id"]

            if(_id):
                response = db.getPost(_id)
                return make_response(response, 200)
            else:
                return make_response(jsonify({"message": "Request body must contain post_id data"}), 400)
        else:
            response = db.getPosts()
            return make_response(response, 200)
    
    if request.is_json:
        if(request.method == "POST"):
            _data = request.get_json()
            _user_id = _data["user_id"]
            _content = _data["content"]

            db.createPost(_user_id, _content)

            return make_response(jsonify({"message": "Success"}), 200)

        elif(request.method == "PATCH"):
            _data = request.get_json()
            _post_id = _data["post_id"]
            _new_content = _data["new_content"]

            db.updatePost(_post_id, _new_content)

            return make_response(jsonify({"message": "Success"}), 200)

        elif(request.method == "DELETE"):
            _data = request.get_json()
            _post_id = _data["post_id"]

            db.deletePost(_post_id)

            return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)


@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        if request.method == "POST":
            _data = request.get_json()
            _username = _data["username"]
            _password = _data["password"]

            db_response = db.login(_username, _password).get_json()

            if len(db_response) == 1:
                return make_response(jsonify({"message": "Success"}), 200)
            else:
                return make_response(jsonify({"message": "Incorrect username or password"}), 400)  