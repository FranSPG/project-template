from pydantic import BaseModel


class ProductBase(BaseModel):
    sku: str
    name: str
    price: float

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass
