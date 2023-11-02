from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from fastapi.templating import Jinja2Templates
from models import Vehicle,Brand,Model,Base
from pydantic import BaseModel
from config import DATABASE_URL
from fastapi.responses import JSONResponse
from fastapi import Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import starlette.status as status

app = FastAPI()
# Configura las rutas para archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
# Incluye otro archivo de rutas
# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
# Agrega esta línea para eliminar las tablas existentes
#Base.metadata.drop_all(bind=engine)

# Luego, usa create_all para crear las tablas según las definiciones de los modelos
#Base.metadata.create_all(bind=engine)

# Configuración de las plantillas de Jinja2
templates = Jinja2Templates(directory="templates")

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def menu(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/vehiculos/")
def vehiculos(request:Request,db: Session = Depends(get_db)):
    brands = db.query(Brand).all()
    return templates.TemplateResponse("formvehiculo.html",{"request":request,"brands":brands})
@app.get("/marcas/")
def marcas(request:Request):
    return templates.TemplateResponse("formmarca.html",{"request":request})
@app.get("/modelos/")
def modelos(request:Request):
    return templates.TemplateResponse("formmodelo.html",{"request":request})


@app.get('/obtener_modelos/{id}')
async def obtener_modelos(request:Request, id:int,db: Session = Depends(get_db)):
    models = db.query(Model).filter_by(idMarcaFk = id).all()
    return JSONResponse(content=[{"idModelo":model.idModelo,"descModelo":model.descModelo} for model in models])



@app.post('/cargar_vehiculos/')
async def cargar_vehiculos(request:Request, matricula: str = Form(...),color: str = Form(...),idMarkaFk: int = Form(...), idModeloFk: int=Form(...), image: str = Form(...),db: Session = Depends(get_db)):
    new_v = Vehicle(matricula = matricula,color=color,foto = image,idMarcaFk=idMarkaFk, idModeloFk=idModeloFk)
    db.add(new_v)
    db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)