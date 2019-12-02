import requests
from bs4 import BeautifulSoup
from logzero import logger
from datetime import datetime


class Drivers:
    def __init__(self, past_seasons: int):
        self._seasons = past_seasons
        self._session = requests.Session()

    def __page_source(self, year: int):
        try:
            response = self._session.get(
                url=f'https://www.formula1.com/en/results.html/{year}/drivers.html',
                timeout=60
            )
            if not response.ok:
                logger.error('Not possible open page')

            return response.text

        except Exception as e:
            logger.error(f'Occurred error in use request. ERROR ---> {e}')

    @staticmethod
    def __format_name_driver(name: str) -> (str, str):
        clear_name = name.strip()
        name_split = clear_name.split("\n")

        name_driver = f"{name_split[0]} { name_split[1]}"
        alias = name_split[2]

        return name_driver, alias

    @staticmethod
    def __extract_content_from_page(page_source, year):
        soup = BeautifulSoup(page_source, 'html.parser')
        table = soup.find('table', {'class': 'resultsarchive-table'})
        for row in table.find_all('tr')[1:]:
            _td = row.find_all('td')
            name_driver, alias = Drivers.__format_name_driver(name=_td[2].get_text())

            _obj = {
                'year': year,
                'pos': _td[1].get_text(),
                'driver': name_driver,
                'alias': alias,
                'nationality': _td[3].get_text(),
                'car': _td[4].get_text().strip(),
                'pts': _td[5].get_text()
            }
            print(_obj)
            break

    @property
    def __get_current_year(self) -> int:
        now = datetime.now()
        return now.year

    def drivers(self):
        for season in range(self._seasons):
            search_by_year = self.__get_current_year - season
            _source_page = self.__page_source(year=search_by_year)
            Drivers.__extract_content_from_page(page_source=_source_page, year=search_by_year)


Drivers(past_seasons=6).drivers()
