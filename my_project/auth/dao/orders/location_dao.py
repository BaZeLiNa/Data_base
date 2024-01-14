# app/dao/location_dao.py

from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.location import Location

class LocationDAO(GeneralDAO):
    _domain_type = Location

    # Додайте інші методи DAO за необхідності

    def find_by_city(self, city: str) -> Location:
        """
        Find a location by its city.
        :param city: City name
        :return: Location object
        """
        return self._session.query(self._domain_type).filter_by(city=city).first()

    def find_by_country(self, country: str) -> Location:
        """
        Find a location by its country.
        :param country: Country name
        :return: Location object
        """
        return self._session.query(self._domain_type).filter_by(country=country).first()

    # Додайте інші методи за необхідності
