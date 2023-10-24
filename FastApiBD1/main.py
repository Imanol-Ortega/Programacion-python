from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import otras_rutas
app = FastAPI()
# Configura las rutas para archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
# Incluye otro archivo de rutas
app.include_router(otras_rutas.router, prefix="/vistas")
# Configura Jinja2
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse("vista3.html", {"request": request})


@app.post("/calcular/")
async def calcular(request: Request, num1: float = Form(...), num2: float =
                   Form(...), op: str = Form(...)):
    res = None
    if op == "s":
        res = num1 + num2
    elif op == "r":
        res = num1 - num2
    elif op == "m":
        res = num1 * num2
    elif op == "d":
        if num2 != 0:
            res = num1 / num2
    return templates.TemplateResponse("vista2.html", {"request": request, "num1": num1, "num2": num2, "op": op, "res": res})
