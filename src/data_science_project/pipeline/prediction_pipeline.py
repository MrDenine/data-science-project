import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def predict(self, input_data: pd.DataFrame):
        prediction = self.model.predict(input_data)

        return prediction
