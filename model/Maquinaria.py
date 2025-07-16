import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from model.RegistroHoras import RegistroHoras
from config.db import base, engenie



class Maquinaria(base):
    __tablename__ = "maquinaria"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(50), nullable=False)
    tipo = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    serie = Column(String(50), nullable=False)
    ubicacion = Column(String(50), nullable=False)
    fecha_adquisicion = Column(Date, nullable=False)
    estado = Column(String(50), nullable=False)
    
    registro_horas = relationship("RegistroHoras", back_populates="maquinaria")
    mantenimiento = relationship("Mantenimiento", back_populates="maquinaria")
    instalacion_material = relationship("InstalacionMaterial", back_populates="maquinaria")
    
    def __repr__(self):
        return f"Maquinaria({self.id}, {self.nombre}, {self.tipo}, {self.modelo}, {self.serie}, {self.ubicacion}, {self.fecha_adquisicion}, {self.estado})"
    
