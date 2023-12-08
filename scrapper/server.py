from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scrappers.generic import scrapper

app = FastAPI()

origins = ['http://127.0.0.1:8000', 'https://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Response(BaseModel):
    search_url: str
    base_url: str
    results_classes: str
    name_classes: str
    price_classes: str
    testing_ean: str


@app.get("/ping")
def read_root():
	return {"status": "ok"}


@app.post("/test")
def read_item(res: Response):
    store = {
        'search_url': res.search_url,
        'base_url': res.base_url,
        'results_classes': res.results_classes,
        'name_classes': res.name_classes,
        'price_classes': res.price_classes,
    }
    return scrapper(store, res.testing_ean)