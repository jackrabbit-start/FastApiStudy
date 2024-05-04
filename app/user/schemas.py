from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes: True


class AuthToken(BaseModel):
    access_token: str
    token_type: str


class UserInDB(User):
    hashed_password: str


class TokenData(BaseModel):
    username: str | None = None
