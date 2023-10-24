from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from fastapi.templating import Jinja2Templates
from models import Pais, Base, Ciudad, Barrio
from pydantic import BaseModel
from config import DATABASE_URL
from fastapi.responses import JSONResponse
from fastapi import Form

app = FastAPI()

# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
# Agrega esta línea para eliminar las tablas existentes
# Base.metadata.drop_all(bind=engine)

# Luego, usa create_all para crear las tablas según las definiciones de los modelos
# Base.metadata.create_all(bind=engine)

# Configuración de las plantillas de Jinja2
templates = Jinja2Templates(directory="templates")

# Función para obtener la sesión de la base de datos


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def cargar_raiz(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/paises")
def paises(request: Request, db: Session = Depends(get_db)):
    paises = db.query(Pais).all()
    return templates.TemplateResponse("paises.html", {"request": request, "paises": paises})


@app.get("/ciudades")
def ciudades(request: Request, db: Session = Depends(get_db)):
    ciudad = db.query(Ciudad).all()
    paises = db.query(Pais).all()
    return templates.TemplateResponse("ciudades.html", {"request": request, "ciudad": ciudad, "paises": paises})


@app.get("/barrios")
def barrios(request: Request, db: Session = Depends(get_db)):
    barrio = db.query(Barrio).all()
    ciudad = db.query(Ciudad).all()
    return templates.TemplateResponse("barrios.html", {"request": request, "barrio": barrio, "ciudad": ciudad})


@app.post("/agregar_barrio/")
def agregar_barrio(request: Request, nombre_barrio: str = Form(...), id_ciudad: int = Form(...), db: Session = Depends(get_db)):
    barrio = Barrio(NombreBarrio=nombre_barrio, IdCiudad=id_ciudad)
    db.add(barrio)
    db.commit()
    barrio = db.query(Barrio).all()
    ciudades = db.query(Ciudad).all()
    return templates.TemplateResponse("barrios.html", {"request": request, "barrio": barrio, "ciudad": ciudades})


@app.post("/agregar_ciudad/")
def agregar_ciudad(request: Request, nombre_ciudad: str = Form(...), id_pais: int = Form(...), db: Session = Depends(get_db)):
    ciudad = Ciudad(NombreCiudad=nombre_ciudad, IdPais=id_pais)
    db.add(ciudad)
    db.commit()
    ciudades = db.query(Ciudad).all()
    paises = db.query(Pais).all()
    return templates.TemplateResponse("ciudades.html", {"request": request, "ciudad": ciudades, "paises": paises})


@app.post("/agregar_pais/")
def agregar_pais(request: Request, nombre_pais: str = Form(...), db: Session = Depends(get_db)):
    pais = Pais(NombrePais=nombre_pais)
    db.add(pais)
    db.commit()
    paises = db.query(Pais).all()
    return templates.TemplateResponse("paises.html", {"request": request, "paises": paises})


@app.get("/borrar_barrio/{barrio_id}")
def borrar_barrio(request: Request, barrio_id: int, db: Session = Depends(get_db)):
    barrios = db.query(Barrio).filter(Barrio.IdBarrio == barrio_id).first()
    if barrios:
        db.delete(barrios)
        db.commit()
        barrio = db.query(Barrio).all()
        ciudades = db.query(Ciudad).all()
        return templates.TemplateResponse("barrios.html", {"request": request, "barrio": barrio, "ciudad": ciudades})
    return HTTPException(status_code=404, detail="barrio no encontrado")


@app.get("/borrar_ciudad/{ciudad_id}")
def borrar_ciudad(request: Request, ciudad_id: int, db: Session = Depends(get_db)):
    ciudades = db.query(Ciudad).filter(Ciudad.IdCiudad == ciudad_id).first()
    if ciudades:
        db.delete(ciudades)
        db.commit()
        ciudades = db.query(Ciudad).all()
        paises = db.query(Pais).all()
        return templates.TemplateResponse("ciudades.html", {"request": request, "ciudad": ciudades, "paises": paises})
    return HTTPException(status_code=404, detail="ciudad no encontrada")


@app.get("/borrar_pais/{pais_id}")
def borrar_barrio(request: Request, pais_id: int, db: Session = Depends(get_db)):
    paises = db.query(Pais).filter(Pais.IdPais == pais_id).first()
    if paises:
        db.delete(paises)
        db.commit()
        paises = db.query(Pais).all()
        return templates.TemplateResponse("paises.html", {"request": request, "paises": paises})
    return HTTPException(status_code=404, detail="PAIS no encontrada")


@app.get("/editar_barrio/{barrio_id}")
def editar_barrio(request: Request, barrio_id: int, db: Session = Depends(get_db)):
    barrios = db.query(Barrio).filter(Barrio.IdBarrio == barrio_id).first()
    ciudades = db.query(Ciudad).all()
    return templates.TemplateResponse("barrios2.html", {"request": request, "barrio": barrios, "ciudad": ciudades})


@app.get("/editar_ciudad/{ciudad_id}")
def editar_ciudad(request: Request, ciudad_id: int, db: Session = Depends(get_db)):
    ciudad = db.query(Ciudad).filter(Ciudad.IdCiudad == ciudad_id).first()
    paises = db.query(Pais).all()
    return templates.TemplateResponse("ciudades2.html", {"request": request, "ciudad": ciudad, "paises": paises})


@app.get("/editar_pais/{pais_id}")
def editar_pais(request: Request, pais_id: int, db: Session = Depends(get_db)):
    paises = db.query(Pais).filter(Pais.IdPais == pais_id).first()
    return templates.TemplateResponse("paises2.html", {"request": request, "paises": paises})


@app.post("/guardar_edicion_barrio/{barrio_id}")
def guardar_edicion_barrio(request: Request, barrio_id: int, nombre_barrio: str = Form(...), id_ciudad: int = Form(...), db: Session = Depends(get_db)):
    barrio = db.query(Barrio).filter(Barrio.IdBarrio == barrio_id)
    if barrio:
        barrio.NombreBarrio = nombre_barrio
        barrio.IdCiudad = id_ciudad
        db.commit()
        return {"message": "hola"}
    return HTTPException(status_code=404, detail="barrio no encontrada")
