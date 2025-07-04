from config.models import RegistroHoras
from config.db import session

def get_horas(maquinaria_id):
    try:        
        horas = session.query(RegistroHoras).filter(RegistroHoras.maquinaria_id == maquinaria_id).all()
        return horas
    
    except Exception as e:
        print(f"ERROR: {e}")

def registrar_horas(maquinaria_id, fecha, horas_maquina, actividad, operador):
    try:
        horas = RegistroHoras(maquinaria_id=maquinaria_id , fecha=fecha, horas_maquina=horas_maquina, actividad=actividad, operador=operador)
        if not horas:
            raise Exception("Horas no registradas, algunos de los parametros no son correctos.")
        session.add(horas)
        session.commit()
    
    except Exception as e:
        session.rollback()
        print(f"ERROR: {e}")



