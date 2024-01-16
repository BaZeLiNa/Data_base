# app/dao/reservation_dao.py

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.reservation import Reservations


class ReservationDAO(GeneralDAO):
    _domain_type = Reservations

