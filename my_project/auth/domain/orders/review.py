# app/domain/review.py

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Reviews(db.Model, IDto):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer)  # foreign key
    user_id = db.Column(db.Integer)  # foreign key
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(255))

    def __repr__(self):
        return (f"Review(review_id={self.review_id}, hotel_id={self.hotel_id},"
                f" user_id={self.user_id}, rating={self.rating}, comment={self.comment})")

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Reviews':
        return Reviews(
            review_id=dto_dict.get("review_id"),
            hotel_id=dto_dict.get("hotel_id"),
            user_id=dto_dict.get("user_id"),
            rating=dto_dict.get("rating"),
            comment=dto_dict.get("comment"),
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "review_id": self.review_id,
            "hotel_id": self.hotel_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "comment": self.comment,
        }
