from pydantic import BaseModel


class User_schema(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'admin',
                'password': 'admin'
            }
        }