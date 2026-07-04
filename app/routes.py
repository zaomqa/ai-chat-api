#routes.py
from fastapi import APIRouter
from models import Rectangle, Numbers, Person, Message
from restaurant_data import restaurant_info


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
def read_restaurant():
        return restaurant_info


@router.get("/menu")
def read_menu(item : str | None = None):
    if item is not None:
        price = restaurant_info["menu"].get(item)
        if price is not None:
            return {
                "item": item,
                "price": price
            }
        else:
            return {
                "error": "404 Not Found",
                "message": f"Item '{item}' not found in the menu."
            }
    return restaurant_info["menu"]

@router.get("/hours")
def read_hours():
    return {
        "hours": restaurant_info["hours"]
    }

@router.get("/location")
def read_location():
    return {
        "location": restaurant_info["location"]
    }
       