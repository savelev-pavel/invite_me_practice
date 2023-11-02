from pydantic import BaseModel, Field
from enum import Enum


class Countries(Enum):
    Russia = 'Russia'


class User(BaseModel):
    id: int = Field(ge=0, frozen=True)
    country: Countries
    phone: str = Field(default='0000000000', min_length=10, max_length=10, pattern=r'^\d*$')
    name: str = Field(default='Безымянный', min_length=1, max_length=50)
