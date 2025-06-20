from config.models import RegistroHoras
from config.db import session

def get_horas(id_maquinaria):
    horas = session.query(RegistroHoras).filter(RegistroHoras.maquinaria_id == id_maquinaria).all()
    return horas

def registrar_horas(id_maquinaria, fecha, horas_maquina, operador):
    horas = RegistroHoras(id_maquinaria=id_maquinaria, fecha=fecha, horas_maquina=horas_maquina, operador=operador)
    session.add(horas)
    session.commit()



