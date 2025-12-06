from tkinter import *
from tkinter import messagebox
from controller import controlador_1

class View:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Notas System")
        ventana.geometry("800x700")
        ventana.resizable(True, True)
        self.menu_principal(ventana)

    @staticmethod
    def borrar_pantalla(ventana):
        for w in ventana.winfo_children():
            w.destroy()
    
    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Menu principal", justify="center")
        lbl_titulo.pack(pady=5)

        btn_autos = Button(ventana, text="1.- Autos", command=lambda: View.menu_acciones(ventana, "Autos"))
        btn_autos.pack(pady=5)

        btn_camionetas = Button(ventana, text="2.- Camionetas", command=lambda: View.menu_acciones(ventana, "Camionetas"))
        btn_camionetas.pack(pady=5)

        btn_camiones = Button(ventana, text="3.- Camiones", command=lambda: View.menu_acciones(ventana, "Camiones"))
        btn_camiones.pack(pady=5)

        btn_salir = Button(ventana, text="4.- Salir", command=ventana.quit)
        btn_salir.pack(pady=5)

    @staticmethod
    def menu_acciones(ventana, opcion=""):
        View.borrar_pantalla(ventana)
        if opcion == "Autos":
            lbl_titulo = Label(ventana, text=f"...::: MENU DE {opcion} :::...")
            lbl_titulo.pack(pady=5)

            btn_insertar = Button(ventana, text="1.- Insertar", command=lambda: View.insertar_autos(ventana))
            btn_insertar.pack(pady=5)

            btn_consultar = Button(ventana, text="2.- Consultar", command=lambda: View.consultar_autos(ventana))
            btn_consultar.pack(pady=5)

            btn_actualizar = Button(ventana, text="3.- Actualizar", command=lambda: View.modificar_autos_id(ventana))
            btn_actualizar.pack(pady=5)
        
            btn_eliminar = Button(ventana, text="4.- Eliminar", command=lambda: View.eliminar_autos(ventana))
            btn_eliminar.pack(pady=5)

            btn_regresar = Button(ventana, text="5.- Regresar", command=lambda: View.menu_principal(ventana))
            btn_regresar.pack(pady=5)

        elif opcion == "Camionetas":
            lbl_titulo = Label(ventana, text=f"...::: MENU DE {opcion} :::...")
            lbl_titulo.pack(pady=5)

            btn_insertar = Button(ventana, text="1.- Insertar", command=lambda: View.insertar_camionetas(ventana))
            btn_insertar.pack(pady=5)

            btn_consultar = Button(ventana, text="2.- Consultar", command=lambda: View.consultar_camionetas(ventana))
            btn_consultar.pack(pady=5)

            btn_actualizar = Button(ventana, text="3.- Actualizar", command=lambda: View.modificar_camionetas_id(ventana))
            btn_actualizar.pack(pady=5)
        
            btn_eliminar = Button(ventana, text="4.- Eliminar", command=lambda: View.eliminar_camionetas(ventana))
            btn_eliminar.pack(pady=5)

            btn_regresar = Button(ventana, text="5.- Regresar", command=lambda: View.menu_principal(ventana))
            btn_regresar.pack(pady=5)
            
        elif opcion == "Camiones":
            lbl_titulo = Label(ventana, text=f"...::: MENU DE {opcion} :::...")
            lbl_titulo.pack(pady=5)

            btn_insertar = Button(ventana, text="1.- Insertar", command=lambda: View.insertar_camiones(ventana))
            btn_insertar.pack(pady=5)

            btn_consultar = Button(ventana, text="2.- Consultar", command=lambda: View.consultar_camiones(ventana))
            btn_consultar.pack(pady=5)

            btn_actualizar = Button(ventana, text="3.- Actualizar", command=lambda: View.modificar_camiones_id(ventana))
            btn_actualizar.pack(pady=5)
        
            btn_eliminar = Button(ventana, text="4.- Eliminar", command=lambda: View.eliminar_camiones(ventana))
            btn_eliminar.pack(pady=5)

            btn_regresar = Button(ventana, text="5.- Regresar", command=lambda: View.menu_principal(ventana))
            btn_regresar.pack(pady=5)
    
    @staticmethod
    def insertar_autos(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Ingrese los datos del vehiculo tipo Auto", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_marca = Label(ventana, text="Marca: ")
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana, width=15, justify="center")
        entry_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Color: ")
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana, width=15, justify="center")
        entry_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Modelo: ")
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana, width=15, justify="center")
        entry_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Velocidad: ")
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana, width=15, justify="center")
        entry_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Potencia: ")
        lbl_potencia.pack(pady=5)
        entry_potencia = Entry(ventana, width=15, justify="center")
        entry_potencia.pack(pady=5)

        lbl_plazas = Label(ventana, text="No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, justify="center")
        entry_plazas.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command=lambda: controlador_1.Controlador.insertar_auto(entry_marca.get(), entry_color.get(),
                                                                                           entry_modelo.get(), entry_velocidad.get(),
                                                                                           entry_potencia.get(), entry_plazas.get()))
        btn_guardar.pack(pady=5)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "Autos"))
        btn_regresar.pack(pady=5)

    @staticmethod
    def consultar_autos(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Aqui se muestran los registros de Autos: ", justify="center")
        lbl_titulo.pack(pady=5)

        filas = ""
        registros = controlador_1.Controlador.mostrar_autos()
        if len(registros) == 0:
            messagebox.showerror(message="No existen registros en la BD")
        for f in registros:
            filas += f"ID: {f[0]}\n Marca: {f[1]}\n Color: {f[2]}\n Modelo: {f[3]}\n Velocidad: {f[4]}\n Potencia: {f[5]}\n Plazas: {f[-1]}\n\n"
        lbl_notas = Label(ventana, text=f"{filas}")
        lbl_notas.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Autos"))
        btn_volver.pack(pady=5)

    @staticmethod
    def modificar_autos_id(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Vamos a modificar una entrada de Autos: ", justify="center")
        lbl_titulo.pack(pady=5)

        id_auto = IntVar()

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID del Auto a modificar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        entry_titulo_2 = Entry(ventana, width=15, textvariable=id_auto, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_buscar = Button(ventana, text="Buscar", command=lambda: controlador_1.Controlador.revisar_id(ventana, id_auto.get()))
        btn_buscar.pack(pady=5)
        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Autos"))
        btn_volver.pack(pady=5)
    
    @staticmethod
    def modificar_auto(ventana, registro):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f"Modificar un auto", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_id = Label(ventana,text="ID de la operacion (No editable)")
        lbl_id.pack(pady=5)

        n_marca = StringVar(value=registro[1])
        n_color = StringVar(value=registro[2])
        n_modelo = IntVar(value=registro[3])
        n_velocidad = IntVar(value=registro[4])
        n_potencia = IntVar(value=registro[5])
        n_plazas = IntVar(value=registro[6])

        id_valor = registro[0]
        id_var = IntVar(value=id_valor)
        entry_id = Entry(ventana, textvariable=id_var, width=10, justify="center", state="readonly")
        entry_id.pack(pady=5)

        lbl_marca = Label(ventana, text="Nueva Marca: ")
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana, width=15, textvariable=n_marca, justify="center")
        entry_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Nuevo Color: ")
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana, width=15, textvariable=n_color, justify="center")
        entry_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Nuevo Modelo: ")
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana, width=15, textvariable=n_modelo, justify="center")
        entry_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Nueva Velocidad: ")
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana, width=15, textvariable=n_velocidad, justify="center")
        entry_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Nueva Potencia: ")
        lbl_potencia.pack(pady=5)
        entry_potencia = Entry(ventana, width=15, textvariable=n_potencia, justify="center")
        entry_potencia.pack(pady=5)

        lbl_plazas = Label(ventana, text="No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, textvariable=n_plazas, justify="center")
        entry_plazas.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command=lambda: controlador_1.Controlador.enviar_actualizacion(n_marca.get(), n_color.get(), n_modelo.get(), n_velocidad.get(), n_potencia.get(), n_plazas.get(), id_var.get()))
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.modificar_autos_id(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def eliminar_autos(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Vamos a eliminar una entrada de Autos: ", justify="center")
        lbl_titulo.pack(pady=5)

        id_auto = IntVar()

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID del Auto a eliminar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        entry_titulo_2 = Entry(ventana, textvariable=id_auto, width=15, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_eliminar = Button(ventana, text="Eliminar", command=lambda:"")
        btn_eliminar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Autos"))
        btn_volver.pack(pady=5)
    
    #CAMIONETAS
    @staticmethod 
    def insertar_camionetas(ventana):

        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Ingrese los datos del vehiculo tipo Camioneta", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_marca = Label(ventana, text="Marca: ")
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana, width=15, justify="center")
        entry_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Color: ")
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana, width=15, justify="center")
        entry_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Modelo: ")
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana, width=15, justify="center")
        entry_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Velocidad: ")
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana, width=15, justify="center")
        entry_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Potencia: ")
        lbl_potencia.pack(pady=5)
        entry_potencia = Entry(ventana, width=15, justify="center")
        entry_potencia.pack(pady=5)

        lbl_plazas = Label(ventana, text="No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, justify="center")
        entry_plazas.pack(pady=5)

        lbl_traccion = Label(ventana, text="Traccion: ")
        lbl_traccion.pack(pady=5)
        entry_traccion = Entry(ventana, width=15, justify="center")
        entry_traccion.pack(pady=5)

        lbl_cerrada = Label(ventana, text="Es Cerrada?: ")
        lbl_cerrada.pack(pady=5)
        entry_cerrada = Entry(ventana, width=15, justify="center")
        entry_cerrada.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command=lambda: controlador_1.Controlador.insertar_camioneta(
            entry_marca.get(), entry_color.get(), entry_modelo.get(), 
            entry_velocidad.get(), entry_potencia.get(), entry_plazas.get(),
            entry_traccion.get(), entry_cerrada.get()
        ))
        btn_guardar.pack(pady=5)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "Camionetas"))
        btn_regresar.pack(pady=5)

    @staticmethod
    def consultar_camionetas(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Aqui se muestran los registros de Camionetas: ", justify="center")
        lbl_titulo.pack(pady=5)

        filas = ""
        registros = controlador_1.Controlador.mostrar_camionetas()
        if len(registros) == 0:
            messagebox.showerror(message="No existen registros en la BD")
        for f in registros:
            filas += f"ID: {f[0]}\n Marca: {f[1]}\n Color: {f[2]}\n Modelo: {f[3]}\n Velocidad: {f[4]}\n Potencia: {f[5]}\n Plazas: {f[-1]}\n Traccion: {f[5]}\n Cerrada: {f[-1]}\n\n"
        lbl_notas = Label(ventana, text=f"{filas}")
        lbl_notas.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Camionetas"))
        btn_volver.pack(pady=5)

    @staticmethod
    def modificar_camionetas_id(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Vamos a modificar una entrada de Camionetas: ", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID del Auto a modificar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        entry_titulo_2 = Entry(ventana, width=15, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_buscar = Button(ventana, text="Buscar", command=lambda: controlador_1.Controlador.revisar_id_camioneta(ventana, entry_titulo_2.get())) # OJO: entry_titulo_2 o la variable IntVar que uses
        btn_buscar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Camionetas"))
        btn_volver.pack(pady=5)


    @staticmethod
    def modificar_camioneta(ventana, registro):
        View.borrar_pantalla(ventana)
        lbl_titulo = Label(ventana, text=f"Modificar Camioneta", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_id = Label(ventana,text="ID de la operacion (No editable)")
        lbl_id.pack(pady=5)

        n_marca = StringVar(value=registro[1])
        n_color = StringVar(value=registro[2])
        n_modelo = IntVar(value=registro[3])
        n_velocidad = IntVar(value=registro[4])
        n_potencia = IntVar(value=registro[5])
        n_plazas = IntVar(value=registro[6])
        n_traccion = StringVar(value=registro[7])
        n_cerrada = StringVar(value=str(registro[8]))

        id_valor = registro[0]
        id_var = IntVar(value=id_valor)
        
        entry_id = Entry(ventana, textvariable=id_var, width=10, justify="center", state="readonly")
        entry_id.pack(pady=5)

        lbl_marca = Label(ventana, text="Nueva Marca: ")
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana, width=15, textvariable=n_marca, justify="center")
        entry_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Nuevo Color: ")
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana, width=15, justify="center")
        entry_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Nuevo Modelo: ")
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana, width=15, justify="center")
        entry_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Nueva Velocidad: ")
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana, width=15, justify="center")
        entry_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Nueva Potencia: ")
        lbl_potencia.pack(pady=5)
        entry_potencia = Entry(ventana, width=15, justify="center")
        entry_potencia.pack(pady=5)

        lbl_plazas = Label(ventana, text="Nuevo No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, justify="center")
        entry_plazas.pack(pady=5)

        lbl_traccion = Label(ventana, text="Traccion: ")
        lbl_traccion.pack(pady=5)
        entry_traccion = Entry(ventana, width=15, justify="center")
        entry_traccion.pack(pady=5)

        lbl_cerrada = Label(ventana, text="Cerrada: ")
        lbl_cerrada.pack(pady=5)
        entry_cerrada = Entry(ventana, width=15, justify="center")
        entry_cerrada.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar Cambios", command=lambda: controlador_1.Controlador.enviar_actualizacion_camioneta(
            n_marca.get(), n_color.get(), n_modelo.get(), n_velocidad.get(), 
            n_potencia.get(), n_plazas.get(), n_traccion.get(), n_cerrada.get(), id_valor
        ))
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.modificar_camionetas_id(ventana))
        btn_volver.pack(pady=5)



    
    @staticmethod
    def eliminar_camionetas(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Vamos a eliminar una entrada de Camionetas: ", justify="center")
        lbl_titulo.pack(pady=5)

        id_auto = IntVar()

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID de la Camioneta a eliminar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        entry_titulo_2 = Entry(ventana, textvariable=id_auto, width=15, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_eliminar = Button(ventana, text="Eliminar Registro", bg="red", fg="white", command=lambda: controlador_1.Controlador.eliminar_camioneta(id_auto.get())) # Asegúrate que id_auto es tu variable IntVar
        btn_eliminar.pack(pady=5)

        btn_buscar = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Camionetas"))
        btn_buscar.pack(pady=5)

    #CAMIONES 
    @staticmethod
    def insertar_camiones(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Ingrese los datos del vehiculo tipo Camiones", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_marca = Label(ventana, text="Marca: ")
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana, width=15, justify="center")
        entry_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Color: ")
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana, width=15, justify="center")
        entry_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Modelo: ")
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana, width=15, justify="center")
        entry_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Velocidad: ")
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana, width=15, justify="center")
        entry_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Potencia: ")
        lbl_potencia.pack(pady=5)
        entry_potencia = Entry(ventana, width=15, justify="center")
        entry_potencia.pack(pady=5)

        lbl_plazas = Label(ventana, text="No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, justify="center")
        entry_plazas.pack(pady=5)

        lbl_eje = Label(ventana, text="Eje: ")
        lbl_eje.pack(pady=5)
        entry_eje = Entry(ventana, width=15, justify="center")
        entry_eje.pack(pady=5)

        lbl_capacidad = Label(ventana, text="Capacidad de Carga: ")
        lbl_capacidad.pack(pady=5)
        entry_capacidad = Entry(ventana, width=15, justify="center")
        entry_capacidad.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command=lambda: controlador_1.Controlador.insertar_camion(
            entry_marca.get(), entry_color.get(), entry_modelo.get(), 
            entry_velocidad.get(), entry_potencia.get(), entry_plazas.get(),
            entry_eje.get(), entry_capacidad.get()
        ))
        btn_guardar.pack(pady=5)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "Camiones"))
        btn_regresar.pack(pady=5)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_acciones(ventana, "Camiones"))
        btn_regresar.pack(pady=5)
    
    @staticmethod
    def consultar_camiones(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Aqui se muestran los registros de Camiones: ", justify="center")
        lbl_titulo.pack(pady=5)

        filas = ""
        registros = controlador_1.Controlador.mostrar_camiones()
        if len(registros) == 0:
            messagebox.showerror(message="No existen registros en la BD")
        for f in registros:
            filas += f"ID: {f[0]}\n Marca: {f[1]}\n Color: {f[2]}\n Modelo: {f[3]}\n Velocidad: {f[4]}\n Potencia: {f[5]}\n Plazas: {f[6]}\n Eje: {f[7]}\n Capacidad Carga: {f[-1]}\n\n"
        lbl_notas = Label(ventana, text=f"{filas}")
        lbl_notas.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Camiones"))
        btn_volver.pack(pady=5)

    @staticmethod
    def modificar_camiones_id(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Vamos a modificar una entrada de Camiones: ", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID del Camion a modificar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        id_camion = IntVar()
        entry_titulo_2 = Entry(ventana, width=15, textvariable=id_camion, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_buscar = Button(ventana, text="Buscar", command=lambda: controlador_1.Controlador.revisar_id_camion(ventana, id_camion.get()))
        btn_buscar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Camiones"))
        btn_volver.pack(pady=5)

    @staticmethod
    def modificar_camion(ventana, registro):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f"Modificar un Camion", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_id = Label(ventana,text="ID de la operacion (No editable)")
        lbl_id.pack(pady=5)

        n_marca = StringVar(registro[1])
        n_color = StringVar(registro[2])
        n_modelo = IntVar(registro[3])
        n_velocidad = IntVar(registro[4])
        n_potencia = IntVar(registro[5])
        n_plazas = IntVar(registro[6])
        n_eje = IntVar(registro[7])
        n_capacidad = IntVar(registro[-1])

        id_var = IntVar(value=registro[0])
        entry_id = Entry(ventana, textvariable=id_var, width=10, justify="center", state="readonly")
        entry_id.pack(pady=5)

        lbl_marca = Label(ventana, text="Nueva Marca: ")
        lbl_marca.pack(pady=5)
        entry_marca = Entry(ventana, width=15, textvariable=n_marca, justify="center")
        entry_marca.pack(pady=5)

        lbl_color = Label(ventana, text="Nuevo Color: ")
        lbl_color.pack(pady=5)
        entry_color = Entry(ventana, width=15, justify="center")
        entry_color.pack(pady=5)

        lbl_modelo = Label(ventana, text="Nuevo Modelo: ")
        lbl_modelo.pack(pady=5)
        entry_modelo = Entry(ventana, width=15, justify="center")
        entry_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Nueva Velocidad: ")
        lbl_velocidad.pack(pady=5)
        entry_velocidad = Entry(ventana, width=15, justify="center")
        entry_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Nueva Potencia: ")
        lbl_potencia.pack(pady=5)
        entry_potencia = Entry(ventana, width=15, justify="center")
        entry_potencia.pack(pady=5)

        lbl_plazas = Label(ventana, text="Nuevo No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, justify="center")
        entry_plazas.pack(pady=5)

        lbl_eje = Label(ventana, text="Nuevo Eje: ")
        lbl_eje.pack(pady=5)
        entry_eje = Entry(ventana, width=15, justify="center")
        entry_eje.pack(pady=5)

        lbl_capacidad = Label(ventana, text="Nueva Capacidad de Carga: ")
        lbl_capacidad.pack(pady=5)
        entry_capacidad = Entry(ventana, width=15, justify="center")
        entry_capacidad.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command="")
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana, text="Guardar", command=lambda: View.modificar_camiones_id(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def eliminar_camiones(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Vamos a eliminar una entrada de Camiones: ", justify="center")
        lbl_titulo.pack(pady=5)

        id_auto = IntVar()

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID de los Camiones a eliminar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        entry_titulo_2 = Entry(ventana, textvariable=id_auto, width=15, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_buscar = Button(ventana, text="Volver", command=lambda: View.menu_acciones(ventana, "Camiones"))
        btn_buscar.pack(pady=5)