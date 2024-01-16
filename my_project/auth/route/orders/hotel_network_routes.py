
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import hotel_network_controller
from my_project.auth.domain.orders.hotel_network import HotelNetworks

hotel_network_bp = Blueprint('hotel_networks', __name__, url_prefix='/hotel-networks')

@hotel_network_bp.get('')
def get_all_hotel_networks() -> Response:
    return make_response(jsonify(hotel_network_controller.find_all()), HTTPStatus.OK)

@hotel_network_bp.post('')
def create_hotel_network() -> Response:
    content = request.get_json()
    hotel_network = HotelNetworks.create_from_dto(content)
    hotel_network_controller.create(hotel_network)
    return make_response(jsonify(hotel_network.put_into_dto()), HTTPStatus.CREATED)

@hotel_network_bp.get('/<int:hotel_network_id>')
def get_hotel_network(hotel_network_id: int) -> Response:
    return make_response(jsonify(hotel_network_controller.find_by_id(hotel_network_id)), HTTPStatus.OK)

@hotel_network_bp.put('/<int:hotel_network_id>')
def update_hotel_network(hotel_network_id: int) -> Response:
    content = request.get_json()
    hotel_network = HotelNetworks.create_from_dto(content)
    hotel_network_controller.update(hotel_network_id, hotel_network)
    return make_response("Hotel Network updated", HTTPStatus.OK)

@hotel_network_bp.patch('/<int:hotel_network_id>')
def patch_hotel_network(hotel_network_id: int) -> Response:
    content = request.get_json()
    hotel_network_controller.patch(hotel_network_id, content)
    return make_response("Hotel Network updated", HTTPStatus.OK)

@hotel_network_bp.delete('/<int:hotel_network_id>')
def delete_hotel_network(hotel_network_id: int) -> Response:
    hotel_network_controller.delete(hotel_network_id)
    return make_response("Hotel Network deleted", HTTPStatus.OK)
