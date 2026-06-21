from .constants import MODEL_FILE_PATH
from app.schemas import Point
import pandas as pd
import pickle


def predict_y(x):
    with open(MODEL_FILE_PATH, "rb") as file:
        model = pickle.load(file)
    x_unknown = pd.DataFrame([[x]], columns=['x'])
    y_unknown = model.predict(x_unknown)
    return Point(x=x, y=y_unknown[0][0])
