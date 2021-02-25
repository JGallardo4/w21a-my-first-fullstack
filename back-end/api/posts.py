from flask import jsonify, make_response, request, Blueprint

posts = Blueprint('posts', __name__)

from ..db.db_posts import db_get_one_post, db_get_all_posts, db_create_post, db_update_post, db_delete_post

@posts.route("/posts", methods=["GET"])
def get_all_posts():        
    return make_response(jsonify(db_get_all_posts()), 200)
        
@posts.route("/posts/<post_id>", methods=["GET"])
def get_one_post(post_id):
    return make_response(jsonify(db_get_one_post(post_id)), 200)

@posts.route("/posts", methods=["POST"])
def create_post():    
    if request.is_json:
        if(request.method == "POST"):
            _data = request.get_json()
            _user_id = _data["user_id"]
            _content = _data["content"]

            db_create_post(_user_id, _content)

            return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@posts.route("/posts", methods=["PATCH"])
def update_post():
    if request.is_json:
        _data = request.get_json()
        _post_id = _data["post_id"]
        _new_content = _data["new_content"]

        db_update_post(_post_id, _new_content)

        return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@posts.route("/posts/<post_id>", methods=["DELETE"])
def delete_post(post_id):
        db_delete_post(post_id)

        return make_response(jsonify({"message": "Success"}), 200)