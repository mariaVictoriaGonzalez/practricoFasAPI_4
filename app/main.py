from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from models.clientes import (
    Cliente,
)
from routers.clientes import clientes_routers

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.title = "Clientes_db"

app.include_router(clientes_routers, tags=["Clientes"], prefix="/clientes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "https://faculemo.github.io/front",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)