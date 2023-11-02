import uvicorn
from fastapi import FastAPI
from test_user_db import users_db
from pydantic_models import User

app = FastAPI(title='Invite me')


@app.get("/")
def root_page():
    return {'Hello, world'}


@app.get("/users/")
def users(user_id: int):
    name = list(filter(lambda user: user.get('id') == user_id, users_db))[0]
    return {'msg': f'Hello, {name.get('name')}'}


@app.get("/user/{user_id}", response_model=User)
def user(user_id: int):
    current_user = [user for user in users_db if user.get('id') == user_id][0]
    return current_user


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, workers=3)
