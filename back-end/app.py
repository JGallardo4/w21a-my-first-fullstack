from flask import Flask, request, Response, jsonify, make_response
import json
import mariadb
import db

app = Flask(__name__)

@app.route("/posts", methods=["GET", "POST", "PATCH", "DELETE"])
def get_posts(): 
    if(request.method == "GET"):
        if request.is_json:
            _id = request.get_json()["post_id"]

            if(_id):
                response = db.getPost(_id)
                return make_response(response, 200)
            else:
                return make_response(jsonify({"message": "Request body must contain post_id data"}), 400)
        else:
            response = db.getPosts()
            return make_response(response, 200)

    elif(request.method == "POST"):
        if request.is_json:
            _data = request.get_json()
            _user_id = _data["user_id"]
            _content = _data["content"]

            db.createPost(_user_id, _content)

            return make_response(jsonify({"message": "Success"}), 200)
        else:
            return make_response(jsonify({"message": "Request body must be JSON"}), 400)

    elif(request.method == "PATCH"):
        _id = request.form["id"]
        _common_name = request.form["common_name"]
        _scientific_name = request.form["scientific_name"  ]     

        db.update_animal(_id, _common_name, _scientific_name)

        return Response(
            "Animal updated",
            mimetype = "text/plain",
            status = 200
        )

    elif(request.method == "DELETE"):
        _id = request.form["id"]
        db.delete_animal(_id)

        return Response(
            "Animal deleted",
            mimetype = "text/plain",
            status = 200
        )