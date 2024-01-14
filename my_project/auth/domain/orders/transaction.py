# app/domain/transaction.py

from typing import Dict, Any


class Transaction:
    def __init__(self, transaction_id, user_id, amount, date):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.date = date

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Transaction':
        return Transaction(
            transaction_id=dto_dict.get("transaction_id"),
            user_id=dto_dict.get("user_id"),
            amount=dto_dict.get("amount"),
            date=dto_dict.get("date"),
        )
