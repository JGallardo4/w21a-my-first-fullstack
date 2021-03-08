import datetime
import uuid

from flask import Blueprint, jsonify, make_response, request

from ..db.db_users import db_get_all_users, db_get_one_user, db_get_user_by_username, db_create_user
from ..security.sec_utils import (check_hash, generate_hash,
                                  generate_token, token_required)

users = Blueprint('/api/users', __name__)

@users.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        username = data["username"]
        password = generate_hash(data["password"].encode('utf8'))

        try:
            user_exists = db_get_user_by_username(username)
            if user_exists:                
                return make_response(jsonify({"message": "Username or password taken"}), 400)
        except:
            pass            
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    else:
        db_create_user(username, password)
        new_user = db_get_user_by_username(username)
        token = generate_token(new_user[0]["Id"])
        new_user[0].update({"loginToken": token})
        return make_response(jsonify(new_user), 201)

@users.route("/api/users", methods=["GET"])
def get_all_users():
    return make_response(jsonify(db_get_all_users()), 200)
    
@users.route("/api/users/<public_id>", methods=["GET"])
def get_one_user(current_user, public_id):
    user = db_get_one_user(public_id)

    if user:
        return make_response(jsonify(user), 200)
    else:
        return make_response(jsonify({"message": "User not found"}), 404)
