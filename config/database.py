from config.db import base, engenie
from model import *

def crear_tablas():
    base.metadata.create_all(engenie)