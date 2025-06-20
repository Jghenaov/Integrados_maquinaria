from config.models import Mantenimiento
from config.db import session


def registrar_mantenimiento(maquinaria_id, tipo_mantenimiento, fecha_inicio, fecha_fin, descripcion, responsable):
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

def get_mantenimiento(maquinaria_id):
    return session.query(Mantenimiento).filter(Mantenimiento.maquinaria_id == maquinaria_id).all()

def update_mantenimiento(id, maquinaria_id, tipo_mantenimiento, fecha_inicio, fecha_fin, descripcion, responsable):
    mantenimiento = session.query(Mantenimiento).get(id)
    if mantenimiento:
        mantenimiento.maquinaria_id = maquinaria_id
        mantenimiento.tipo_mantenimiento = tipo_mantenimiento
        mantenimiento.fecha_inicio = fecha_inicio
        mantenimiento.fecha_fin = fecha_fin
        mantenimiento.descripcion = descripcion
        mantenimiento.responsable = responsable
        session.commit()

def mantenimiento_completado(id):
    mantenimiento = session.query(Mantenimiento).get(id)
    if mantenimiento:
        mantenimiento.estado = "Completado"
        session.commit()

def mantenimiento_en_proceso(id):
    mantenimiento = session.query(Mantenimiento).get(id)
    if mantenimiento:
        mantenimiento.estado = "En Proceso"
        session.commit()
