import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from config.db import base, engenie

class InstalacionMaterial(base):
    __tablename__ = "instalacion_material"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    materiales_id = Column(UUID(as_uuid=True),ForeignKey("materiales.id"), nullable=False)
    maquinaria_id = Column(UUID(as_uuid=True),ForeignKey("maquinaria.id"), nullable=False)
    cantidad = Column(Numeric, nullable=False)
    fecha_instalacion = Column(Date, nullable=False)
    horas_maquina = Column(Numeric, nullable=False)
    responsable = Column(String(50), nullable=False)
    estado = Column(String(50), nullable=False)
    
    materiales = relationship("Materiales", back_populates="instalacion_material")
    maquinaria = relationship("Maquinaria", back_populates="instalacion_material")
    
    def __repr__(self):
        return f"Instalacion_Material({self.id}, {self.materiales_id}, {self.maquinaria_id}, {self.cantidad}, {self.fecha_instalacion}, {self.responsable}, {self.estado})"

