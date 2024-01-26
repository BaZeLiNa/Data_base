from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import room_controller
from my_project.auth.domain.orders.room import Rooms

room_bp = Blueprint('rooms', __name__, url_prefix='/rooms')


@room_bp.get('')
def get_all_rooms() -> Response:
    return make_response(jsonify(room_controller.find_all()), HTTPStatus.OK)


@room_bp.post('')
def create_room() -> Response:
    content = request.get_json()
    room = Rooms.create_from_dto(content)
    room_controller.create(room)
    return make_response(jsonify(room.put_into_dto()), HTTPStatus.CREATED)


@room_bp.get('/<int:room_id>')
def get_room(room_id: int) -> Response:
    return make_response(jsonify(room_controller.find_by_id(room_id)), HTTPStatus.OK)


@room_bp.put('/<int:room_id>')
def update_room(room_id: int) -> Response:
    content = request.get_json()
    room = Rooms.create_from_dto(content)
    room_controller.update(room_id, room)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.patch('/<int:room_id>')
def patch_room(room_id: int) -> Response:
    content = request.get_json()
    room_controller.patch(room_id, content)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.delete('/<int:room_id>')
def delete_room(room_id: int) -> Response:
    room_controller.delete(room_id)
    return make_response("Room deleted", HTTPStatus.OK)


@room_bp.get('/get-rooms-after-number/<int:in_num>')
def get_rooms_after_number(in_num: int) -> Response:
    return make_response(jsonify(room_controller.get_rooms_after_number(in_num)), HTTPStatus.OK)


@room_bp.get('/get-rooms-with-name-and-number-filter/<string:name_filter>/after-number/<int:in_num>')
def get_rooms_with_name_and_number_filter(name_filter: str, in_num: int) -> Response:
    return make_response(jsonify(room_controller.get_rooms_with_name_and_number_filter(name_filter, in_num)),
                         HTTPStatus.OK)
