from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    password: str
    email: str

class LoginUserData(BaseModel):
    email: str
    password: str

