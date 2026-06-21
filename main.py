from app.models import get_data_map, predict_y, train_model
from app.schemas import Point
from fastapi import FastAPI

app = FastAPI()


@app.get(path="/data")
async def get_data():
    return get_data_map()


@app.get(path="/model/predict/{x}")
async def predict(x: float):
    return predict_y(x)


@app.post(path="/model/train", status_code=201)
async def train(data: Point):
    train_model(data)
