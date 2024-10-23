from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
import os

STAGE_NAME = "Model trainer stage"

class ModelTrainerTrainingPipeline():
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__init__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.train()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx--------------x")
    except Exception as e:
        logger.exception(e)
        raise e
    