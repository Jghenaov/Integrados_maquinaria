from config.models import Maquinaria
from config.db import session  # Asegúrate de tener esto en tu db.py

class MaquinariaController:
    
    def listar_maquinarias(self):
        return session.query(Maquinaria).all()
    
    def agregar_maquinaria(self, maquinaria):
        session.add(maquinaria)
        session.commit()
    
    def eliminar_maquinaria(self, id):
        maquinaria = session.query(Maquinaria).get(id)
        if maquinaria:
            session.delete(maquinaria)
            session.commit()
    
    def actualizar_maquinaria(self, maquinaria_actualizada):
        maquinaria = session.query(Maquinaria).get(maquinaria_actualizada.id)
        if maquinaria:
            maquinaria.nombre = maquinaria_actualizada.nombre
            maquinaria.tipo = maquinaria_actualizada.tipo
            maquinaria.modelo = maquinaria_actualizada.modelo
            maquinaria.serie = maquinaria_actualizada.serie
            maquinaria.ubicacion = maquinaria_actualizada.ubicacion
            maquinaria.fecha_adquisicion = maquinaria_actualizada.fecha_adquisicion
            maquinaria.estado = maquinaria_actualizada.estado
            session.commit()
    
    def obtener_maquinaria(self, id):
        return session.query(Maquinaria).get(id)
