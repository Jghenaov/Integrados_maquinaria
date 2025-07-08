#querys con session
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Utils.logs import loggings


log = loggings()
# Funciones para lectura
def get_all(db:Session, model, skip:int = 0, limit:int = 100):
    log.info("Informacion obtenida de la base de datos")
    return db.query(model).offset(skip).limit(limit).all()

def get_by_id(db: Session, model, id:int):
    log.info("Informacion obtenida de la base de datos")
    return db.query(model).filter(model.id == id).first()

def get_by_atribute(db:Session, model, attribute:str, value):
    log.info("Informacion obtenida de la base de datos")
    return db.query(model).filter(getattr(model, attribute) == value).firts()
    

# Funciones para escritura

def create(db: Session, model, data: dict):
    try:
        db_item = model(**data)
        log.info("Informacion creada en la base de datos")
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError as e:
        db.rollback()
        log.error(f"Error: {e}")
        return None
    except Exception as e:
        db.rollback()
        log.error(f"Error: {e}")
        return None
    
def update(db: Session, db_item, update_data: dict):
    try:
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError as e:
        db.rollback()
        log.error(f"Error {db_item.__class__.__name__}: {e}")
        return None
    except Exception as e:
        db.rollback()
        log.error(f"Error {db_item.__class__.__name__}: {e}")
        return None 
    
def delete(db: Session, db_item):
    try:
        db.delete(db_item)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        log.error(f"Error {db_item.__class__.__name__}: {e}")
        return False
    except Exception as e:
        db.rollback()
        log.error(f"Error {db_item.__class__.__name__}: {e}")
        return False
    