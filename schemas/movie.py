from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int]= None
    title: str = Field(min_length=2, max_length=255)
    year: int = Field(le=2023)
    rating: int = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=40)


    class Config:
        schema_extra = {
            'example': {
                'title': "Mi pelicula",
                'year': 2022,
                'rating': 10,
                'category': 'Comedy'
            }
        }
