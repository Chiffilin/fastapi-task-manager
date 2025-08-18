# app/main.py

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import create_tables, engine

# Import the router
from app.routers.tasks import router


# Asynchronous context manager to handle application lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application lifecycle events.
    Executes on startup and shutdown.
    """
    # Actions on startup
    print("Creating tables...")
    create_tables()
    yield
    # Actions on shutdown
    print("Closing database connection...")
    engine.dispose()


app = FastAPI(lifespan=lifespan)

# Include the router
app.include_router(router)
