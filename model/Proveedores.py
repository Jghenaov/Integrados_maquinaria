import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from config.db import base, engenie

class Proveedores(base):
    __tablename__ = "proveedores"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(50), nullable=False)
    direccion = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    
    materiales = relationship("Materiales", back_populates="proveedor")
    
    def __repr__(self):
        return f"Proveedores({self.id}, {self.nombre}, {self.direccion}, {self.telefono}, {self.email})"
    