# app/domain/blocked_fund.py

from typing import Dict, Any


class BlockedFund:
    def __init__(self, blocked_fund_id, user_id, amount, expiry_date):
        self.blocked_fund_id = blocked_fund_id
        self.user_id = user_id
        self.amount = amount
        self.expiry_date = expiry_date

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "blocked_fund_id": self.blocked_fund_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "expiry_date": self.expiry_date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'BlockedFund':
        return BlockedFund(
            blocked_fund_id=dto_dict.get("blocked_fund_id"),
            user_id=dto_dict.get("user_id"),
            amount=dto_dict.get("amount"),
            expiry_date=dto_dict.get("expiry_date"),
        )
