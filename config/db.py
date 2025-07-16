from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()


dialect = os.getenv("DB_DIALECT")
driver = os.getenv("DB_DRIVER")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")


DB_URL = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"


engenie = create_engine(DB_URL)
base = declarative_base()
Session = sessionmaker(bind=engenie)
session = Session()

import model

try:
    engenie.connect()
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")