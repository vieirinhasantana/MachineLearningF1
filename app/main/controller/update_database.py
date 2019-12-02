import zipfile
import io
import os
import shutil
import requests
from logzero import logger
from datetime import datetime

import settings


class UpdateDatabase:
    def __init__(self):
        self._session = requests.Session()

    def __enter__(self):
        if not os.path.exists('app/main/temp'):
            os.makedirs('app/main/temp')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree('app/main/temp', ignore_errors=True)

    @property
    def __get_current_year(self) -> int:
        now = datetime.now()
        return now.year

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
        self.__download_extract_fileszip()

