"""Parsers and serializers for /auth API endpoints."""
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    disabled: bool

    class Config:
        orm_mode = True
