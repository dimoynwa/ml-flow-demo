import numpy as np
import joblib
from pathlib import Path
import pandas as pd

class PredictionPipeline:
    def __init__(self) -> None:
        self.model = joblib.load(Path('./artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        predictions = self.model.predict(data)
        return predictions
    