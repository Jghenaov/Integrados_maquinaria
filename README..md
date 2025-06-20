# 🛠️ Sistema de Gestión de Operación y Mantenimiento de Maquinarias

Este proyecto es una aplicación backend desarrollada en Python que permite registrar, consultar y gestionar:
- Operación de maquinaria pesada
- Registro de horas máquina y horas hombre
- Mantenimiento preventivo y correctivo
- Control de repuestos y materiales
- Instalación y seguimiento de componentes
- Proveedores de materiales

Toda la interacción es inicialmente por línea de comandos (terminal), y está diseñado para ser **modular, escalable** y **preparado para una futura interfaz gráfica o API REST**.

---

## 📌 Objetivos del Proyecto

1. Registrar y consultar datos de maquinaria, mantenimientos, materiales y proveedores.
2. Registrar horas máquina/hombre para control operativo.
3. Controlar instalación de materiales por maquinaria y su vida útil en horas.
4. Gestionar inventario (stock mínimo, actual y máximo).
5. Generar alertas simples desde CLI (por ejemplo: “stock mínimo alcanzado”).

---

## 📂 Estructura del Proyecto

maquinaria_backend/
│
├── app/
│ ├── models/ # Modelos SQLAlchemy (ORM)
│ ├── services/ # Lógica CRUD y reglas de negocio
│ ├── cli/ # Menús interactivos por terminal
│ ├── db/ # Conexión y configuración de base de datos
│ └── utils/ # Funciones auxiliares (validaciones, alertas, formatos)
│
├── tests/ # Pruebas unitarias (pytest recomendado)
├── config.py # Configuración del proyecto (BD, parámetros generales)
├── run.py # Archivo principal para iniciar el sistema desde terminal
├── requirements.txt # Dependencias del entorno
└── README.md # Documentación general



---

## 🔧 Tecnologías recomendadas

- **Lenguaje**: Python 3.10 o superior
- **Base de datos**: PostgreSQL o MySQL
- **ORM**: SQLAlchemy
- **CLI**: Python `cmd`, `argparse` o menús manuales con input()
- **Entorno virtual**: `venv` o `poetry` para manejar dependencias
- **Pruebas**: Pytest

---

## ✅ Paso a paso para desarrollar el proyecto

### 1. Configurar entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


