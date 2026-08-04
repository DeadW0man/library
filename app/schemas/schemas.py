from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class Register(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

class UserCreate(BaseModel):
    pass
class UserLogin(BaseModel):
    pass

class Book(BaseModel):
    id: int
    title: str
    author: str
    release_year: int
    owner_id: int

class Share(BaseModel):
    id: int
    book_id: int
    giver_id: int
    taker_id: int
    final_date: str

class Session(BaseModel):
    session_id: int
    user_id: int

