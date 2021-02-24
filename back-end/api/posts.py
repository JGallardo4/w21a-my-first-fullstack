from flask import jsonify, make_response, request, Blueprint

posts = Blueprint('posts', __name__)

from ..db.db_posts import getPost, getPosts, createPost, updatePost, deletePost

# import sys
# sys.path.insert(0, "../db")

# try:
#     from db import db_posts
# except ImportError:
#     print('No Import')

@posts.route("/posts", methods=["GET", "POST", "PATCH", "DELETE"])
def get_posts():    
    if(request.method == "GET"):
        if request.is_json:        
            _id = request.get_json()["post_id"]

            if(_id):
                response = getPost(_id)
                return make_response(response, 200)
            else:
                return make_response(jsonify({"message": "Request body must contain post_id data"}), 400)
        else:
            response = getPosts()
            return make_response(response, 200)
    
    if request.is_json:
        if(request.method == "POST"):
            _data = request.get_json()
            _user_id = _data["user_id"]
            _content = _data["content"]

            createPost(_user_id, _content)

            return make_response(jsonify({"message": "Success"}), 200)

        elif(request.method == "PATCH"):
            _data = request.get_json()
            _post_id = _data["post_id"]
            _new_content = _data["new_content"]

            updatePost(_post_id, _new_content)

            return make_response(jsonify({"message": "Success"}), 200)

        elif(request.method == "DELETE"):
            _data = request.get_json()
            _post_id = _data["post_id"]

            deletePost(_post_id)

            return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)