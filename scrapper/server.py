from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Store(BaseModel):
    url: str


@app.get("/ping")
def read_root():
    return {"status": "ok"}


@app.post("/test")
def read_item(store: Store):
    print(store)
    return {"status": store}