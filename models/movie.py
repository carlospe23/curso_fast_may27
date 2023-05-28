from config.database import Base
from sqlalchemy import Column, Integer, String


class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key= True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Integer)
    category = Column(String)
