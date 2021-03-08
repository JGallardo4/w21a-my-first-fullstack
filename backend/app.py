import json

import mariadb
from flask import Flask, Response, g, jsonify, make_response, request, session
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from .api.routes.login import login
from .api.routes.posts import posts
from .api.routes.users import users
from .config_secrets import secrets

app = Flask(__name__)

app.secret_key = secrets["secret_key"]

app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(posts)
app.register_blueprint(users)
app.register_blueprint(login)


flask_bcrypt = Bcrypt(app)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
