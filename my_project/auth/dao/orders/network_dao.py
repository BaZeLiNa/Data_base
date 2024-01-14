# app/dao/network_dao.py

from typing import Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.network import Network


class NetworkDAO(GeneralDAO):
    _domain_type = Network

    # Додайте інші методи DAO за необхідності

    def find_by_name(self, network_name: str) -> Network:
        """
        Find a network by its name.
        :param network_name: Name of the network
        :return: Network object
        """
        return self._session.query(self._domain_type).filter_by(network_name=network_name).first()

    # Додайте інші методи за необхідності
