#routes.py
from fastapi import FastAPI
from models import Rectangle, Numbers, Person, Message

app = FastAPI()


@app.get("/")
def read_root():
    return {"project": "AI Chat API", "author": "Zaid"}

@app.get("/status")
def read_status():
    return {"status": "running"}

@app.get("/about")
def read_about():
    return {
    "name": "AI Chat API",
    "version": "1.0"
}

@app.get("/greet")
def read_greet():
    return {
    "message": "Welcome to my API!"
}

@app.get("/greet/{name}")
def read_greet_name(name: str):
    return {
    "message": f"Hello, {name}"
    }

@app.get("/square/{number}")
def read_square(number: int):
    return {
        "number": number,
        "square": number ** 2
    }

@app.get("/add/{num1}/{num2}")
def read_add(num1 : int, num2: int):
    return {
        "num1": num1,
        "num2": num2,
        "sum": num1 + num2
    }

##query parameters

@app.get("/search")
def read_search(name: str):
    return {
        "result" : f"Searching for {name}" 
    }

@app.get("/multiply")
def read_multiply(a: int, b: int):
    return {
        "result": a * b
    }

@app.get("/profile")
def read_profile(name: str, age: int | None = None):
    if age is not None:
        return {
            "name": name,
            "age": age
        }
    return {
        "name": name,
        "age": "Age not provided"
    }

##post request




@app.post("/echo")
def create_message(msg: Message):
    return {
        "message": msg.message
    }


@app.post("/person")
def create_person(person: Person):
    return {
        "message" : f"Hello {person.name}, you are {person.age} years old."
    }



@app.post("/multiply")
def create_multiply(numbers: Numbers):
    return {
        "result": numbers.num1 * numbers.num2
    }



@app.post("/rectangle/area")
def calculate_rectangle_area(rectangle: Rectangle):
    return {
        "area": rectangle.length * rectangle.width
    }