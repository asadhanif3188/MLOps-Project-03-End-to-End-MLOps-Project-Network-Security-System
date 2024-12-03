import os
import sys
import numpy as np
import pandas as pd

"""
Defining common constants for training pipeline 
"""

TARGET_COLUMNS: str = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion relate constants starts with DATA_INGESTION var name 
"""

DATA_INGESTION_COLLECTION_NAME: str = "netwrok_phising_data"
DATA_INGESTION_DATABASE_NAME: str = "asad_db"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2