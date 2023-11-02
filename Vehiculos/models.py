from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Text

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
    foto = Column(String(245))
    idMarcaFk = Column(Integer, ForeignKey('brands.idMarca'))
    idModeloFk = Column(Integer, ForeignKey('models.idModelo'))
    brand = relationship("Brand")
    model = relationship("Model")