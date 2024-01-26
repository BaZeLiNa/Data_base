from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.hotel import Hotels
from my_project.auth.domain.orders.hotel_network import HotelNetworks
from my_project.auth.domain.orders.network import Networks


class NetworkDAO(GeneralDAO):
    _domain_type = Networks

    def find_hotels_in_network(self, network_id: int):
        hotels_in_network = (
            self._session.query(Networks, Hotels)
            .join(HotelNetworks, Networks.network_id == HotelNetworks.network_id)
            .join(Hotels, HotelNetworks.hotel_id == Hotels.hotel_id)
            .filter(Networks.network_id == network_id)
            .all()
        )

        hotels_data = [
            {
                "networks": {
                    "network_id": network.network_id,
                    "network_name": network.network_name,
                },
                "hotel": {
                    "hotel_id": hotel.hotel_id,
                    "name": hotel.name,
                    "location_id": hotel.location_id,
                    "rating": hotel.rating,
                },
            }
            for network, hotel in hotels_in_network
        ]

        return hotels_data

