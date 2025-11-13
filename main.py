import sys
from networksecurity.components.data_ingestion import DataIngestion, DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformationConfig, DataTransformation


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

        logging.info("Initiate data transformation...")
        data_transformation_config = DataTransformationConfig(trainingPipelineConfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed..")

    except Exception as e:
        raise NetworkSecurityException(e, sys)

