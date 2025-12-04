from sqlalchemy import Column, Integer, String
from database import Base
from datetime import date


class JugadorDB(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    nacionalidad = Column(String)
    edad = Column(Integer)
    num = Column(Integer)

    altura = Column(Integer)
    peso = Column(Integer)
    pie = Column(String)
    posicion = Column(String)
    valormer = Column(Integer)
    estado = Column(String)
    ingreso = Column(Integer)


    goles = Column(Integer, default=0)
    asistencias = Column(Integer, default=0)


class PartidoDB(Base):
    __tablename__ = "partidos"

    id = Column(Integer, primary_key=True, index=True)
    local = Column(String)
    visitante = Column(String)
    goles_local = Column(Integer)
    goles_visitante = Column(Integer)
    fecha = Column(String)
