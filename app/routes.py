#routes.py
from fastapi import APIRouter
from models import Rectangle, Numbers, Person, Message
from restaurant_data import restaurant_info
import services.restaurant_service as restaurant_service


router = APIRouter()

@router.get("/")
def read_root():
    return {"project": "AI Chat API", "author": "Zaid"}

@router.get("/status")
def read_status():
    return {"status": "running"}

@router.get("/about")
def read_about():
    return {
    "name": "AI Chat API",
    "version": "1.0"
}

@router.get("/greet")
def read_greet():
    return {
    "message": "Welcome to my API!"
}

@router.get("/greet/{name}")
def read_greet_name(name: str):
    return {
    "message": f"Hello, {name}"
    }

@router.get("/square/{number}")
def read_square(number: int):
    return {
        "number": number,
        "square": number ** 2
    }

@router.get("/add/{num1}/{num2}")
def read_add(num1 : int, num2: int):
    return {
        "num1": num1,
        "num2": num2,
        "sum": num1 + num2
    }

##query parameters

@router.get("/search")
def read_search(name: str):
    return {
        "result" : f"Searching for {name}" 
    }

@router.get("/multiply")
def read_multiply(a: int, b: int):
    return {
        "result": a * b
    }

@router.get("/profile")
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




@router.post("/echo")
def create_message(msg: Message):
    return {
        "message": msg.message
    }


@router.post("/person")
def create_person(person: Person):
    return {
        "message" : f"Hello {person.name}, you are {person.age} years old."
    }



@router.post("/multiply")
def create_multiply(numbers: Numbers):
    return {
        "result": numbers.num1 * numbers.num2
    }



@router.post("/rectangle/area")
def calculate_rectangle_area(rectangle: Rectangle):
    return {
        "area": rectangle.length * rectangle.width
    }


### restaurant ###

@router.get("/restaurant")
def read_restaurant_info():
    return restaurant_service.get_restaurant()    


@router.get("/menu")
def read_menu_item(item: str | None = None):
    return restaurant_service.get_menu(item)


@router.get("/hours")
def read_restaurant_hours():
    return restaurant_service.get_hours()   


@router.get("/location")
def read_restaurant_location():
    return restaurant_service.get_location()

@router.get("/search_menu")
def search_menu_item(item: str):
    return restaurant_service.get_menu(item)

@router.get("/phone")
def read_restaurant_phone():
    return restaurant_service.get_phone()

@router.get("/ask")
def answer_question(question: str):
    return restaurant_service.answer_question(question)
