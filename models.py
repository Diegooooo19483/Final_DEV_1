from sqlalchemy import Column, Integer, String
from database import Base


class JugadorDB(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)
    posicion = Column(String)
    estado = Column(String)

    # 🟢 ESTADÍSTICAS
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
