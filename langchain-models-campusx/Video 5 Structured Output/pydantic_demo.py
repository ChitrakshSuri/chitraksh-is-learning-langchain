from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'chitraksh'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5,
                        description='a decimal value representing the cgps of the student')


new_student = {'age': '23', 'email': 'abx'}

student = Student(**new_student)
print(student)
