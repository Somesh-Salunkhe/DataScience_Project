from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import  ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def model_evaluate(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluator = ModelEvaluation(config=model_evaluation_config)
        model_evaluator.log_in_mlflow()