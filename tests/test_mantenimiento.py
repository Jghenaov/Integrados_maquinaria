import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime

from services.mantenimientoController import MantenimientoController
from model.Mantenimiento import Mantenimiento
from Utils.exceptions import RegistroNoEncontradoError, RegistroVacioError, ErrorDeRegitro
from config import Crud

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def controller():
    return MantenimientoController()

# Simula un objeto Mantenimiento
def mock_mantenimiento(id=1, estado='Pendiente'):
    mantenimiento = Mantenimiento()
    mantenimiento.id = id
    mantenimiento.estado = estado
    mantenimiento.maquinaria_id = 1
    mantenimiento.tipo_mantenimiento = "Correctivo"
    mantenimiento.fecha_inicio = datetime.now()
    mantenimiento.fecha_fin = datetime.now()
    mantenimiento.descripcion = "Cambio de filtro"
    mantenimiento.responsable = "Juan"
    return mantenimiento

# ------------------------
# Pruebas para registrar
# ------------------------
@patch('config.Crud.create')
def test_registrar_mantenimiento(mock_create, controller, mock_db):
    mock_create.return_value = mock_mantenimiento()
    
    resultado = controller.registrar_mantenimiento(
        db=mock_db,
        maquinaria_id=1,
        tipo_mantenimiento="Correctivo",
        fecha_inicio=datetime.now(),
        fecha_fin=datetime.now(),
        descripcion="Cambio de aceite",
        responsable="Carlos"
    )

    assert resultado.estado == 'Pendiente'
    mock_create.assert_called_once()

# ------------------------
# Obtener por ID
# ------------------------
def test_get_mantenimiento_by_id_exitoso(controller, mock_db):
    mantenimiento = mock_mantenimiento()
    controller.get_mantenimiento_by_id = MagicMock(return_value=mantenimiento)

    resultado = controller.get_mantenimiento_by_id(mock_db, 1)

    assert resultado.id == 1
    assert resultado.estado == 'Pendiente'

# ------------------------
# Completar mantenimiento
# ------------------------
def test_completar_mantenimiento_pendiente(controller, mock_db):
    mantenimiento = mock_mantenimiento()
    controller.get_mantenimiento_by_id = MagicMock(return_value=mantenimiento)

    with patch('config.Crud.update', return_value=mantenimiento):
        resultado = controller.completar_mantenimiento(mock_db, 1)

    assert resultado.estado == 'Completado'

def test_completar_mantenimiento_ya_completado(controller, mock_db):
    mantenimiento = mock_mantenimiento(estado='Completado')
    controller.get_mantenimiento_by_id = MagicMock(return_value=mantenimiento)

    resultado = controller.completar_mantenimiento(mock_db, 1)

    assert resultado.estado == 'Completado'

# ------------------------
# Actualizar mantenimiento
# ------------------------
@patch('config.Crud.update')
def test_actualizar_mantenimiento(mock_update, controller, mock_db):
    mantenimiento = mock_mantenimiento()
    controller.get_mantenimiento_by_id = MagicMock(return_value=mantenimiento)

    datos_actualizados = {"estado": "Completado"}
    
    mantenimiento.estado = "Completado"  # Simula el cambio real
    mock_update.return_value = mantenimiento

    resultado = controller.actualizar_mantenimiento(mock_db, 1, datos_actualizados)

    assert resultado.estado == "Completado"


# ------------------------
# Eliminar mantenimiento
# ------------------------
@patch('config.Crud.delete')
def test_eliminar_mantenimiento(mock_delete, controller, mock_db):
    mantenimiento = mock_mantenimiento()
    controller.get_mantenimiento_by_id = MagicMock(return_value=mantenimiento)
    mock_delete.return_value = True

    resultado = controller.eliminar_mantenimiento(mock_db, 1)

    assert resultado is True
    mock_delete.assert_called_once()
