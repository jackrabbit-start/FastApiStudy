from fastapi import APIRouter, Depends, HTTPException
from . import models, schemas, services
from sqlalchemy.orm import Session
from ..dependencies import get_db

router = APIRouter(
    prefix="/item",
    tags=["item"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Item)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    user_id: int = 1,
):
    print(item)
    return services.create_user_item(db, item, user_id)
