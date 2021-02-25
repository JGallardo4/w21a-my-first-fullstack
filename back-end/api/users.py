import datetime
import uuid

import jwt
from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import check_password_hash, generate_password_hash

from ..db.db_creds import secrets
from ..db.db_users import (db_create_user, db_get_all_users, db_get_one_user,
                           db_get_user_by_username)

users = Blueprint('users', __name__)

import sys

sys.path.insert(0, "../db")
sys.path.insert(0, "../app")

try:
    from app import app
    from db import db_users
except ImportError:
    print('No Import')

@users.route("/users", methods=["GET"])
def get_all_users():
    return make_response(jsonify(db_get_all_users()), 200)
    
@users.route("/users/<public_id>", methods=["GET"])
def get_one_user(public_id):
    user = db_get_one_user(public_id)

    if user:
        return make_response(jsonify(user), 200)
    else:
        return make_response(jsonify({"message": "User not found"}), 404)

@users.route("/users", methods=["POST"])
def create_user():
    if request.is_json:
        if request.method == "POST":
            _data = request.get_json()
            _public_id = str(uuid.uuid4())
            _username = _data["username"]
            _password = str(_data["password"])
            _hashed_password = generate_password_hash(_password, method="sha256")

            db_create_user(_public_id, _username, _hashed_password)

            return make_response(jsonify({"message": "New user created"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@users.route("/users/login")
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required'"})
    
    user = db_get_user_by_username(auth.username)
    
    if not user:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required'"})    

    if check_password_hash(user[0]["password_hash"], auth.password):
        token = jwt.encode({"public_id" : user[0]["public_id"], "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, secrets["secret_key"], algorithm="HS256")

        # decoded_token = jwt.decode(token, secrets["secret_key"], algorithms=["HS256"])

        return make_response(jsonify({"token" : token}))
    
    return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required'"})
