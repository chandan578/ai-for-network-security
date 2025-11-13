import sys
from networksecurity.components.data_ingestion import DataIngestion, DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__=='__main__':
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        dataIngestion = DataIngestion(dataIngestionConfig)
        
        logging.info('Initiate data ingestion...')
        dataIngestion_artifact = dataIngestion.initiate_data_ingestion()
        logging.info('Data ingestion completd...')
        print(dataIngestion_artifact)

        data_validation_config = DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(dataIngestion_artifact, data_validation_config)
        logging.info("Initiate data validation ..")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('Completed data validation...')
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)

