from flask import Blueprint, jsonify, make_response, request
from flask_bcrypt import check_password_hash, generate_password_hash

from ..db import db_sessions
from ..db.db_users import db_create_user, db_get_user_by_username
from ..security.sec_utils import (check_hash, generate_hash,
                                  generate_token, token_required)

login = Blueprint('/api/login', __name__)

@login.route("/api/login", methods=["POST"])
def log_user_in():
    try:
        data = request.get_json()
        username = data["username"]
        password_claim = data["password"].encode('utf8')       

        user = db_get_user_by_username(username)
        stored_password = get_user_password(user[0]["userId"])

        if check_hash(password_claim, stored_password):
            db_sessions.log_user_in(user[0]["userId"])
            token = generate_token(user[0]["userId"])
            user[0].update({"loginToken": token})
            return make_response(jsonify(user), 201)
        else:
            return make_response(jsonify({"message": "Incorrect username or password"}), 400)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    
@login.route("/logout", methods=["DELETE"])
def log_user_out(session_id):
    db_sessions.db_delete_session(session_id)

    return make_response(jsonify({"message": "Logged out"}), 200)
