import glob
import zipfile
import io
import csv
import os
import shutil
import requests
from logzero import logger

import settings
from ..persistence.mongo.mongo import MongoDB

class UpdateDatabase:
    def __init__(self):
        self._session = requests.Session()
        self.mgo = None

    def __enter__(self):
        self.mgo = MongoDB()

        if not os.path.exists('app/main/temp'):
            os.makedirs('app/main/temp')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    #     shutil.rmtree('app/main/temp', ignore_errors=True)

    def __save_database(self, data: dict, coll: str):
        _key = next(iter(data))
        self.mgo.save_or_update(
            query={_key: data.get(_key)},
            obj=data,
            collection=coll
        )

    @staticmethod
    def __headers_file_csv(file_name: str) -> list:
        headers = {
            'circuits.csv': ['circuitId', 'circuitRef', 'name', 'location', 'country', 'lat', 'lng', 'alt', 'url'],
            'constructor_results.csv': ['constructorResultsId', 'raceId', 'constructorId', 'points', 'status'],
            'constructor_standings.csv': ['constructorStandingsId', 'raceId', 'constructorId', 'points', 'position', 'positionText', 'wins'],
            'constructors.csv': ['constructorId', 'constructorRef', 'name', 'nationality', 'url'],
            'driver_standings.csv': ['driverStandingsId', 'raceId', 'driverId', 'points', 'position', 'positionText', 'wins'],
            'drivers.csv': ['driverId', 'driverRef', 'number', 'code', 'forename', 'surname', 'dob', 'nationality', 'url'],
            'lap_times.csv': ['raceId', 'driverId', 'lap', 'position', 'time', 'milliseconds'],
            'pit_stops.csv': ['raceId', 'driverId', 'stop', 'lap', 'time', 'duration', 'milliseconds'],
            'qualifying.csv': ['qualifyId', 'raceId', 'driverId', 'constructorId', 'number', 'position', 'q1', 'q2', 'q3'],
            'races.csv': ['raceId', 'year', 'round', 'circuitId', 'name', 'date', 'time', 'url'],
            'results.csv': ['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'positionOrder', 'points', 'laps', 'time', 'milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId'],
            'seasons.csv': ['year', 'url'],
            'status.csv': ['statusId', 'status']
        }
        return headers.get(file_name)

    def __mount_object(self):
        files = [f for f in glob.glob("app/main/temp/*.csv", recursive=True)]
        for f in files:
            file_dir = f.replace('\\', '/')
            file_name = file_dir.replace('app/main/temp/', '')

            _header = UpdateDatabase.__headers_file_csv(file_name=file_name)
            if _header:
                with open(file_dir, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        _obj = {}
                        for indx in range(0, len(_header)):
                            key = _header[indx]
                            value = row[indx]
                            _obj[key] = value

                        self.__save_database(data=_obj, coll=file_name.replace('.csv', ''))

    def __download_extract_fileszip(self):
        try:
            response = self._session.get(
                url=settings.URL_DATASET_DOWNLOAD,
                timeout=60
            )
            if not response.ok:
                logger.error(f'Not possible download dataset. GET [{settings.URL_DATASET_DOWNLOAD}]')

            z = zipfile.ZipFile(io.BytesIO(response.content))
            z.extractall('app/main/temp')

        except Exception as e:
            logger.error(f'Occurred error in use request. ERROR ---> {e}')

    def update_database(self):
        #self.__download_extract_fileszip()
        self.__mount_object()

