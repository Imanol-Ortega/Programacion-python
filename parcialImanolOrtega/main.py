from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from fastapi.templating import Jinja2Templates
from models import DatosParcial,Base
from pydantic import BaseModel
from config import DATABASE_URL
from fastapi.responses import JSONResponse
from fastapi import Form
from fastapi.staticfiles import StaticFiles
from routers import otras_rutas
from fastapi.responses import RedirectResponse
import starlette.status as status

app = FastAPI()
# Configura las rutas para archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
# Incluye otro archivo de rutas
app.include_router(otras_rutas.router, prefix="/vistas")
# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
# Agrega esta línea para eliminar las tablas existentes
# Base.metadata.drop_all(bind=engine)

# Luego, usa create_all para crear las tablas según las definiciones de los modelos
#Base.metadata.create_all(bind=engine)

# Configuración de las plantillas de Jinja2
templates = Jinja2Templates(directory="templates")

# Función para obtener la sesión de la base de datos

# Configura Jinja2


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def menu(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})
@app.post("/guardar/")
def cargar_datos(request:Request,dato: str = Form(...),valor_combo: str = Form(...),detalle: str = Form(...),db: Session = Depends(get_db)):
    datos_parcial = DatosParcial(Dato = dato,Detalle = detalle,ValordelCombo = valor_combo)
    db.add(datos_parcial)
    db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)
@app.get("/obtener")
def obtener_datos(request:Request,db: Session = Depends(get_db)):
    datos_parcial = db.query(DatosParcial).all()
    return templates.TemplateResponse("listar.html",{"request":request,"datos_parcial":datos_parcial})

@app.get("/borrar/{dato_id}")
def borrar(request:Request,dato_id:int,db: Session = Depends(get_db)):
    parcial = db.query(DatosParcial).filter(DatosParcial.Id == dato_id).first()
    if parcial:
        db.delete(parcial)
        db.commit()
        return RedirectResponse('/obtener',status_code=status.HTTP_302_FOUND)
    return HTTPException(status_code=404, detail="a")