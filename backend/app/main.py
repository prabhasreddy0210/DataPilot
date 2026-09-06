from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.database import router as database_router
from app.routes.query import router as query_router


app = FastAPI(
    title="DataPilot",
    description="AI-powered SQL analytics assistant",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(database_router)
app.include_router(query_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to DataPilot!"
    }