from fastapi import FastAPI, Depends, Request, Form,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from fastapi.templating import Jinja2Templates
from models import Vehicle,Brand,Model,Base,Ingreso,DetalleIngreso,Garaje,DetalleGaraje
from config import DATABASE_URL
from fastapi.responses import JSONResponse
from fastapi import Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import starlette.status as status
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import text
from sqlalchemy import exc

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

@app.get("/ingresos/")
def ingresos(request:Request,db: Session = Depends(get_db)):
    vehiculos = db.query(Vehicle).all()
    return templates.TemplateResponse("formingreso.html", {"request": request, "vehiculos":vehiculos})

@app.get('/ingreso_vehiculo/')
async def prueba(dias: str, fechas: str,cantidad: int ,db: Session = Depends(get_db)):

    result = db.execute(text("CALL guardar_ingreso(:dia_entrada,:fecha_entrada,:cantingreso_entrada,@out_id)"),
    {"dia_entrada":dias , "fecha_entrada":fechas ,"cantingreso_entrada":cantidad})
    db.commit()
    out_id = db.execute(text("SELECT @out_id")).fetchone()[0]
    return JSONResponse(content=[{"out_id":out_id}])
    
@app.get('/agregar_ingreso_vehiculo/')
async def agregar_ingreso(idIngreso: int, idVehiculo: int, db: Session = Depends(get_db)):
    detalle = DetalleIngreso(idIngreso = idIngreso, idVehiculo = idVehiculo)
    db.add(detalle)
    db.commit()
    vehiculos = db.query(Vehicle).join(DetalleIngreso).filter(DetalleIngreso.idIngreso == idIngreso)
    vehiculo_dict = [vehiculo.to_dict() for vehiculo in vehiculos]
    return JSONResponse(content=[vehiculo_dict])



@app.get('/listarpordia/')
def listarpordia(request:Request):
    return templates.TemplateResponse("listadopordia.html",{'request':request})

@app.get('/buscar_ingreso/')
async def buscar_ingreso(dia: str,db: Session = Depends(get_db)):
    vehiculos = db.query(Vehicle).join(DetalleIngreso).join(Ingreso).filter(Ingreso.Dia == dia)
    print(vehiculos)
    vehiculo_dict = [vehiculo.to_dict() for vehiculo in vehiculos]
    return JSONResponse(content=[vehiculo_dict])


@app.get('/listarpormodelo/')
def listarpormodelo(request:Request,db: Session = Depends(get_db)):
    marcas = db.query(Brand).all()
    return templates.TemplateResponse("listadopormarca.html",{'request':request,'marcas':marcas})


@app.get('/listar_garajes/')
def listargarajes(request:Request,db: Session = Depends(get_db)):
    garajes = db.query(Garaje).all()
    return templates.TemplateResponse('listargaraje.html',{'request':request,'garajes':garajes})

@app.get('/garajes/')
def garajes(request:Request):
    return templates.TemplateResponse('formgaraje.html',{'request':request})
@app.post('/guardar_garaje/')
def guardar_garaje(request:Request,nombre: str = Form(...),db: Session = Depends(get_db)):
    new = Garaje(nombre = nombre)
    db.add(new)
    db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)
#formulariosss
@app.get("/vehiculos/")
def vehiculos(request:Request,db: Session = Depends(get_db)):
    brands = db.query(Brand).all()
    return templates.TemplateResponse("formvehiculo.html",{"request":request,"brands":brands})
@app.get("/marcas/")
def marcas(request:Request):
    return templates.TemplateResponse("formmarca.html",{"request":request})


@app.get("/modelos/")
def modelos(request:Request,db: Session = Depends(get_db)):
    marca = db.query(Brand).all()
    return templates.TemplateResponse("formmodelo.html",{"request":request,"marca":marca})
@app.get('/busquedaVehiculos/')
async def busquedaVehiculos(request:Request):
    return templates.TemplateResponse("busquedavehiculos.html",{"request":request})

#pedido de datos
@app.get('/obtener_modelos/{id}')
async def obtener_modelos(id:int,db: Session = Depends(get_db)):
    models = db.query(Model).filter_by(idMarcaFk = id).all()
    return JSONResponse(content=[{"idModelo":model.idModelo,"descModelo":model.descModelo} for model in models])


#carga de formularios
@app.post('/cargar_vehiculos/')
async def cargar_vehiculos(request:Request, matricula: str = Form(...),color: str = Form(...),idMarkaFk: int = Form(...), idModeloFk: int=Form(...), image: str = Form(...),db: Session = Depends(get_db)):
    new_v = Vehicle(matricula = matricula,color=color,foto = image,idMarcaFk=idMarkaFk, idModeloFk=idModeloFk)
    db.add(new_v)
    db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)
@app.post('/cargar_marca/')
async def cargar_marca(request:Request, marca: str=Form(...),db: Session = Depends(get_db)):
    new_m = Brand(descMarca=marca)
    db.add(new_m)
    db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)

