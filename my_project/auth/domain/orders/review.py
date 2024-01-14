# app/domain/review.py

from typing import Dict, Any


class Review:
    def __init__(self, review_id, hotel_id, user_id, rating, comment):
        self.review_id = review_id
        self.hotel_id = hotel_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "review_id": self.review_id,
            "hotel_id": self.hotel_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "comment": self.comment,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Review':
        return Review(
            review_id=dto_dict.get("review_id"),
            hotel_id=dto_dict.get("hotel_id"),
            user_id=dto_dict.get("user_id"),
            rating=dto_dict.get("rating"),
            comment=dto_dict.get("comment"),
        )
