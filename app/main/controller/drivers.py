import json

import requests
from logzero import logger
from datetime import datetime


class Drivers:
    def __init__(self, past_seasons: int = 6):
        self._seasons = past_seasons
        self._session = requests.Session()

    @property
    def __get_current_year(self) -> int:
        now = datetime.now()
        return now.year

    def __page_source(self, year: int):
        try:
            response = self._session.get(
                url=f'http://ergast.com/api/f1/{year}/drivers.json?callback=drivers',
                timeout=60
            )
            if not response.ok:
                logger.error('Not possible open page')

            return response.text

        except Exception as e:
            logger.error(f'Occurred error in use request. ERROR ---> {e}')

    @staticmethod
    def __extract_content_from_json(data, year) -> list:
        _new_data = data.replace('drivers(', '').replace(')', '')
        drivers = json.loads(_new_data)
        for row in drivers.get('MRData', {}).get('DriverTable', {}).get('Drivers', []):
            row['season'] = year

        return drivers.get('MRData', {}).get('DriverTable', {}).get('Drivers', [])

    def get_drivers(self):
        for season in range(self._seasons):
            search_by_year = self.__get_current_year - season
            _data = self.__page_source(year=search_by_year)
            _drivers = Drivers.__extract_content_from_json(data=_data, year=search_by_year)
            return _drivers