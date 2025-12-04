from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal
from models import JugadorDB, PartidoDB
from routers import jugadores, equipos
app = FastAPI(title="Sigmotoa FC")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(jugadores.router)
app.include_router(equipos.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#HOME
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





# jSON
@app.get("/api/jugadores")
def api_jugadores(db: Session = Depends(get_db)):
    return db.query(JugadorDB).all()


@app.get("/api/partidos")
def api_partidos(db: Session = Depends(get_db)):
    return db.query(PartidoDB).all()
