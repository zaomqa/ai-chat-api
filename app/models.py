#models.py
from pydantic import BaseModel
class Rectangle(BaseModel):
    length: float
    width: float

class Numbers(BaseModel):
    num1: int
    num2: int

class Person(BaseModel):
    name: str
    age: int

class Message(BaseModel):
    message: str

class Question(BaseModel):
    question: str