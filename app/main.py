#main.py
from fastapi import FastAPI
from routes import router


app = FastAPI()

# plugs

app.include_router(router)