from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import network_controller
from my_project.auth.domain.orders.network import Network

network_bp = Blueprint('networks', __name__, url_prefix='/networks')

@network_bp.get('')
def get_all_networks() -> Response:
    return make_response(jsonify(network_controller.find_all()), HTTPStatus.OK)

@network_bp.post('')
def create_network() -> Response:
    content = request.get_json()
    network = Network.create_from_dto(content)
    network_controller.create(network)
    return make_response(jsonify(network.put_into_dto()), HTTPStatus.CREATED)

@network_bp.get('/<int:network_id>')
def get_network(network_id: int) -> Response:
    return make_response(jsonify(network_controller.find_by_id(network_id)), HTTPStatus.OK)

@network_bp.put('/<int:network_id>')
def update_network(network_id: int) -> Response:
    content = request.get_json()
    network = Network.create_from_dto(content)
    network_controller.update(network_id, network)
    return make_response("Network updated", HTTPStatus.OK)

@network_bp.patch('/<int:network_id>')
def patch_network(network_id: int) -> Response:
    content = request.get_json()
    network_controller.patch(network_id, content)
    return make_response("Network updated", HTTPStatus.OK)

@network_bp.delete('/<int:network_id>')
def delete_network(network_id: int) -> Response:
    network_controller.delete(network_id)
    return make_response("Network deleted", HTTPStatus.OK)

@network_bp.get('/get-networks-after-number/<int:in_num>')
def get_networks_after_number(in_num: int) -> Response:
    return make_response(jsonify(network_controller.get_networks_after_number(in_num)), HTTPStatus.OK)

@network_bp.get('/get-networks-with-name-and-number-filter/<string:name_filter>/after-number/<int:in_num>')
def get_networks_with_name_and_number_filter(name_filter: str, in_num: int) -> Response:
    return make_response(jsonify(network_controller.get_networks_with_name_and_number_filter(name_filter, in_num)),
                         HTTPStatus.OK)


