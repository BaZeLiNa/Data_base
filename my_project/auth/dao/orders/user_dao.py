# app/dao/user_dao.py

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.blocked_fund import BlockedFunds
from my_project.auth.domain.orders.reservation import Reservations
from my_project.auth.domain.orders.review import Reviews
from my_project.auth.domain.orders.transaction import Transactions
from my_project.auth.domain.orders.user import Users


class UserDAO(GeneralDAO):
    _domain_type = Users

    def find_users_with_blocked_funds(self, user_id: int):
        users_with_blocked_funds = (
            self._session.query(Users, BlockedFunds)
            .join(BlockedFunds, Users.user_id == BlockedFunds.user_id)
            .filter(Users.user_id == user_id)
            .all()
        )

        users_data = [
            {
                "blocked_funds": {
                    "blocked_fund_id": blocked_fund.blocked_fund_id,
                    "amount": blocked_fund.amount,
                    "expiry_date": blocked_fund.expiry_date,
                },
            }
            for user, blocked_fund in users_with_blocked_funds
        ]

        return users_data

    def find_users_with_transactions(self, user_id: int):
        users_with_transactions = (
            self._session.query(Users, Transactions)
            .join(Transactions, Users.user_id == Transactions.user_id)
            .filter(Users.user_id == user_id)
            .all()
        )

        users_data = [
            {
                "transactions": {
                    "transaction_id": transaction.transaction_id,
                    "amount": transaction.amount,
                    "date": transaction.date,
                },
            }
            for user, transaction in users_with_transactions
        ]

        return users_data

    def find_users_with_reviews(self, user_id: int):
        users_with_reviews = (
            self._session.query(Users, Reviews)
            .join(Reviews, Users.user_id == Reviews.user_id)
            .filter(Users.user_id == user_id)
            .all()
        )

        users_data = [
            {
                "reviews": {
                    "review_id": review.review_id,
                    "hotel_id": review.hotel_id,
                    "rating": review.rating,
                    "comment": review.comment,
                },
            }
            for user, review in users_with_reviews
        ]

        return users_data

    def find_users_with_reservations(self, user_id: int):
        users_with_reservations = (
            self._session.query(Users, Reservations)
            .join(Reservations, Users.user_id == Reservations.user_id)
            .filter(Users.user_id == user_id)
            .all()
        )

        users_data = [
            {
                "reservations": {
                    "reservation_id": reservation.reservation_id,
                    "hotel_id": reservation.hotel_id,
                    "room_number": reservation.room_number,
                    "checkin_date": reservation.checkin_date,
                    "checkout_date": reservation.checkout_date,
                },
            }
            for user, reservation in users_with_reservations
        ]

        return users_data
