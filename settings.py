import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", 'develop').lower()
URL_DATASET_DOWNLOAD = os.environ.get("URL_DATASET_DOWNLOAD", 'http://ergast.com/downloads/f1db_csv.zip')
