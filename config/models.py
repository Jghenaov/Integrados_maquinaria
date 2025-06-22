import uuid
from sqlalchemy import Column, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
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


base.metadata.create_all(engenie) 