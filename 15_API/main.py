from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()
app.counter = 0

class Product(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    code: str
    tax: Union[float, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def get_name(name: str):
    return f' Hello {name} :)'

@app.get("/counter")
def counter():
    app.counter += 1
    return {"counter": app.counter}

#Utwórz endpoint, który za pomocą metody post pozwala “dodać” produkt.
# Produkt ma pola: name (string), description (optional), price (float), code (string), tax (optional).
# Przy “dodaniu” endpoint zwraca dodany produkt i opcjonalnie cenę brutto produktu.

@app.post("/product")
def create_product(prod: Product):
    return prod
