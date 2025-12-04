from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from models import JugadorDB, PartidoDB


router = APIRouter( tags=["equipo"])
templates = Jinja2Templates(directory="templates")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#  CREAR PARTIDO --------
@router.post("/crear-partido")
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

#  LISTAR --------


@router.get("/partidos")
def ver_partidos(request: Request, db: Session = Depends(get_db)):
    partidos = db.query(PartidoDB).all()
    return templates.TemplateResponse("partidos.html", {
        "request": request,
        "partidos": partidos
    })