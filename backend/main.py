from fastapi import FastAPI
from backend.routers.todo import router as todo_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from backend.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("A iniciar a Base de Dados...")
    init_db() 
    yield
    print("A desligar a API...")

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

app.include_router(todo_router)

