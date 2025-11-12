import sys
from networksecurity.components.data_ingestion import DataIngestion
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
        dataIngestion_initiate = dataIngestion.initiate_data_ingestion()
        print(dataIngestion_initiate)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

