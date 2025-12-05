SIGMOTOA FC - FASTAPI PROJECT
CLONAR PROYECTO DESDE GITHUB

Comando general:

git clone https://github.com/USUARIO/REPOSITORIO.git

cd REPOSITORIO

Ejemplo real:

git clone https://github.com/Diegooooo19483/Final_DEV_1.git

cd Final_DEV_1

CREAR ENTORNO VIRTUAL
WINDOWS

Crear entorno virtual:

python -m venv venv

Activar:

CMD:
venv\Scripts\activate

PowerShell:
venv\Scripts\Activate.ps1

LINUX / MAC

Crear entorno virtual:

python3 -m venv venv

Activar:

source venv/bin/activate

INSTALAR DEPENDENCIAS

Si tienes requirements.txt:

pip install -r requirements.txt

Si no:

pip install fastapi uvicorn jinja2

EJECUTAR PROYECTO FASTAPI

uvicorn main:app --reload

ABRIR EN NAVEGADOR

Proyecto:

http://127.0.0.1:8000

Documentación FastAPI:

http://127.0.0.1:8000/docs

DETENER SERVIDOR

CTRL + C

DESACTIVAR ENTORNO VIRTUAL

deactivate

COMANDOS IMPORTANTES DE GIT

Ver estado:

git status

Agregar archivos:

git add .

Guardar cambios:

git commit -m "mensaje del commit"

Subir cambios:

git push origin main

SOLUCIÓN DE ERRORES

Python no reconocido:

py -m venv venv

Error PowerShell:

Set-ExecutionPolicy Unrestricted -Scope Process

DESPLIEGUE EN RENDER

Build Command:

pip install -r requirements.txt

Run Command:

uvicorn main:app --host 0.0.0.0 --port 10000
