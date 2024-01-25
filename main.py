from fastapi import FastAPI

from routes import convert

app = FastAPI()

app.include_router(convert.router)

