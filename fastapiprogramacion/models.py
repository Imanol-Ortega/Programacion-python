from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Text

Base = declarative_base()


class Pais(Base):
    __tablename__ = 'Pais'

    IdPais = Column(Integer, primary_key=True, index=True)
    NombrePais = Column(String(50))
    PobPais = Column(Integer)
    Curiosidades = Column(Text)
    ciudades = relationship("Ciudad", backref="pais")


class Barrio(Base):
    __tablename__ = "Barrios"
    IdBarrio = Column(Integer, primary_key=True, index=True)
    NombreBarrio = Column(String(50), index=True)
    IdCiudad = Column(Integer, ForeignKey("ciudades.IdCiudad"))


class Ciudad(Base):
    __tablename__ = "ciudades"
    IdCiudad = Column(Integer, primary_key=True, index=True)
    NombreCiudad = Column(String(50), index=True)
    IdPais = Column(Integer, ForeignKey("Pais.IdPais"))
    barrios = relationship("Barrio", backref="ciudades")
