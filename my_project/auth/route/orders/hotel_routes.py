from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import hotel_controller
from my_project.auth.domain.orders.hotel import Hotels
hotel_bp = Blueprint('hotels', __name__, url_prefix='/hotels')


@hotel_bp.get('')
def get_all_hotels() -> Response:
    return make_response(jsonify(hotel_controller.find_all()), HTTPStatus.OK)


@hotel_bp.post('')
def create_hotel() -> Response:
    content = request.get_json()
    hotel = Hotels.create_from_dto(content)
    hotel_controller.create(hotel)
    return make_response(jsonify(hotel.put_into_dto()), HTTPStatus.CREATED)


@hotel_bp.get('/<int:hotel_id>')
def get_hotel(hotel_id: int) -> Response:
    return make_response(jsonify(hotel_controller.find_by_id(hotel_id)), HTTPStatus.OK)


@hotel_bp.get('/rooms/<int:hotel_id>')
def get_hotel_rooms(hotel_id: int) -> Response:
    return make_response(jsonify(hotel_controller.find_rooms_in_hotel(hotel_id)), HTTPStatus.OK)


@hotel_bp.get('/reservations/<int:hotel_id>')
def get_hotel_reservations(hotel_id: int) -> Response:
    return make_response(jsonify(hotel_controller.find_reservations_in_hotels(hotel_id)), HTTPStatus.OK)


@hotel_bp.get('/reviews/<int:hotel_id>')
def get_hotel_reviews(hotel_id: int) -> Response:
    return make_response(jsonify(hotel_controller.find_hotels_with_reviews(hotel_id)), HTTPStatus.OK)


@hotel_bp.get('/networks/<int:hotel_id>')
def get_hotel_networks(hotel_id: int) -> Response:
    return make_response(jsonify(hotel_controller.find_hotels_with_networks(hotel_id)), HTTPStatus.OK)


@hotel_bp.put('/<int:hotel_id>')
def update_hotel(hotel_id: int) -> Response:
    content = request.get_json()
    hotel = Hotels.create_from_dto(content)
    hotel_controller.update(hotel_id, hotel)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.patch('/<int:hotel_id>')
def patch_hotel(hotel_id: int) -> Response:
    content = request.get_json()
    hotel_controller.patch(hotel_id, content)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.delete('/<int:hotel_id>')
def delete_hotel(hotel_id: int) -> Response:
    hotel_controller.delete(hotel_id)
    return make_response("Hotel deleted", HTTPStatus.OK)
