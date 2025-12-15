from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re

class Major(str, Enum):
    informatics = "Информатика"
    economics = "Экономика"
    law = "Право"
    medicine = "Медицина"
    engineering = "Инженерия"
    languages = "Языки"

class Student(BaseModel):
    student_id:int
    phone_number:str = Field(...,description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: date = Field(..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(..., description="Электронная почта студента")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес студента, не более 200 символов")
    enrollment_year: int = Field(..., ge=2002, description="Год поступления должен быть не меньше 2002")
    major: Major = Field(..., description="Специальность студента")
    course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(default=None, max_length=500, description="Дополнительные заметки, не более 500 символов")       