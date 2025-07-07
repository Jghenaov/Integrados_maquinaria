import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from config.db import base, engenie

class RegistroHoras(base):
    __tablename__ = "registro_horas"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    maquinaria_id = Column(UUID(as_uuid=True),ForeignKey("maquinaria.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    horas_maquina = Column(Numeric, nullable=False)
    actividad = Column(String(50), nullable=False)
    operador = Column(String(50), nullable=False)
    
    maquinaria = relationship("Maquinaria", back_populates="registro_horas")
    
    def __repr__(self):
        return f"RegistroHoras({self.id}, {self.maquinaria_id}, {self.fecha}, {self.horas_maquina}, {self.horas_hombre}, {self.operador})"   
    