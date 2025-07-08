
class ProyectoError(Exception):
    pass


class MaterialNoEncontradoError(ProyectoError):
    def __init__(self, material_id):
        self.message = f"Error: El material con ID {material_id} no fue encontrado."
        super().__init__(self.message)


class StockInsuficienteError(ProyectoError):
    def __init__(self, stock_actual, cantidad_requerida):
        self.message = (
            f"Error: Stock insuficiente. Disponible: {stock_actual}, Requerido: {cantidad_requerida}."
        )
        super().__init__(self.message)


class ErrorDeBaseDeDatos(ProyectoError):
    def __init__(self, detalle="Error desconocido en la base de datos."):
        self.message = f"Error en la base de datos: {detalle}"
        super().__init__(self.message)


class EntradaInvalidaError(ProyectoError):
    def __init__(self, campo, valor):
        self.message = f"Entrada invalida: el campo '{campo}' recibio un valor no permitido: '{valor}'."
        super().__init__(self.message)


class OperacionNoPermitidaError(ProyectoError):
    def __init__(self, detalle="Operacion no permitida en el sistema."):
        self.message = detalle
        super().__init__(self.message)
        

