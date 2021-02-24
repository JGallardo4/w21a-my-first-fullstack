from flask import jsonify, make_response, request, Blueprint

posts = Blueprint('posts', __name__)

from ..db.db_posts import getPost, getPosts, createPost, updatePost, deletePost

@posts.route("/posts", methods=["GET"])
def get_all_posts():
    if not request.is_json:
        response = getPosts()
        return make_response(response, 200)
        
@posts.route("/posts/<post_id>", methods=["GET"])
def get_one_post():
    if request.is_json:        
        _id = request.get_json()["post_id"]

        if(_id):
            response = getPost(_id)
            return make_response(response, 200)
        else:
            return make_response(jsonify({"message": "Request body must contain post_id data"}), 400)

@posts.route("/posts", methods=["POST"])
def create_post():    
    if request.is_json:
        if(request.method == "POST"):
            _data = request.get_json()
            _user_id = _data["user_id"]
            _content = _data["content"]

            createPost(_user_id, _content)

            return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@posts.route("/posts", methods=["PATCH"])
def update_post():
    if request.is_json:
        _data = request.get_json()
        _post_id = _data["post_id"]
        _new_content = _data["new_content"]

        updatePost(_post_id, _new_content)

        return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@posts.route("/posts/<post_id>", methods=["DELETE"])
def delete_post():
    if request.is_json:        
        _data = request.get_json()
        _post_id = _data["post_id"]

        deletePost(_post_id)

        return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)