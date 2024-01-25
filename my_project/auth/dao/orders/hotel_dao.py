from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Hotels
from my_project.auth.domain.orders.hotel_network import HotelNetworks
from my_project.auth.domain.orders.network import Networks
from my_project.auth.domain.orders.reservation import Reservations
from my_project.auth.domain.orders.review import Reviews
from my_project.auth.domain.orders.room import Rooms


class HotelDAO(GeneralDAO):
    _domain_type = Hotels

    def find_rooms_in_hotel(self, hotel_id: int):
        """
        Find all rooms in a hotel by hotel_id in rooms table
        """
        rooms_in_hotel = (
            self._session.query(Rooms, Hotels)
            .join(Hotels, Rooms.hotel_id == Hotels.hotel_id)
            .filter(Rooms.hotel_id == hotel_id)
            .all()
        )

        room_data = [
            {
                "room": {
                    "room_number": room.room_number,
                    "hotel_id": room.hotel_id,
                    "room_type": room.room_type,
                    "price": room.price,
                },
            }
            for room, hotel in rooms_in_hotel
        ]

        return room_data

    def find_reservations_in_hotels(self, hotel_id: int):
        hotels_with_reservations = (
            self._session.query(Hotels, Reservations)
            .join(Reservations, Hotels.hotel_id == Reservations.hotel_id)
            .filter(Hotels.hotel_id == hotel_id)
            .all()
        )

        hotels_data = [
            {
                "reservations": {
                    "reservation_id": reservation.reservation_id,
                    "user_id": reservation.user_id,
                    "room_number": reservation.room_number,
                    "checkin_date": reservation.checkin_date,
                    "checkout_date": reservation.checkout_date,
                },
            }
            for hotel, reservation in hotels_with_reservations
        ]

        return hotels_data

    def find_hotels_with_reviews(self, hotel_id: int):
        hotels_with_reviews = (
            self._session.query(Hotels, Reviews)
            .join(Reviews, Hotels.hotel_id == Reviews.hotel_id)
            .filter(Hotels.hotel_id == hotel_id)
            .all()
        )

        hotels_data = [
            {
                "reviews": {
                    "review_id": review.review_id,
                    "user_id": review.user_id,
                    "rating": review.rating,
                    "comment": review.comment,
                },
            }
            for hotel, review in hotels_with_reviews
        ]

        return hotels_data

    def find_networks_in_hotel(self, hotel_id: int):
        """
        Find all rooms in a hotel by hotel_id in rooms table
        """
        rooms_in_hotel = (
            self._session.query(Rooms, Hotels)
            .join(Hotels, Rooms.hotel_id == Hotels.hotel_id)
            .filter(Rooms.hotel_id == hotel_id)
            .all()
        )

        room_data = [
            {
                "room": {
                    "room_number": room.room_number,
                    "hotel_id": room.hotel_id,
                    "room_type": room.room_type,
                    "price": room.price,
                },
            }
            for room, hotel in rooms_in_hotel
        ]

        return room_data

    def find_hotels_with_networks(self, hotel_id: int):
        hotels_with_networks = (
            self._session.query(Hotels, Networks)
            .join(HotelNetworks, Hotels.hotel_id == HotelNetworks.hotel_id)
            .join(Networks, HotelNetworks.network_id == Networks.network_id)
            .filter(Hotels.hotel_id == hotel_id)
            .all()
        )

        hotels_data = [
            {
                "networks": {
                    "network_id": network.network_id,
                    "network_name": network.network_name,
                },
            }
            for hotel, network in hotels_with_networks
        ]

        return hotels_data

