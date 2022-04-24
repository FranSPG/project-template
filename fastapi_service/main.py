from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models
from .crud import create_product
from .schemas import ProductBase, ProductCreate
from .db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def main():
    return """<h1>Welcome to the FastAPI product service</h1>"""


@app.post("/products/", response_model=ProductBase)
def create_product_function(
        product: ProductCreate, db: Session = Depends(get_db)
):
    return create_product(product=product, db=db)
