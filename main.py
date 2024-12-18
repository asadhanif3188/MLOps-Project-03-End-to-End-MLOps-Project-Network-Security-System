from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__ == "__main__":
    try:
        logging.info("From main.py")
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        
        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Data Ingestion Started")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")

        print(data_ingestion_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)