from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.room import Rooms


class RoomDAO(GeneralDAO):
    _domain_type = Rooms

    # Додайте інші методи DAO за необхідності

