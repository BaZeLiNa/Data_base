from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Transactions(db.Model, IDto):
    __tablename__ = 'transactions'

    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    amount = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False))
    date = db.Column(db.Date)

    user = db.relationship('Users', back_populates='transactions')

    def __repr__(self):
        return (f"Transaction(transaction_id={self.transaction_id},"
                f" user_id={self.user_id}, amount={self.amount}, date={self.date})")

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Transactions':
        obj = Transactions(
            transaction_id=dto_dict.get("transaction_id"),
            user_id=dto_dict.get("user_id"),
            amount=dto_dict.get("amount"),
            date=dto_dict.get("date"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "date": self.date,
        }
