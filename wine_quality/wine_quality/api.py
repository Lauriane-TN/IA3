import pickle
import pandas as pd
from typing import Union
import numpy as np

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root(alcohol: Union[float, None] = None,
        sulphates: Union[float, None] = None,
        citric_acid: Union[float, None] = None,
        volatile_acidity: Union[float, None] = None
                    ):
    input_user = read_user_input(alcohol, sulphates, citric_acid, volatile_acidity)
    pickle_model = pickle.load(open("model.pkl", "rb"))
    pred = pickle_model.predict(input_user)
    return {"prediction": f"{round(pred[0])}"}

def read_user_input(alcohol, sulphates, citric_acid, volatile_acidity):
    input_user = pd.DataFrame({
        'alcohol': [float(alcohol)],
        'sulphates': [float(sulphates)],
        'citric_acid': [float(citric_acid)],
        'volatile_acidity': [float(volatile_acidity)]
    })
    return input_user
