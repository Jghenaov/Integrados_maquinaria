from model.Maquinaria import Maquinaria
from sqlalchemy.orm import Session
from config.Crud import create, get_all, get_by_id, update, delete
from Utils.logs import loggings
from Utils.exceptions import *
from datetime import datetime

class MaquinariaController:
    def __init__(self):
        self.log = loggings()
    
    def obtener_maquinaria(self, db:Session):
        try:
            return get_all(db, Maquinaria)
        except Exception as e:
            self.log.error(f"Error: {e}")
            
            
    
    def crear_maquinaria(self, db:Session, nombre: str, tipo: str, modelo: str, serie: str, ubicacion: str, fecha_adquisicion: datetime, estado: str):
        try:
                        
            equipo_data = {
                "nombre": nombre,
                "tipo": tipo,
                "modelo": modelo,
                "serie": serie,
                "ubicacion": ubicacion,
                "fecha_adquisicion": fecha_adquisicion.date(),
                "estado": estado
            }
            self.log.info(f'Equipo creado: {equipo_data["nombre"]}')
            return create(db, Maquinaria, equipo_data)
        except Exception as e:
            self.log.error(f"Error: {e}")
            
    # Obtener maquinaria por ID      
    def get_maquinaria_by_id(self, db:Session, maquinaria_id: int):
        try:
            return get_by_id(db, Maquinaria, maquinaria_id)
        except Exception as e:
            self.log.error(f"Error: {e}")
    
    # Actualizar maquinaria por id        
    def actualizar_maquinaria(self, db:Session, maquinaria_id: int, nuevo_dato: dict):
        controlmaquinaria = MaquinariaController()
        try:
            maquinaria = controlmaquinaria.get_maquinaria_by_id(db, maquinaria_id)
            return update(db, maquinaria, nuevo_dato)
        except Exception as e:
            self.log.error(f"Error: {e}")
            
    # Eliminar maquinaria por id
    def eliminar_maquinaria(self, db:Session, maquinaria_id: int):
        controlmaquinaria = MaquinariaController()
        try:
            maquinaria = controlmaquinaria.get_maquinaria_by_id(db, maquinaria_id)
            if maquinaria is None:
                raise MaterialNoEncontradoError(maquinaria_id)
            
            return delete(db, maquinaria)
        except Exception as e:
            self.log.error(f"Error: {e}")