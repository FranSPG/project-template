from sqlalchemy import Column, Integer, String, Float

from .db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String)
    name = Column(String)
    price = Column(Float)
