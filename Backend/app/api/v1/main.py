from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app:FastAPI):
    """
    Application lifecycle manager.

    Startup:
        Initialize resources required by the application.

    Shutdown:
        Gracefully release resources before exiting.
    """
    print("Application is starting......")
    
    yield
    
    print("Application is shutdown.........")
app=FastAPI()

@app.get("/")

async def root():
    return{"msg":"success"}