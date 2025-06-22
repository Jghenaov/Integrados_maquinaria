from config.models import Maquinaria
from config.db import session  # Asegúrate de tener esto en tu db.py

class MaquinariaController:
    
    def listar_maquinarias(self):
        try:
            return session.query(Maquinaria).all()
        
        except Exception as e:
            print(f"ERROR: {e}")
    
    def agregar_maquinaria(self, maquinaria):
        try:
            session.add(maquinaria)
            session.commit()
        
        except Exception as e:
            session.rollback()
            print(f"ERROR: {e}")
    
    def eliminar_maquinaria(self, id):
        maquinaria = None
        try:
            maquinaria = session.query(Maquinaria).get(id)
            if maquinaria:
                session.delete(maquinaria)
                session.commit()
            else:
                raise Exception("Maquinaria no encontrada")
            
        except Exception as e:
            session.rollback()  
            print(f"ERROR: {e}")
    
    def actualizar_maquinaria(self, maquinaria_actualizada):
        print(maquinaria_actualizada)
        try:
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
            
        except Exception as e:
            session.rollback()
            print(f"ERROR: {e}")
    
    def obtener_maquinaria(self, id):
        print(id)
        try:
            return session.query(Maquinaria).get(id)
        
        except Exception as e:
            print(f"ERROR: {e}")
    