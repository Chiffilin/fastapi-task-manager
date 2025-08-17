# app/main.py

from fastapi import FastAPI

from app.db.database import create_tables
from app.routers.tasks import router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    Creates the database tables when the application starts up.
    """
    create_tables()


app.include_router(router)
