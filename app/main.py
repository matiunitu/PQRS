from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.role_routes import router as role_router
from routes.programa_routes import router as programa_router
from routes.dependencia_routes import router as dependencia_router
from routes.tipospqrs_routes import router as tipospqrs_router
from routes.estado_routes import router as estado_router
from routes.prioridad_routes import router as prioridad_router
from routes.pqrs_routes import router as pqrs_router
from routes.respuesta_routes import router as respuesta_router
from routes.historial_estados_routes import router as historial_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ep-square-flower-aiq3n3y4-pooler.c-4.us-east-1.aws.neon.tech",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(role_router)
app.include_router(programa_router)
app.include_router(dependencia_router)
app.include_router(tipospqrs_router)
app.include_router(estado_router)
app.include_router(prioridad_router)
app.include_router(pqrs_router)
app.include_router(respuesta_router)
app.include_router(historial_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)