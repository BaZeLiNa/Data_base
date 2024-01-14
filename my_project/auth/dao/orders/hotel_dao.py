from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Hotels


class HotelDAO(GeneralDAO):
    _domain_type = Hotels
