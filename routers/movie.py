from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()


# GET MOVIES
@movie_router.get("/movies", tags=['Movies'], response_model = List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content = jsonable_encoder(result) )


# GET MOVIE BY ID
@movie_router.get('/movie/{id}',  tags=['Movies'],  response_model = Movie)
def get_movie(id: int = Path( ge=1, le=2000)):
    db = Session()
    movie = MovieService(db).get_movie(id)
    if movie:
        return JSONResponse(status_code=200, content = jsonable_encoder(movie))
    return JSONResponse(status_code=404, content = {"message": "Movie not found"})

# GET MOVIE BY 
@movie_router.get('/moviesby/',  tags=['Movies'],  response_model = List[Movie])
def get_movies_by_cat(category: str = Query(min_length=5, max_length=40)) -> List[Movie]:
    category = category.capitalize()
    db = Session()
    moviesby = MovieService(db).get_movie_by(category)
    if moviesby:
        return JSONResponse(status_code=200,content = jsonable_encoder(moviesby))
    return JSONResponse(status_code=404,content = {"message": "Movies not found"})

# POST MOVIES
@movie_router.post('/movie', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content = {'message': 'Movie added succsesfully'})


# ACTUALIZAR MOVIES
@movie_router.put('/movie/{id}', tags=['Movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie):
    db = Session()
    result = MovieService(db).get_movie(id)
    if result:
        MovieService(db).update_movie(id, movie)
        return JSONResponse(status_code=200, content = {'message': 'Movie updated '})
    
    return JSONResponse(status_code=404, content = {"message": "Movie not found"})
    

# DELETE MOVIES
@movie_router.delete('/movie/{id}', tags=['Movies'], response_model=dict, status_code=200)
def delete_movie(id: int):
    db = Session()
    result = MovieService(db).get_movie(id)
    if result:
        MovieService(db).delete_movie(id)
        return JSONResponse(status_code=200, content = {'message': 'Movie deleted'})

    return JSONResponse(status_code=404, content = {"message": "Movie not found"})

