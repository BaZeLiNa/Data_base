from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.hotel import Hotels
from my_project.auth.domain.orders.hotel_network import HotelNetworks
from my_project.auth.domain.orders.network import Networks


class NetworkDAO(GeneralDAO):
    _domain_type = Networks

    def find_hotels_in_network(self, network_id: int):
        hotels_in_network = (
            self._session.query(Hotels, HotelNetworks)
            .join(HotelNetworks, Hotels.hotel_id == HotelNetworks.hotel_id)
            .filter(HotelNetworks.network_id == network_id)
            .all()
        )

        hotels_data = [
            {
                "hotel": {
                    "hotel_id": hotel.hotel_id,
                    "name": hotel.name,
                    "location_id": hotel.location_id,
                    "rating": hotel.rating,
                },
            }
            for hotel, network in hotels_in_network
        ]

        return hotels_data

