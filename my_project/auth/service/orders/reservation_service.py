from my_project.auth.dao.orders import reservation_dao
from my_project.auth.service.general_service import GeneralService


class ReservationService(GeneralService):
    """
    Realisation of Reservation service.
    """
    _dao = reservation_dao
