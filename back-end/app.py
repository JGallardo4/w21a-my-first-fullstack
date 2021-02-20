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

            response = db.getPost(_id)

            return make_response(response, 200)
        else:
            return make_response(jsonify({"message": "Request body must be JSON"}), 400)
    # req = request.get_json()

    # response_body = {
    #     "message": "JSON received!",
    #     "sender": req.get("name")
    # }

    # result = make_response(jsonify(response_body), 200)

    # if(request.method == "GET"):   
    #     if request.is_json:
    #         if(request.form):
    #             try:
    #                 _id = request.form["id"]
    #                 if _id:
    #                     return Response(
    #                         json.dumps(db.post(_id), default=str),
    #                         mimetype="application/json",
    #                         status = 200
    #                     )                
    #             except Exception as e:
    #                 print(e)
    #                 return Response (
    #                     "Bad Request",
    #                     mimetype="text/plain",
    #                     status = 400
    #                 )
    #         elif(db.get_animals()):
    #             return Response (
    #                 json.dumps(db.get_animals(), default=str),
    #                 mimetype="application/json",
    #                 status = 200
    #             )
    #         else:
    #             return Response (
    #                 "No content",
    #                 mimetype="text/plain",
    #                 status = 404
    #             )
    #     else:
    #         return make_response(jsonify({"message": "Request body must be JSON"}), 400)

    elif(request.method == "POST"):
        _common_name = request.form["common_name"]
        _scientific_name = request.form["scientific_name"]

        db.create_animal(_common_name, _scientific_name)

        return Response(
            "New animal added",
            mimetype = "text/plain",
            status = 200
        )

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