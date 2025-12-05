from pydantic import BaseModel
from utils.positions import Position
from utils.states import States


class Estadistica(BaseModel):
    goles: int
    asistencias: int
    amarillas: int
    rojas: int


class Jugador(BaseModel):
    id: int
    nombre: str
    edad: int
    posicion: Position
    estado: States
    estadisticas: Estadistica


class Partido(BaseModel):
    id: int
    rival: str
    goles_favor: int
    goles_contra: int
