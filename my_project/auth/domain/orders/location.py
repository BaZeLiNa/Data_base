# # app/domain/location.py
#
# from typing import Dict, Any
#
#
# class Location:
#     def __init__(self, location_id, city, country):
#         self.location_id = location_id
#         self.city = city
#         self.country = country
#
#     def put_into_dto(self) -> Dict[str, Any]:
#         return {
#             "location_id": self.location_id,
#             "city": self.city,
#             "country": self.country,
#         }
#
#     @staticmethod
#     def create_from_dto(dto_dict: Dict[str, Any]) -> 'Location':
#         return Location(
#             location_id=dto_dict.get("location_id"),
#             city=dto_dict.get("city"),
#             country=dto_dict.get("country"),
#         )


from typing import Dict, Any


class Location:
    def __init__(self, location_id: int, city: str, country: str):
        self.location_id = location_id
        self.city = city
        self.country = country

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Location':
        return Location(
            location_id=dto_dict.get('location_id'),
            city=dto_dict.get('city'),
            country=dto_dict.get('country')
        )


class LocationDto:
    def __init__(self, location_id: int, city: str, country: str):
        self.location_id = location_id
        self.city = city
        self.country = country

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'location_id': self.location_id,
            'city': self.city,
            'country': self.country
        }
