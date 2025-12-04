from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from models import JugadorDB, PartidoDB
from utils.positions import Position
from utils.states import States

app = FastAPI(title="Sigmotoa FC")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# -------- DEPENDENCIA DB --------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- HOME --------
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    jugadores = db.query(JugadorDB).count()
    partidos = db.query(PartidoDB).count()

    goles = db.query(func.sum(JugadorDB.goles)).scalar() or 0
    asistencias = db.query(func.sum(JugadorDB.asistencias)).scalar() or 0

    return templates.TemplateResponse("index.html", {
        "request": request,
        "jugadores": jugadores,
        "partidos": partidos,
        "goles": goles,
        "asistencias": asistencias
    })


# -------- FORMULARIOS --------
@app.get("/form-jugador")
def form_jugador(request: Request):
    return templates.TemplateResponse("form_jugador.html", {
        "request": request,
        "posiciones": list(Position),
        "estados": list(States)
    })

@app.get("/form-partido")
def form_partido(request: Request):
    return templates.TemplateResponse("form_partido.html", {"request": request})


# -------- CREAR JUGADOR --------
@app.post("/crear-jugador")
def crear_jugador(
    nombre: str = Form(...),
    nacionalidad: str = Form(...),
    edad: int = Form(...),
    posicion: str = Form(...),
    estado: str = Form(...),
    ncamiseta: int = Form(0),
    goles: int = Form(0),
    asistencias: int = Form(0),
    db: Session = Depends(get_db)
):
    jugador = JugadorDB(
        nombre=nombre,
        nacionalidad=nacionalidad,
        edad=edad,
        posicion=posicion,
        estado=estado,
        goles=goles,
        asistencias=asistencias
    )

    db.add(jugador)
    db.commit()

    return RedirectResponse("/jugadores", status_code=303)


# -------- CREAR PARTIDO --------
@app.post("/crear-partido")
def crear_partido(
    local: str = Form(...),
    visitante: str = Form(...),
    goles_local: int = Form(...),
    goles_visitante: int = Form(...),
    fecha: str = Form(...),
    db: Session = Depends(get_db)
):
    partido = PartidoDB(
        local=local,
        visitante=visitante,
        goles_local=goles_local,
        goles_visitante=goles_visitante,
        fecha=fecha
    )

    db.add(partido)
    db.commit()

    return RedirectResponse("/partidos", status_code=303)


# -------- LISTAR --------
@app.get("/jugadores")
def ver_jugadores(request: Request, db: Session = Depends(get_db)):
    jugadores = db.query(JugadorDB).all()
    return templates.TemplateResponse("jugadores.html", {
        "request": request,
        "jugadores": jugadores
    })


@app.get("/partidos")
def ver_partidos(request: Request, db: Session = Depends(get_db)):
    partidos = db.query(PartidoDB).all()
    return templates.TemplateResponse("partidos.html", {
        "request": request,
        "partidos": partidos
    })


# -------- ELIMINAR --------
@app.get("/eliminar-jugador/{jugador_id}")
def eliminar_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = db.query(JugadorDB).filter(JugadorDB.id == jugador_id).first()
    if jugador:
        db.delete(jugador)
        db.commit()
    return RedirectResponse("/jugadores", status_code=303)


# -------- API JSON --------
@app.get("/api/jugadores")
def api_jugadores(db: Session = Depends(get_db)):
    return db.query(JugadorDB).all()


@app.get("/api/partidos")
def api_partidos(db: Session = Depends(get_db)):
    return db.query(PartidoDB).all()
