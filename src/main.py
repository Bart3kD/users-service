from flask import request, jsonify
from src.controllers import UserController
from src.repositories import UserRepository
from src.users import User
from flask import Flask, Response
from json import dumps

app = Flask(__name__)

user_repository = UserRepository()
user_controller = UserController(user_repository)


@app.get("/users")
def get_all_users():
    users = user_controller.get_all()
    if users:
        return Response(response=[user.as_dict for user in users], status=200, mimetype='application/json')
    else:
        return Response(response=dumps([]), status=200, mimetype='application/json')


@app.get("/users/<int:user_id>")
def get_user_by_id(user_id):
    user = user_controller.get_by_id(user_id)
    if user:
        return Response(response=user.as_dict, status=200,  mimetype='application/json')
    else:
        return Response(status=404)


@app.post("/users")
def create_user():
    user_data = request.json
    try:
        user = user_controller.create(user_data)
        return Response(status=201)
    except ValueError as e:
        return Response(str(e), status=400)


@app.patch("/users/<int:user_id>")
def update_user(user_id):
    user_data = request.json
    user = user_controller.update(user_id, user_data)
    try:
        if user:
            return Response(response=user.as_dict, status=200,  mimetype='application/json')
        else:
            return Response(status=400)
    except ValueError as e:
        return Response(str(e), status=400)


@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    success = user_controller.delete(user_id)
    if success:
        return Response(status=204)
    else:
        return Response(status=404)
