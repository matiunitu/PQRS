from fastapi import APIRouter, HTTPException
from controllers.role_controller import *
from models.role_model import Role

router = APIRouter()

nuevo_role = RoleController()

@router.post("/create_role")
async def create_role(role: Role):
    rpta = nuevo_role.create_role(role)
    return rpta

@router.get("/get_role/{id_rol}", response_model=Role)
async def get_role(id_rol: int):
    rpta = nuevo_role.get_role(id_rol)
    return rpta

@router.get("/get_roles/")
async def get_roles():
    rpta = nuevo_role.get_roles()
    return rpta