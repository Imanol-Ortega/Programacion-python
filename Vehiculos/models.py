from sqlalchemy import Column, Integer, String, ForeignKey,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Text
from sqlalchemy.dialects.mysql import LONGTEXT

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'
    idMarca = Column(Integer, primary_key=True, index=True)
    descMarca = Column(String(50), unique=True, index=True)
    models = relationship("Model", back_populates="brand")

class Model(Base):
    __tablename__ = 'models'
    idModelo = Column(Integer, primary_key=True, index=True)
    descModelo = Column(String(50), unique=True, index=True)
    idMarcaFk = Column(Integer, ForeignKey('brands.idMarca'))
    brand = relationship("Brand", back_populates="models")
    vehicles = relationship("Vehicle", back_populates="model")

class Vehicle(Base):
    __tablename__ = 'vehicles'
    idVehiculo = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(50), unique=True, index=True)
    color = Column(String(50))
    foto = Column(LONGTEXT)
    idMarcaFk = Column(Integer, ForeignKey('brands.idMarca'))
    idModeloFk = Column(Integer, ForeignKey('models.idModelo'))
    brand = relationship("Brand")
    model = relationship("Model")
    ingreso = relationship('Ingreso', secondary='detalleingreso')

class Ingreso(Base):
    __tablename__ = 'ingresos'
    idIngreso = Column(Integer, primary_key=True, index=True)
    Dia = Column(String(50), index=True)
    Fecha = Column(Date)
    CantIngreso = Column(Integer)
    vehiculo = relationship('Vehicle', secondary='detalleingreso')


class DetalleIngreso(Base):
    __tablename__ = 'detalleingreso'
    idIngreso = Column(Integer,ForeignKey('ingresos.idIngreso'), primary_key=True )
    idVehiculo = Column(Integer, ForeignKey('vehicles.idVehiculo'),primary_key=True, )

