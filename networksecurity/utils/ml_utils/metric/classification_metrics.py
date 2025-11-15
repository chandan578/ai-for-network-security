from networksecurity.entity.artifact_entity import  ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import recall_score, precision_score, f1_score
import sys

def get_classification_score(y_pred, y_true)->ClassificationMetricArtifact:

    try:
        f1_score_value = f1_score(y_pred, y_true)
        precision_score_value = precision_score(y_pred, y_true)
        recall_score_val = recall_score(y_pred, y_true)

        classification_metrix = ClassificationMetricArtifact(f1_score=f1_score_value, precision_score= precision_score_value, recall_score=recall_score_val)

        return classification_metrix
    except Exception as e:
        raise NetworkSecurityException(e, sys)
