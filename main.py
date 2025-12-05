from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models import Jugador, Partido, Estadistica
from utils.states import States
from utils.positions import Position

app = FastAPI(title="Sigmotoa FC")

templates = Jinja2Templates(directory="templates")

jugadores = []
partidos = []


# ------------------
# WEB
# ------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "jugadores": len(jugadores),
        "partidos": len(partidos)
    })


@app.get("/jugadores", response_class=HTMLResponse)
def ver_jugadores(request: Request):
    return templates.TemplateResponse("jugadores.html", {
        "request": request,
        "jugadores": jugadores
    })


@app.get("/partidos", response_class=HTMLResponse)
def ver_partidos(request: Request):
    return templates.TemplateResponse("partidos.html", {
        "request": request,
        "partidos": partidos
    })


# ------------------
# FORMULARIOS
# ------------------

@app.get("/form-jugador", response_class=HTMLResponse)
def form_jugador(request: Request):
    return templates.TemplateResponse("form_jugador.html", {
        "request": request,
        "posiciones": Position,
        "estados": States
    })


@app.post("/form-jugador")
def crear_jugador_form(
    nombre: str = Form(...),
    edad: int = Form(...),
    posicion: Position = Form(...),
    estado: States = Form(...),
    goles: int = Form(...),
    asistencias: int = Form(...),
    amarillas: int = Form(...),
    rojas: int = Form(...)
):
    nuevo = Jugador(
        id=len(jugadores)+1,
        nombre=nombre,
        edad=edad,
        posicion=posicion,
        estado=estado,
        estadisticas=Estadistica(
            goles=goles,
            asistencias=asistencias,
            amarillas=amarillas,
            rojas=rojas
        )
    )

    jugadores.append(nuevo)
    return RedirectResponse("/jugadores", status_code=303)


@app.get("/form-partido", response_class=HTMLResponse)
def form_partido(request: Request):
    return templates.TemplateResponse("form_partido.html", {"request": request})


@app.post("/form-partido")
def crear_partido_form(
    rival: str = Form(...),
    goles_favor: int = Form(...),
    goles_contra: int = Form(...)
):
    nuevo = Partido(
        id=len(partidos)+1,
        rival=rival,
        goles_favor=goles_favor,
        goles_contra=goles_contra
    )

    partidos.append(nuevo)
    return RedirectResponse("/partidos", status_code=303)
