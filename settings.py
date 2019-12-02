import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", 'develop').lower()

MONGO_URL = os.environ.get("MONGO_URL", "cluster0-shard-00-00-h1dgk.gcp.mongodb.net")
MONGO_DATABASE = os.environ.get("MONGO_DATABASE", "machine-learning")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "cedrotech_ai")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "tEnrrKgE")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "text-bigdata")

MONGO_COLLECTION_SENTIMENT_ANALYSIS_GOOGLE = os.environ.get("MONGO_COLLECTION_SENTIMENT_ANALYSIS_GOOGLE", "sentiment-analysis-google")
MONGO_COLLECTION_SENTIMENT_ANALYSIS_IBM = os.environ.get("MONGO_COLLECTION_SENTIMENT_ANALYSIS_IBM", "sentiment-analysis-ibm")
