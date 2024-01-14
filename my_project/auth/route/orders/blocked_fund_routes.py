from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import blocked_fund_controller
from my_project.auth.domain.orders.blocked_fund import BlockedFund

blocked_fund_bp = Blueprint('blocked_funds', __name__, url_prefix='/blocked-funds')

@blocked_fund_bp.get('')
def get_all_blocked_funds() -> Response:
    return make_response(jsonify(blocked_fund_controller.find_all()), HTTPStatus.OK)

@blocked_fund_bp.post('')
def create_blocked_fund() -> Response:
    content = request.get_json()
    blocked_fund = BlockedFund.create_from_dto(content)
    blocked_fund_controller.create(blocked_fund)
    return make_response(jsonify(blocked_fund.put_into_dto()), HTTPStatus.CREATED)

@blocked_fund_bp.get('/<int:blocked_fund_id>')
def get_blocked_fund(blocked_fund_id: int) -> Response:
    return make_response(jsonify(blocked_fund_controller.find_by_id(blocked_fund_id)), HTTPStatus.OK)

@blocked_fund_bp.put('/<int:blocked_fund_id>')
def update_blocked_fund(blocked_fund_id: int) -> Response:
    content = request.get_json()
    blocked_fund = BlockedFund.create_from_dto(content)
    blocked_fund_controller.update(blocked_fund_id, blocked_fund)
    return make_response("Blocked Fund updated", HTTPStatus.OK)

@blocked_fund_bp.patch('/<int:blocked_fund_id>')
def patch_blocked_fund(blocked_fund_id: int) -> Response:
    content = request.get_json()
    blocked_fund_controller.patch(blocked_fund_id, content)
    return make_response("Blocked Fund updated", HTTPStatus.OK)

@blocked_fund_bp.delete('/<int:blocked_fund_id>')
def delete_blocked_fund(blocked_fund_id: int) -> Response:
    blocked_fund_controller.delete(blocked_fund_id)
    return make_response("Blocked Fund deleted", HTTPStatus.OK)
