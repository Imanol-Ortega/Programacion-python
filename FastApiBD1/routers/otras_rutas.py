from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
router = APIRouter()
# Configura Jinja2
templates = Jinja2Templates(directory="templates")
# Configura las rutas para archivos estáticos
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/vista1/")
async def otros(request: Request):
    return templates.TemplateResponse("vista1.html", {"request": request})


@router.get("/vista3/")
async def otros(request: Request):
    return templates.TemplateResponse("vista3.html", {"request": request})


@router.get("/vista4/")
async def otros(request: Request):
    return templates.TemplateResponse("vista4.html", {"request": request})
