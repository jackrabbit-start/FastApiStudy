from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.user.dependencies import get_current_active_user

from . import models, schemas, services
from sqlalchemy.orm import Session
from ..dependencies import get_db
from fastapi import status

router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


# @router.post("/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = services.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return services.create_user(db, user)


# @router.get("/", response_model=schemas.User)
# async def read_user(current_user: models.User = Depends(services.get_current_user)):
#     return current_user


@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = services.authenticate_user(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = services.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.AuthToken(access_token=access_token, token_type="bearer")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db, user)


@router.get("/me", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[models.User, Depends(get_current_active_user)],
):
    return current_user
