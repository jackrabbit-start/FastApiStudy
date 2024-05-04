from typing import Annotated
from fastapi import Depends, FastAPI
from app.database import engine, oauth2_scheme
from .user import models as user_models, controllers as user_controllers

# item_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)


ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

app.include_router(user_controllers.router)
# app.include_router(item_controllers.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.get("/user/token/")
async def read_test(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
