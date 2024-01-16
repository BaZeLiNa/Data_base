from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import review_controller
from my_project.auth.domain.orders.review import Reviews


review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@review_bp.get('')
def get_all_reviews() -> Response:
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)

@review_bp.post('')
def create_review() -> Response:
    content = request.get_json()
    review = Reviews.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)

@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)

@review_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:
    content = request.get_json()
    review = Reviews.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)

@review_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:
    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)

@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)

@review_bp.get('/get-reviews-after-number/<int:in_num>')
def get_reviews_after_number(in_num: int) -> Response:
    return make_response(jsonify(review_controller.get_reviews_after_number(in_num)), HTTPStatus.OK)

@review_bp.get('/get-reviews-with-name-and-number-filter/<string:name_filter>/after-number/<int:in_num>')
def get_reviews_with_name_and_number_filter(name_filter: str, in_num: int) -> Response:
    return make_response(jsonify(review_controller.get_reviews_with_name_and_number_filter(name_filter, in_num)),
                         HTTPStatus.OK)
