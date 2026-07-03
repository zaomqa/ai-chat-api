#main.py
from fastapi import FastAPI
from pydantic import BaseModel
from routes import app as routes_app

app = FastAPI()

# plugs

app.include_router(routes_app)