@app.post('/cargar_modelo/')
async def cargar_modelo(request:Request,modelo: str = Form(...),marca: int = Form(...),db: Session = Depends(get_db)):
    new_md = Model(descModelo=modelo,idMarcaFk=marca)
    db.add(new_md)
    db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)
#listadossss
@app.get('/listar_vehiculos/')
async def listar_vehiculos(request:Request,db: Session = Depends(get_db)):
    vehiculos = db.query(Vehicle).all()
    marca = db.query(Brand).all()
    return templates.TemplateResponse('listarvehiculo.html',{'request':request,"vehiculos":vehiculos,"marca":marca})

@app.get('/listar_modelo/')
async def listar_modelo(request:Request,db: Session = Depends(get_db)):
    modelo = db.query(Model).all()
    marca = db.query(Brand).all()
    return templates.TemplateResponse('listarmodelo.html',{"request":request,"marcas":marca,"modelos":modelo})

@app.get('/listar_marca/')
async def listar_marca(request:Request,db: Session = Depends(get_db)):
    marca = db.query(Brand).all()
    return templates.TemplateResponse('listarmarca.html',{"request":request,"marcas":marca})

#envio formulario editable    
@app.get('/editar_vehiculo/{id}')
async def listar_vehiculo(request:Request,id:int,db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.idVehiculo == id).first()
    brands = db.query(Brand).all()
    models = db.query(Model).filter(Model.idMarcaFk == vehicle.idMarcaFk).all()
    db.close()
    return templates.TemplateResponse("edit_vehicle.html", {"request": request, "vehicle": vehicle, "brands": brands, "models": models})
@app.get('/editar_marca/{id}')
async def editar_modelo(request:Request,id:int,db: Session = Depends(get_db)):
    marca = db.query(Brand).filter(Brand.idMarca == id).first()
    db.close()
    return templates.TemplateResponse("edit_marca.html",{"request":request,"marca":marca})
@app.get('/editar_modelo/{id}')
async def editar_modelo(request:Request,id:int,db: Session = Depends(get_db)):
    modelo = db.query(Model).filter(Model.idModelo == id).first()
    marca = db.query(Brand).all()
    return templates.TemplateResponse('edit_modelo.html',{"request": request, "modelo":modelo,"marca":marca})

 #guardar actualizaciones
@app.post('/update_vehicle/{id}')
async def update_vehicle(request:Request,id:int,matricula: str = Form(...),color: str = Form(...),idMarcaFk: int = Form(...), idModeloFk: int=Form(...), image: str = Form(...),  db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.idVehiculo == id)
    if vehicle:
        vehicle.matricula = matricula
        vehicle.color = color
        vehicle.foto = image
        vehicle.idMarcaFk = idMarcaFk
        vehicle.idModeloFk = idModeloFk
        db.commit()

    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)
@app.post('/update_marca/{id}')
async def update_marca(request:Request,id:int, marca: str = Form(...),  db: Session = Depends(get_db)):
    marca = db.query(Brand).filter(Brand.idMarca == id)
    if marca:
        marca.descMarca = marca
        db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)

@app.post('/update_modelo/{id}')
async def update_modelo(request:Request,id:int, marca: int = Form(...),modelo:str = Form(...)  ,db: Session = Depends(get_db)):
    modelo = db.query(Model).filter(Model.idModelo == id)
    print(id)
    if modelo:
        modelo.descModelo = modelo
        modelo.idMarcaFk = marca
        db.commit()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)


@app.get('/borrar_vehiculo/{id}')
async def borrar_vehiculo(request:Request,id:int,db: Session = Depends(get_db)):
    vehiculo = db.query(Vehicle).filter(Vehicle.idVehiculo == id).first()
    if vehiculo:
        db.delete(vehiculo)
        db.commit()
        db.close()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)

@app.get('/borrar_modelo/{id}')
async def borrar_modelo(request:Request,id:int,db: Session = Depends(get_db)):
    modelo = db.query(Model).filter(Model.idModelo == id).first()
    if modelo:
        db.delete(modelo)
        db.commit()
        db.close()

    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)
@app.get('/borrar_marca/{id}')
async def borrar_marca(request:Request,id:int,db: Session = Depends(get_db)):
    marca = db.query(Brand).filter(Brand.idMarca ==id).first()
    if marca:
        db.delete(marca)
        db.commit()
        db.close()
    return RedirectResponse(
        '/', 
        status_code=status.HTTP_302_FOUND)


@app.get("/vehicles/")
async def read_vehicles(matricula: str = None, marca: str = None, modelo: str = None,color: str = None):
    db = Session(bind=engine)
    query = db.query(Vehicle).options(joinedload(Vehicle.brand), joinedload(Vehicle.model))
    if matricula:
        query = query.filter(Vehicle.matricula.ilike(f"%{matricula}%"))
    if marca:
        query = query.join(Brand).filter(Brand.descMarca.ilike(f"%{marca}%"))
    if modelo:
        query = query.join(Model).filter(Model.descModelo.ilike(f"%{modelo}%"))
    if color:
        query = query.filter(Vehicle.color.ilike(f"%{color}%"))
    vehicles = query.all()
    return vehicles