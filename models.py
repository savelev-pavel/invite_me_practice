from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int = Field(ge=0, frozen=True)
    name: str = Field(default='Безымянный', min_length=1, max_length=50)
    phone: str = Field(default='', min_length=10, max_length=10, pattern=r'^\d*$')
    email: EmailStr = Field(default='', min_length=3, max_length=50)


user = User(id=1, name='П')
print(user.model_dump())