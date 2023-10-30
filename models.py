from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = unnamed
    phone: str
    mail:


