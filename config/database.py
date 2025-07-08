from config.db import base, engenie
from model import *

def crear_tablas():
    try:
        base.metadata.create_all(engenie)
        return True
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
        return False
