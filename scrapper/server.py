from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scrappers.generic import scrapper, get_product_url, get_product_content, get_product_details

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
    results_classes: str | None
    name_classes: str | None
    price_classes: str | None
    currency: str
    redirected: bool
    testing_ean: str


@app.get("/ping")
def read_root():
	return {"status": "ok"}


@app.post("/test")
def read_item(res: Response):
    try:
        store = {
            'search_url': res.search_url,
            'base_url': res.base_url,
            'results_classes': res.results_classes,
            'name_classes': res.name_classes,
            'price_classes': res.price_classes,
            'redirected': res.redirected,
            'currency': res.currency,
        }

        print(store)

        resdata = {
             "product_url": None,
             "product_content": None,
             "product_details": None,
        }

        if not store['redirected']:
            resdata["product_url"] = get_product_url(store, res.testing_ean)
            if not resdata["product_url"]:
                return resdata
        else:
            resdata["product_url"] = store['search_url'] + res.testing_ean

        product_content = get_product_content(resdata["product_url"])
        if not product_content:
            return resdata
        
        resdata["product_content"] = "Ok"
        resdata["product_details"] = get_product_details(store, product_content, resdata["product_url"])	
        if not resdata["product_details"]:
             return resdata
        return resdata

        
        # return scrapper(store, res.testing_ean)
    except:
        return { 'error': "scrapper has failed"}