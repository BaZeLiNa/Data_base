from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import user_controller
from my_project.auth.domain.orders.user import Users

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.get('')
def get_all_users() -> Response:
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)


@user_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = Users.create_from_dto(content)
    user_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)


@user_bp.get('/transactions/<int:user_id>')
def get_user_transactions(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_users_with_transactions(user_id)), HTTPStatus.OK)


@user_bp.get('/blocked-funds/<int:user_id>')
def get_user_blocked_funds(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_users_with_blocked_funds(user_id)), HTTPStatus.OK)


@user_bp.get('/reviews/<int:user_id>')
def get_user_reviews(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_users_with_reviews(user_id)), HTTPStatus.OK)


@user_bp.get('/reservations/<int:user_id>')
def get_user_reservations(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_users_with_reservations(user_id)), HTTPStatus.OK)


@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = Users.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
