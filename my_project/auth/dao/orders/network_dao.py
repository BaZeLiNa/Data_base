from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.network import Networks


class NetworkDAO(GeneralDAO):
    _domain_type = Networks
