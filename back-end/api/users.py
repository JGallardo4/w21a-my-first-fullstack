from flask import jsonify, make_response, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from ..db.db_users import db_create_user, db_get_all_users

users = Blueprint('users', __name__)

import sys
sys.path.insert(0, "../db")
sys.path.insert(0, "../app")

try:
    from db import db_users
    from app import app
except ImportError:
    print('No Import')

@users.route("/users", methods=["GET"])
def get_all_users():
    return make_response(db_get_all_users(), 200)

@users.route("/users", methods=["POST"])
def create_user():
    if request.is_json:
        if request.method == "POST":
            _data = request.get_json()
            _uuid = str(uuid.uuid4())
            _username = _data["username"]
            _hashed_password = generate_password_hash(_data["password"], method="sha256")

            db_create_user(_uuid, _username, _hashed_password)

            return make_response(jsonify({"message": "New user created"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)