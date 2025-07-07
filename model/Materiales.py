import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from config.db import base, engenie

class Materiales(base):
    __tablename__ = "materiales"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_material = Column(String(50), nullable=False)
    tipo = Column(String(50), nullable=False)
    unidad_medida = Column(String(50), nullable=False)
    vida_util = Column(Numeric, nullable=False)
    stock_minimo = Column(Numeric, nullable=False)
    stock_actual = Column(Numeric, nullable=False)
    stock_maximo = Column(Numeric, nullable=False)
    proveedor_id = Column(UUID(as_uuid=True),ForeignKey("proveedores.id"),  nullable=False)
    
    proveedor = relationship("Proveedores", back_populates="materiales")
    instalacion_material = relationship("InstalacionMaterial", back_populates="materiales")
    
    def __repr__(self):
        return f"Materiales({self.id}, {self.nombre_material}, {self.tipo}, {self.unidad_medida}, {self.vida_util}, {self.stock_minimo}, {self.stock_actual}, {self.stock_maximo}, {self.proveedor})"
    
