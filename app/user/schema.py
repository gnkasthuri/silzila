from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    uid: str

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    uid: str
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
