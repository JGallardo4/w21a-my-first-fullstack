from flask import jsonify, make_response, request, Blueprint

auth = Blueprint('auth', __name__)

import sys
sys.path.insert(0, "../db")
sys.path.insert(0, "../app")

try:
    from db import db_users
    from app import app
except ImportError:
    print('No Import')

@auth.route("/login", methods=["POST"])
def login():
    if request.is_json:
        if request.method == "POST":
            _data = request.get_json()
            _username = _data["username"]
            _password = _data["password"]

            db_response = db_users.login(_username, _password).get_json()

            if len(db_response) == 1:
                return make_response(jsonify({"message": "Success"}), 200)
            else:
                return make_response(jsonify({"message": "Incorrect username or password"}), 400)  