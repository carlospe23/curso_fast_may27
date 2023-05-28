from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manage import create_token
from schemas.user import User_schema

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User_schema):
    if user.username == 'admin' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200 ,content= token)
    return JSONResponse(status_code=404 ,content= {'message': 'User not found'})
    


