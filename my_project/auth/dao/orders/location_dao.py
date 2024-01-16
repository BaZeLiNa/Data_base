from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.location import Locations


class LocationDAO(GeneralDAO):
    _domain_type = Locations
