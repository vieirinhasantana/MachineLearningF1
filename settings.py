import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", 'develop').lower()
URL_DATASET_DOWNLOAD = os.environ.get("URL_DATASET_DOWNLOAD", 'http://ergast.com/downloads/f1db_csv.zip')

MONGO_URL = os.environ.get("MONGO_URL", "ds133550.mlab.com:33550")
MONGO_DATABASE = os.environ.get("MONGO_DATABASE", "formula-1")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "sOuUoMfXpgcs")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "T1KtTupYdaZtkB8C")
