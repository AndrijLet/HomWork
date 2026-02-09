from pydantic import BaseModel
from typing import Optional

"""Стандатна """
class ListingBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float


"""Для подальших змін"""
class ListingCreate(ListingBase):
    pass

# схема для оновлення
class ListingUpdate(ListingBase):
    pass

# схема для ВІДПОВІДІ
class Listing(ListingBase):
    id: int

    class Config:"""дозволяє FastAPI брати дані не тільки з dict а й з обʼєктів словників"""
        from_attributes = True

# http://127.0.0.1:8000/docs
#
# http://127.0.0.1:8000/redoc
#