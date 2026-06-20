from app.models import predict, train
from app.schemas import Point
from fastapi import FastAPI

app = FastAPI()


@app.get("/model.predict/{x}")
async def predict_y(x: float):
    return predict(x)


@app.post("/model/train", status_code=201)
async def train_model(data: Point):
    train(data)
