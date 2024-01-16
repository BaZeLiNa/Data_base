from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class BlockedFunds(db.Model, IDto):
    __tablename__ = 'blocked_funds'

    blocked_fund_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)  # foreign key
    amount = db.Column(db.Integer)
    expiry_date = db.Column(db.Date)

    def __repr__(self):
        return (f"BlockedFund(blocked_fund_id={self.blocked_fund_id}, user_id={self.user_id},"
                f" amount={self.amount}, expiry_date={self.expiry_date})")

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'BlockedFunds':
        obj = BlockedFunds(
            blocked_fund_id=dto_dict.get("blocked_fund_id"),
            user_id=dto_dict.get("user_id"),
            amount=dto_dict.get("amount"),
            expiry_date=dto_dict.get("expiry_date"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "blocked_fund_id": self.blocked_fund_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "expiry_date": self.expiry_date,
        }
