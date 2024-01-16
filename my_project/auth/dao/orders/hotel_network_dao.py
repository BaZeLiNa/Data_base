from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.hotel_network import HotelNetworks


class HotelNetworkDAO(GeneralDAO):
    _domain_type = HotelNetworks

    # Додайте інші методи DAO за необхідності
