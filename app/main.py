from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.clientes import clientes_routers
from routers.servicio import servicio_routers


app = FastAPI()
app.title = "Clientes_db"

app.include_router(clientes_routers, tags=["Clientes"], prefix="/clientes")
app.include_router(servicio_routers, tags=["Servicio"], prefix="/servicio")

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
