from typing import Annotated

from fastapi import Depends, HTTPException

from ..dependencies import get_db
from app.user import models
from sqlalchemy.orm import Session
from app.user.services import get_current_user
from app.database import oauth2_scheme


async def get_current_active_user(
    token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)
):
    user = await get_current_user(db, token)
    if not user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user
