import os
from datetime import datetime
from networksecurity.constants import  training_pipeline_constants

# print(training_pipeline_constants.PIPELINE_NAME)
# print(training_pipeline_constants.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        # timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        # self.timestamp = timestamp
        self.timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline_constants.PIPELINE_NAME
        self.artifact_name = training_pipeline_constants.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, self.timestamp)


class DataIngestionConfig:
    def __init__(self, training_pipeline_constants_config = TrainingPipelineConfig()):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_constants_config.artifact_dir, 
            training_pipeline_constants.DATA_INGESTION_DIR_NAME
            )
        
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline_constants.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline_constants.FILE_NAME
            )
        
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline_constants.DATA_INGESTION_INGESTED_DIR,
            training_pipeline_constants.TRAIN_FILE_NAME
            )
        
        self.test_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline_constants.DATA_INGESTION_INGESTED_DIR,
            training_pipeline_constants.TEST_FILE_NAME
            )
        
        self.train_test_split_ratio: float = training_pipeline_constants.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = training_pipeline_constants.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline_constants.DATA_INGESTION_DATABASE_NAME
