from flask import Blueprint, request, jsonify

auth_routes = Blueprint("auth", __name__)

users = []

@auth_routes.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.json
    users.append(data)
    return {"message": "User registered successfully"}, 201
