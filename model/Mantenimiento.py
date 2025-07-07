import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from config.db import base, engenie


class Mantenimiento(base):
    __tablename__ = "mantenimiento"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    maquinaria_id = Column(UUID(as_uuid=True),ForeignKey("maquinaria.id"), nullable=False)
    tipo_mantenimiento = Column(String(50), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    descripcion = Column(Text, nullable=False)
    responsable = Column(String(50), nullable=False)
    estado = Column(String(50), nullable=False)
    
    maquinaria = relationship("Maquinaria", back_populates="mantenimiento")
    
    def __repr__(self):
        return f"Mantenimiento({self.id}, {self.maquinaria_id}, {self.tipo_mantenimiento}, {self.fecha_inicio}, {self.fecha_fin}, {self.descripcion}, {self.responsable}, {self.estado})"
    
