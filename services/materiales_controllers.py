from config.models import Materiales
from config.db import session


class MaterialesController:
    def __init__(self):
        self.model = Materiales
        
        
        
    # Registro de materiales
    def register_material(self, nombre_material, tipo, unidad_medida, vida_util, stock_minimo, stock_actual, stock_maximo, proveedor_id):
        try:    
            material = Materiales(
                nombre_material=nombre_material,
                tipo=tipo,
                unidad_medida=unidad_medida,
                vida_util=vida_util,
                stock_minimo=stock_minimo,
                stock_actual=stock_actual,
                stock_maximo=stock_maximo,
                proveedor_id=proveedor_id
            )
            
            session.add(material)
            session.commit()
            return "Material registrado exitosamente"
        
        
        
        except Exception as e:
            session.rollback()
            print(f"ERROR: {e}")
    
    def salidas_materiales(self, material_id, cantidad):
        try:
            material = session.get(self.model, material_id)

            if material is None:
                raise ValueError(f"No se encontró el material con ID {material_id}")

            material.stock_actual -= cantidad
            session.commit()
            return "Salida de materiales realizada exitosamente"

        except Exception as e:
            session.rollback()
            print(f"ERROR: {e}")
            return f"Error: {e}"
