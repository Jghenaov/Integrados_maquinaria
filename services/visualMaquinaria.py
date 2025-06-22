from controllers.maquinariaControl import MaquinariaController
from controllers import mantenimientoController
from controllers import horasControllers
from prettytable import PrettyTable
from config.models import Maquinaria
from datetime import datetime
import uuid

class VisualMaquinaria:
    def __init__(self):
        self.maquinaria = MaquinariaController()
        

    def mostrar(self):
        try:
            maquinarias = self.maquinaria.listar_maquinarias()
            if maquinarias:
                table = PrettyTable()
                table.field_names = ["ID", "Nombre", "Tipo", "Modelo", "Serie", "Ubicación", "Fecha Adquisición", "Estado"]
                for m in maquinarias:
                    table.add_row([m.id, m.nombre, m.tipo, m.modelo, m.serie, m.ubicacion, m.fecha_adquisicion, m.estado])
                    print(table)
            else:
                print("No hay maquinaria registrada.")

        except Exception as e:
            print(f"ERROR: {e}")
    
    
    
    def mostrar_menu(self):
        while True:
            print('\nMenu Principal')
            print('1. Maquinaria')
            print('2. Mantenimiento')
            print('3. Horas')
            print('4. Salir')

            opcion = input('Seleccione una opción: ')

            if opcion == '1':
                self.menu_maquinaria()
            elif opcion == '2':
                self.menu_mantenimiento()
            elif opcion == '3':
                self.menu_horas()     
            elif opcion == '4':
                print('Saliendo del sistema...')
                break
            else:
                print('Opción no válida.')
                
                
    def menu_horas(self):
        visual = VisualMaquinaria()
        
        while True:
            print('\nGestión de Horas')
            print('1. Ver horas por maquinaria')
            print('2. Agregar horas')
            print('3. Volver')
            
            opcion_horas = input('Seleccione una opcion: ')
            
            if opcion_horas == '1':
                try:
                    maquinaria_id = input("ID de la maquinaria: ")
                    horas = horasControllers.get_horas(maquinaria_id)
                    if horas:
                        table = PrettyTable()
                        table.field_names = ["ID", "Fecha", "Horas Máquina", "Operador"]
                        for h in horas:
                            table.add_row([h.id, h.fecha, h.horas_maquina, h.operador])
                        print(table)
                    else:
                        print("No hay horas registradas para esta maquinaria.")

                except Exception as e:
                    print(f"ERROR: {e}")
                    
            elif opcion_horas == '2':
                try:
                    maquinaria_id = input("ID maquinaria: ")
                    fecha = datetime.strptime(input("Fecha (YYYY-MM-DD): "), "%Y-%m-%d")
                    horas_maquina = input("Horas Máquina: ")
                    actividad = input("Actividad realizada: ")
                    operador = input("Operador: ")
                    horasControllers.registrar_horas(maquinaria_id, fecha, horas_maquina, actividad, operador)
                    input("Horas registradas. Presione Enter para continuar...")
                    
                except Exception as e:
                    print(f"ERROR: {e}")
                
            elif opcion_horas == '3':
                visual.mostrar_menu()
                
            else:
                print('Opción no válida.')
    
    

    def menu_maquinaria(self):
        visual = VisualMaquinaria()
        
        while True:
            print('\nGestión de Maquinaria')
            print('1. Ver maquinaria')
            print('2. Agregar maquinaria')
            print('3. Eliminar maquinaria')
            print('4. Actualizar maquinaria')
            print('5. Volver')

            opcion = input('Seleccione una opción: ')

            if opcion == '1':
                try:
                    visual.mostrar()
                except Exception as e:
                    print(f"ERROR: {e}")
                

            elif opcion == '2':
                try:
                    id = uuid.uuid4()
                    nombre = input("Nombre: ")
                    tipo = input("Tipo: ")
                    modelo = input("Modelo: ")
                    serie = input("Serie: ")
                    ubicacion = input("Ubicación: ")
                    fecha_adquisicion = datetime.strptime(input("Fecha de adquisición (YYYY-MM-DD): "), "%Y-%m-%d")
                    estado = input("Estado: ")

                    nueva = Maquinaria(id=id, nombre=nombre, tipo=tipo, modelo=modelo, serie=serie,
                                    ubicacion=ubicacion, fecha_adquisicion=fecha_adquisicion, estado=estado)
                    self.maquinaria.agregar_maquinaria(nueva)
                    input("Maquinaria agregada. Presione Enter para continuar...")

                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '3':
                try:
                    visual.mostrar()
                    id = input("ID de la maquinaria a eliminar: ")
                    if not self.maquinaria.obtener_maquinaria(id):
                        raise Exception("Maquinaria no encontrada.")                    
                    self.maquinaria.eliminar_maquinaria(id)
                    input("Maquinaria eliminada. Presione Enter para continuar...")

                except Exception as e:
                    print(f"ERROR: {e}")    

            elif opcion == '4':
                try:
                    id = input("ID de la maquinaria: ")
                    nombre = input("Nombre: ")
                    tipo = input("Tipo: ")
                    modelo = input("Modelo: ")
                    serie = input("Serie: ")
                    ubicacion = input("Ubicación: ")
                    fecha_adquisicion = datetime.strptime(input("Fecha de adquisición (YYYY-MM-DD): "), "%Y-%m-%d")
                    estado = input("Estado: ")

                    actualizada = Maquinaria(id=id, nombre=nombre, tipo=tipo, modelo=modelo, serie=serie,
                                            ubicacion=ubicacion, fecha_adquisicion=fecha_adquisicion, estado=estado)
                    self.maquinaria.actualizar_maquinaria(actualizada)
                    input("Maquinaria actualizada. Presione Enter para continuar...")

                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '5':
                visual.mostrar_menu()

            else:
                print("Opción no válida.")

    def menu_mantenimiento(self):
        visual = VisualMaquinaria()
        
        while True:
            print('\nGestión de Mantenimiento')
            print('1. Ver mantenimiento por maquinaria')
            print('2. Agregar mantenimiento')
            print('3. Eliminar mantenimiento')
            print('4. Actualizar mantenimiento')
            print('5. Marcar como Completado')
            print('6. Marcar como En Proceso')
            print('7. Volver')

            opcion = input('Seleccione una opción: ')

            if opcion == '1':
                try:
                    visual.mostrar()
                    maquinaria_id = input("ID de la maquinaria: ")
                    mantenimientos = mantenimientoController.get_mantenimiento(maquinaria_id)
                    if mantenimientos:
                        table = PrettyTable()
                        table.field_names = ["ID", "Tipo", "Fecha Inicio", "Fecha Fin", "Descripción", "Responsable", "Estado"]
                        for m in mantenimientos:
                            table.add_row([m.id, m.tipo_mantenimiento, m.fecha_inicio, m.fecha_fin, m.descripcion, m.responsable, m.estado])
                        print(table)
                    else:
                        print("No hay mantenimiento registrado para esta maquinaria.")

                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '2':
                try:
                    visual.mostrar()
                    maquinaria_id = input("ID maquinaria: ")
                    tipo = input("Tipo de mantenimiento (Preventivo o Correctivo): ")
                    if tipo not in ["Preventivo", "Correctivo"]:
                        raise ValueError ("Tipo de mantenimiento no valido.")
                        return
                    fecha_inicio = datetime.strptime(input("Fecha inicio (YYYY-MM-DD): "), "%Y-%m-%d")
                    fecha_fin = datetime.strptime(input("Fecha fin (YYYY-MM-DD): "), "%Y-%m-%d")
                    descripcion = input("Descripción: ")
                    responsable = input("Responsable: ")
                    mantenimientoController.registrar_mantenimiento(maquinaria_id, tipo, fecha_inicio, fecha_fin, descripcion, responsable)
                    input("Mantenimiento registrado. Presione Enter para continuar...")

                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '3':
                try:
                    id_mantenimiento = input("ID del mantenimiento a eliminar: ")
                    mantenimientoController.eliminar_mantenimiento(id_mantenimiento)
                    input("Mantenimiento eliminado. Presione Enter para continuar...")

                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '4':
                try:
                    id_mantenimiento = input("ID del mantenimiento: ")
                    maquinaria_id = input("ID maquinaria: ")
                    tipo = input("Tipo: ")
                    fecha_inicio = datetime.strptime(input("Fecha inicio (YYYY-MM-DD): "), "%Y-%m-%d")
                    fecha_fin = datetime.strptime(input("Fecha fin (YYYY-MM-DD): "), "%Y-%m-%d")
                    descripcion = input("Descripción: ")
                    responsable = input("Responsable: ")
                    mantenimientoController.update_mantenimiento(id_mantenimiento, maquinaria_id, tipo, fecha_inicio, fecha_fin, descripcion, responsable)
                    input("Mantenimiento actualizado. Presione Enter para continuar...")

                except Exception as e:
                    print(f"ERROR: {e}")
                    
                    
            elif opcion == '5':
                try:
                    id_mantenimiento = input("ID del mantenimiento: ")
                    mantenimientoController.mantenimiento_completado(id_mantenimiento)
                    input("Estado actualizado a Completado. Presione Enter para continuar...")
                    
                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '6':
                try:
                        id_mantenimiento = input("ID del mantenimiento: ")
                        mantenimientoController.mantenimiento_en_proceso(id_mantenimiento)
                        input("Estado actualizado a En Proceso. Presione Enter para continuar...")
                        
                except Exception as e:
                    print(f"ERROR: {e}")

            elif opcion == '7':
                visual.mostrar_menu()

            else:
                print("Opción no válida.")


       

