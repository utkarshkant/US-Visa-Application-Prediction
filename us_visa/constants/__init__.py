import os
from datetime import date
import os
from dotenv import load_dotenv
load_dotenv()


DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = os.getenv("MONGODB_CONNECTION_STRING")
PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"
MODEL_FILE_NAME = "model.pkl"
FILE_NAME = "usvisa.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

DATA_INGESTION_COLLECTION_NAME: str = "visa-data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2