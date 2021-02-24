import json

import mariadb
from flask import Flask, Response, g, jsonify, make_response, request, session
from flask_cors import CORS

from .api.posts import posts
from .api.users import users

app = Flask(__name__)

CORS(app)

app.register_blueprint(posts)
app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True)