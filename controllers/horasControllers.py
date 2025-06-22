from config.models import RegistroHoras
from config.db import session

def get_horas(id_maquinaria):
    try:        
        horas = session.query(RegistroHoras).filter(RegistroHoras.maquinaria_id == id_maquinaria).all()
        return horas
    
    except Exception as e:
        print(f"ERROR: {e}")

def registrar_horas(id_maquinaria, fecha, horas_maquina, actividad, operador):
    print(id_maquinaria)
    try:
        horas = RegistroHoras(id_maquinaria=id_maquinaria, fecha=fecha, horas_maquina=horas_maquina, actividad=actividad, operador=operador)
        session.add(horas)
        session.commit()
    
    except Exception as e:
        session.rollback()
        print(f"ERROR: {e}")



