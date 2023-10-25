from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()
# Configura Jinja2
templates = Jinja2Templates(directory="templates")
# Configura las rutas para archivos estáticos
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/cargar/")
async def otros(request: Request):
    return templates.TemplateResponse("cargar.html", {"request": request})


@router.get("/listar/")
async def otros(request: Request):
    return templates.TemplateResponse("listar.html", {"request": request})



