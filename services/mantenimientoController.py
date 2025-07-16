from model.Mantenimiento import Mantenimiento
from model.Maquinaria import Maquinaria
from sqlalchemy.orm import Session
from config import Crud
from datetime import datetime
from Utils.logs import loggings
from Utils.exceptions import *


class MantenimientoController:
    
    def __init__(self):
        self.log = loggings()
    
    
    def registrar_mantenimiento(self, db: Session, maquinaria_id: int, tipo_mantenimiento: str, fecha_inicio: datetime, fecha_fin: datetime, descripcion: str, responsable: str, estado: str = 'Pendiente'):
        try:
            crear_mantenimiento = {
                "maquinaria_id": maquinaria_id,
                "tipo_mantenimiento": tipo_mantenimiento,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "descripcion": descripcion,
                "responsable": responsable,
                "estado": estado
            }

            self.log.info(f'Mantenimiento creado: {crear_mantenimiento["tipo_mantenimiento"]}')
            
            return Crud.create(db, Mantenimiento, crear_mantenimiento)
        except ErrorDeRegitro as e:
            self.log.error(f"Error: {e}")
        except Exception as e:
            self.log.error(f"Error: {e}")
    
    #Obtener todos los mantenimientos
    def obtener_mantenimientos(self, db: Session):
        try:
            self.log.info("Informacion obtenida de la base de datos")
            return Crud.get_all(db, Mantenimiento)
        
        except RegistroVacioError as e:
            self.log.error(f"Error: {e}")
        except Exception as e:
            self.log.error(f"Error: {e}")
        
    #Actualizar mantenimiento
    def actualizar_mantenimiento(self, db:Session, mantenimiento_id: int, nuevo_dato: dict):
        #controlmantenimiento = MantenimientoController()
        try:
            mantenimiento = self.get_mantenimiento_by_id(db, mantenimiento_id)
            self.log.info(f"Mantenimiento actualizado: {mantenimiento_id}")
            return Crud.update(db, mantenimiento, nuevo_dato)
        
        except RegistroNoEncontradoError as e:
            self.log.error(f"Error: {e}")
        except Exception as e:
            self.log.error(f"Error: {e}")
            
            
    #Eliminar mantenimiento
    def eliminar_mantenimiento(self, db:Session, mantenimiento_id: int):
        #controlmantenimiento = MantenimientoController()
        try:
            mantenimiento = self.get_mantenimiento_by_id(db, mantenimiento_id)
            self.log.info(f"Mantenimiento eliminado: {mantenimiento_id}")
            return Crud.delete(db, mantenimiento)
        except RegistroNoEncontradoError as e:
            self.log.error(f"Error: {e}")
        except  Exception as e:
            self.log.error(f"Error: {e}")
            
            
    #Obtener mantenimiento por id
    def get_mantenimiento_by_id(self, db:Session, mantenimiento_id: int):
        try:
            self.log.info("Informacion obtenida de la base de datos")
            return Crud.get_by_id(db, Mantenimiento, mantenimiento_id)
        except RegistroNoEncontradoError as e:
            self.log.error(f"Error: {e}")
        except Exception as e:
            self.log.error(f"Error: {e}")
    
    
    #Obtener mantenimientos por maquinaria
    def obtener_mantenimientos_maquinaria(self, db:Session, maquinaria_id: int):
        try:
            self.log.info("Informacion obtenida de la base de datos")
            return Crud.get_by_id(db, Maquinaria, maquinaria_id)
        except RegistroNoEncontradoError as e:
            self.log.error(f"Error: {e}")
        except Exception as e:
            self.log.error(f"Error: {e}")
    
    
    #Dar completado al mantenimiento
    def completar_mantenimiento(self, db:Session, mantenimiento_id: int):
        #controlmantenimiento = MantenimientoController()
        try:
            mantenimiento = self.get_mantenimiento_by_id(db, mantenimiento_id)
            if mantenimiento.estado == 'Completado':
                self.log.warning(f"El mantenimiento {mantenimiento_id} ya estaba completado.")
                return mantenimiento
        
            mantenimiento.estado = 'Completado'
            self.log.info(f"Mantenimiento completado: {mantenimiento_id}")
            return Crud.update(db, mantenimiento, {"estado": mantenimiento.estado})
        except RegistroNoEncontradoError as e:
            self.log.error(f"Error: {e}")
        except Exception as e:
            self.log.error(f"Error: {e}")
            
    

    
           