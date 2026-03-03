from fastapi import APIRouter, HTTPException
from controllers.prioridad_controller import *
from models.prioridad_model import Prioridad

router = APIRouter()

nuevo_prioridad = PrioridadController()

@router.post("/create_prioridad")
async def create_prioridad(prioridad: Prioridad):
    rpta = nuevo_prioridad.create_prioridad(prioridad)
    return rpta

@router.get("/get_prioridad/{id_prioridad}", response_model=Prioridad)
async def get_prioridad(id_prioridad: int):
    rpta = nuevo_prioridad.get_prioridad(id_prioridad)
    return rpta

@router.get("/get_prioridades/")
async def get_prioridades():
    rpta = nuevo_prioridad.get_prioridades()
    return rpta