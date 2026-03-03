from fastapi import APIRouter, HTTPException
from controllers.historial_estados_controller import *
from models.historial_estados_model import HistorialEstados

router = APIRouter()

nuevo_historial = HistorialEstadosController()

@router.post("/create_historial")
async def create_historial(historial: HistorialEstados):
    rpta = nuevo_historial.create_historial(historial)
    return rpta

@router.get("/get_historial/{id_historial}", response_model=HistorialEstados)
async def get_historial(id_historial: int):
    rpta = nuevo_historial.get_historial(id_historial)
    return rpta

@router.get("/get_historiales/")
async def get_historiales():
    rpta = nuevo_historial.get_historiales()
    return rpta