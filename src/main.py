from fastapi import FastAPI
from src.routers.todo import router as todo_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("A iniciar a Base de Dados...")
    init_db() 
    yield
    print("A desligar a API...")

app = FastAPI()

app.include_router(todo_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers=["*"]
)
