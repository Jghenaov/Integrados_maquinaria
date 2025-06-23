from config.models import Mantenimiento
from config.db import session


def registrar_mantenimiento(maquinaria_id, tipo_mantenimiento, fecha_inicio, fecha_fin, descripcion, responsable):
    try:
        mantenimiento = Mantenimiento(
            maquinaria_id=maquinaria_id,
            tipo_mantenimiento=tipo_mantenimiento,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            descripcion=descripcion,
            responsable=responsable,
            estado="En Proceso"  
        )
        session.add(mantenimiento)
        session.commit()
        
    except Exception as e:
        session.rollback()
        print(f"ERROR: {e}")


def get_mantenimiento(maquinaria_id):
    try:
        return session.query(Mantenimiento).filter(Mantenimiento.maquinaria_id == maquinaria_id).all()
    
    except Exception as e:
        print(f"ERROR: {e}")
   
        
def update_mantenimiento(id, maquinaria_id, tipo_mantenimiento, fecha_inicio, fecha_fin, descripcion, responsable):
    try:
        mantenimiento = session.query(Mantenimiento).get(id)
        if mantenimiento:
            mantenimiento.maquinaria_id = maquinaria_id
            mantenimiento.tipo_mantenimiento = tipo_mantenimiento
            mantenimiento.fecha_inicio = fecha_inicio
            mantenimiento.fecha_fin = fecha_fin
            mantenimiento.descripcion = descripcion
            mantenimiento.responsable = responsable
            session.commit()
            
    except Exception as e:
        session.rollback()
        print(f"ERROR: {e}")



def mantenimiento_completado(id):
    try:
        mantenimiento = session.query(Mantenimiento).get(id)
        if mantenimiento:
            mantenimiento.estado = "Completado"
            session.commit()
            
    except Exception as e:
        print(f"ERROR: {e}")

def mantenimiento_en_proceso(id):
    try:
        mantenimiento = session.query(Mantenimiento).get(id)
        if mantenimiento:
            mantenimiento.estado = "En Proceso"
            session.commit()

    except Exception as e:
        print(f"ERROR: {e}")
        
# mostrar todos los mantenimientos realizados
def mostrar_mantenimientos():
    try:
        mantenimientos = session.query(Mantenimiento).all()
        return mantenimientos

    except Exception as e:
        print(f"ERROR: {e}")