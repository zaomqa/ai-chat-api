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
