from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import hotel_network_controller, hotel_controller, network_controller
from my_project.auth.domain.orders.hotel import Hotels
from my_project.auth.domain.orders.hotel_network import HotelNetworks
from my_project.auth.domain.orders.network import Networks


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


@hotel_network_bp.get('/<int:identifier>')
def get_hotel_network(identifier: int) -> Response:
    if is_hotel_id(identifier):
        return make_response(jsonify(hotel_controller.find_by_id(identifier)), HTTPStatus.OK)
    elif is_network_id(identifier):
        return make_response(jsonify(network_controller.find_by_id(identifier)), HTTPStatus.OK)
    else:
        return make_response(jsonify({"error": "Invalid identifier"}), HTTPStatus.BAD_REQUEST)


def is_hotel_id(identifier: int) -> bool:
    return Hotels.query.filter_by(hotel_id=identifier).first() is not None


def is_network_id(identifier: int) -> bool:
    return Networks.query.filter_by(network_id=identifier).first() is not None


@hotel_network_bp.put('/<int:hotel_id>')
def update_hotel_network(hotel_id: int, network_id: int) -> Response:
    content = request.get_json()
    hotel_network = HotelNetworks.create_from_dto(content)
    hotel_network_controller.update(hotel_id, network_id, hotel_network)
    return make_response("Hotel Network updated", HTTPStatus.OK)


@hotel_network_bp.delete('/<int:hotel_id>')
def delete_hotel_network(hotel_id: int, network_id: int) -> Response:
    hotel_network_controller.delete(hotel_id, network_id)
    return make_response("Hotel Network deleted", HTTPStatus.OK)


@hotel_network_bp.patch('/<int:hotel_id>')
def patch_hotel_network(hotel_id: int, network_id: int) -> Response:
    content = request.get_json()
    hotel_network = hotel_network_controller.find_by_ids(hotel_id, network_id)
    if hotel_network is None:
        return make_response("Hotel Network not found", HTTPStatus.NOT_FOUND)
    hotel_network_controller.patch(hotel_id, network_id, content)
    return make_response("Hotel Network patched", HTTPStatus.OK)
