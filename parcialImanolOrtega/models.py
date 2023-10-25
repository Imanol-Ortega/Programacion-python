from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Text

Base = declarative_base()

class DatosParcial(Base):
    __tablename__ = 'DatosParcial'

    Id = Column(Integer, primary_key=True, index=True)
    Dato = Column(String(50))
    Detalle = Column(String(50))
    ValordelCombo = Column(String(50))