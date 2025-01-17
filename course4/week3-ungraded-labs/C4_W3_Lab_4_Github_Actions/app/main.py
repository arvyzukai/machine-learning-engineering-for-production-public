import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist


# test GitHub Actions
app = FastAPI(title="Predicting Wine Class with batching")

# Open classifier in global scope
with open("models/wine-95-fixed.pkl", "rb") as file:
    clf = pickle.load(file)


class Wine(BaseModel):
    batches: List[conlist(item_type=float, min_length=13, max_length=13)]


@app.post("/predict")
def predict(wine: Wine):
    batches = wine.batches
    np_batches = np.array(batches)
    pred = clf.predict(np_batches).tolist()
    return {"Prediction": pred}
    
    
# Test actions v4 config yaml scikit-learn==0.24.2
# Python 3.8
# min_items -> min_length
# yaml formatting test
# v2 test
