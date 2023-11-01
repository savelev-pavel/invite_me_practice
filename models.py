from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(ge=0, frozen=True)
    phone: str = Field(default='', min_length=10, max_length=10, pattern=r'^\d*$')
    name: str = Field(default='Безымянный', min_length=1, max_length=50)


if __name__ == '__main__':
    try:
        user = User(id=1)
        print(user)
    except ValueError:
        pass
