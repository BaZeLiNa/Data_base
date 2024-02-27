"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.reservation_service import ReservationService
from .orders.review_service import ReviewService
from .orders.user_service import UserService
from .orders.room_service import RoomService
from .orders.network_service import NetworkService
from .orders.transaction_service import TransactionService
from .orders.location_service import LocationService
from .orders.hotel_service import HotelService
# from .orders.hotel_network_service import HotelNetworkService
from .orders.blocked_fund_service import BlockedFundService
# from .orders.guest_service import GuestService


reservation_service = ReservationService()
review_service = ReviewService()
user_service = UserService()
room_service = RoomService()
network_service = NetworkService()
transaction_service = TransactionService()
location_service = LocationService()
hotel_service = HotelService()
# hotel_network_service = HotelNetworkService()
blocked_fund_service = BlockedFundService()
# guest_service = GuestService()
