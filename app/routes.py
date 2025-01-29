from flask import Blueprint, render_template
from app.Controllers import (
    UserController,
)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/users", methods=["GET"])
def user():
    return UserController.index()


@main.route("/user/create", methods=["GET", "POST"])
def user_create():
    return UserController.create()


@main.route("/user/edit/<int:id>", methods=["GET", "POST"])
def user_edit(id: int):
    return UserController.edit(id)


@main.route("/user/destroy/<int:id>", methods=["GET", "POST"])
def user_destroy(id: int):
    return UserController.destroy(id)
