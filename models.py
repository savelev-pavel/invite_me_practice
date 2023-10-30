from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int = Field(ge=0, frozen=True)
    # целое число, больше 0, без возможности изменения
    name: str = Field(default='Безымянный', min_length=1, max_length=50)
    # текстовый тип, от 1 до 50 символов, по умолчанию значение: Безымянный
    phone: str = Field(default='', min_length=10, max_length=10, pattern=r'^\d*$')
    # текстовый тип, разрешены только цифры, 10 символов, по умолчанию пустая строка
    email: EmailStr = Field(default='', min_length=3, max_length=50)
    # тип данных строка е-мэйла, от 3 до 50 символов, по умолчанию пустая строка


try:
    user = User(id=-1)
    print(user.model_dump())
except ValueError:
    print
