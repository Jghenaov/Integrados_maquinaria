from model.Mantenimiento import Mantenimiento
from model.Maquinaria import Maquinaria
from sqlalchemy.orm import Session
from config.Crud import *
from datetime import datetime


class MantenimientoController:
    
    
    def registrar_mantenimiento(db: Session, maquinaria_id: int, tipo_mantenimiento: str, fecha_inicio: datetime, fecha_fin: datetime, descripcion: str, responsable: str, estado: str = 'Pendiente'):
        crear_mantenimiento = {
            "maquinaria_id": maquinaria_id,
            "tipo_mantenimiento": tipo_mantenimiento,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "descripcion": descripcion,
            "responsable": responsable,
            "estado": estado
        }

        return create(db, Mantenimiento, crear_mantenimiento)
    
    
        