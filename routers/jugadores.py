from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal
from models import JugadorDB, PartidoDB
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from models import JugadorDB, PartidoDB
from utils.positions import Position
from utils.states import States

router = APIRouter( tags=["Jugador"])


templates = Jinja2Templates(directory="templates")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# FORMs
@router.get("/form-jugador")
def form_jugador(request: Request):
    return templates.TemplateResponse("form_jugador.html", {
        "request": request,
        "posiciones": list(Position),
        "estados": list(States)
    })

@router.get("/form-partido")
def form_partido(request: Request):
    return templates.TemplateResponse("form_partido.html", {"request": request})


# CREAR JUGADOR
@router.post("/crear-jugador")
def crear_jugador(
    nombre: str = Form(...),
    nacionalidad: str = Form(...),
    edad: int = Form(...),
    posicion: str = Form(...),
    estado: str = Form(...),
    altura: float = Form(...),
    goles: int = Form(0),
    peso: int = Form(0),
    pie: str = Form(...),
    valormer: int = Form(0),
    asistencias: int = Form(0),
    db: Session = Depends(get_db)
):
    jugador = JugadorDB(

        nombre=nombre,
        nacionalidad=nacionalidad,
        edad=edad,


        peso=peso,
        altura=altura,
        pie=pie,
        posicion=posicion,
        valormer=valormer,
        estado=estado,
        goles=goles,
        asistencias=asistencias
    )

    db.add(jugador)
    db.commit()

    return RedirectResponse("/jugadores", status_code=303)

#  LISTAR -
@router.get("/jugadores")
def ver_jugadores(request: Request, db: Session = Depends(get_db)):
    jugadores = db.query(JugadorDB).all()
    return templates.TemplateResponse("jugadores.html", {
        "request": request,
        "jugadores": jugadores
    })

@router.get("/eliminar-jugador/{jugador_id}")
def eliminar_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = db.query(JugadorDB).filter(JugadorDB.id == jugador_id).first()
    if jugador:
        db.delete(jugador)
        db.commit()
    return RedirectResponse("/jugadores", status_code=303)
