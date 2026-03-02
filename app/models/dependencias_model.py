from pydantic import BaseModel

class Dependencias(BaseModel):
    id_dependencia: int = None
    nombre_dependencia: str
    descripcion: str