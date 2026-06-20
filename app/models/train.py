from .constants import DATA_FILE_PATH, MODEL_FILE_PATH
from app.schemas import Point
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle


def train(point: Point):
    df = pd.read_csv(DATA_FILE_PATH)
    df.loc[len(df.index)] = [point.x, point.y]
    df.to_csv(DATA_FILE_PATH, index=False)
    x_train = df[['x']]
    y_train = df[['y']]
    model = LinearRegression()
    model.fit(x_train, y_train)
    with open(MODEL_FILE_PATH, "wb") as file:
        pickle.dump(model, file)
