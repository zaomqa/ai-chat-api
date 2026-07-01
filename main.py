from fastapi import FastAPI

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