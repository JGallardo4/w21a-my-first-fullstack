import json

import mariadb
from flask import Flask, Response, jsonify, make_response, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

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

    elif(request.method == "POST"):
        if request.is_json:
            _data = request.get_json()
            _user_id = _data["user_id"]
            _content = _data["content"]

            db.createPost(_user_id, _content)

            return make_response(jsonify({"message": "Success"}), 200)
        else:
            return make_response(jsonify({"message": "Request body must be JSON"}), 400)

    elif(request.method == "PATCH"):
        if request.is_json:
            _data = request.get_json()
            _post_id = _data["post_id"]
            _new_content = _data["new_content"]

            db.updatePost(_post_id, _new_content)

            return make_response(jsonify({"message": "Success"}), 200)
        else:
            return make_response(jsonify({"message": "Request body must be JSON"}), 400)

    elif(request.method == "DELETE"):
        if request.is_json:
            _data = request.get_json()
            _post_id = _data["post_id"]

            db.deletePost(_post_id)

            return make_response(jsonify({"message": "Success"}), 200)
        else:
            return make_response(jsonify({"message": "Request body must be JSON"}), 400)
