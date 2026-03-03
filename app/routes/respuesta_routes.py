from fastapi import APIRouter, HTTPException
from controllers.respuesta_controller import *
from models.respuesta_model import Respuesta

router = APIRouter()

nuevo_respuesta = RespuestaController()

@router.post("/create_respuesta")
async def create_respuesta(respuesta: Respuesta):
    rpta = nuevo_respuesta.create_respuesta(respuesta)
    return rpta

@router.get("/get_respuesta/{id_respuesta}", response_model=Respuesta)
async def get_respuesta(id_respuesta: int):
    rpta = nuevo_respuesta.get_respuesta(id_respuesta)
    return rpta

@router.get("/get_respuestas/")
async def get_respuestas():
    rpta = nuevo_respuesta.get_respuestas()
    return rpta