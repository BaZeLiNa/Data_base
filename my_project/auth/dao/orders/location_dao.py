from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.hotel import Hotels
from my_project.auth.domain.orders.location import Locations


class LocationDAO(GeneralDAO):
    _domain_type = Locations

    def find_hotels_in_location(self, location_id: int):
        hotels_in_location = (
            self._session.query(Hotels, Locations)
            .join(Locations, Hotels.location_id == Locations.location_id)
            .filter(Hotels.location_id == location_id)
            .all()
        )

        hotels_data = [
            {
                "hotels": {
                    "hotel_id": hotel.hotel_id,
                    "name": hotel.name,
                    "location_id": hotel.location_id,
                    "rating": hotel.rating,
                },
            }
            for hotel, location in hotels_in_location
        ]

        return hotels_data
