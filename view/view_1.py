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

        lbl_titulo_2 = Label(ventana, text="Ingresa el ID del Auto a modificar: ", justify="center")
        lbl_titulo_2.pack(pady=5)
        entry_titulo_2 = Entry(ventana, width=15, justify="center")
        entry_titulo_2.pack(pady=5)

        btn_buscar = Button(ventana, text="Buscar", command="")
        btn_buscar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=View.menu_acciones(ventana, "Autos"))
        btn_volver.pack(pady=5)
    
    @staticmethod
    def modificar_auto(ventana, registro):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f"Modificar un auto", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_id = Label(ventana,text="ID de la operacion (No editable)")
        lbl_id.pack(pady=5)

        n_marca = StringVar(registro[1])
        n_color = StringVar(registro[2])
        n_modelo = IntVar(registro[3])
        n_velocidad = IntVar(registro[4])
        n_potencia = IntVar(registro[5])
        n_plazas = IntVar(registro[-1])

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

        lbl_plazas = Label(ventana, text="No. de Plazas: ")
        lbl_plazas.pack(pady=5)
        entry_plazas = Entry(ventana, width=15, justify="center")
        entry_plazas.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command="")
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana, text="Guardar", command=lambda: View.modificar_autos_id(ventana))
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

        btn_buscar = Button(ventana, text="Volver", command=View.menu_acciones(ventana, "Autos"))
        btn_buscar.pack(pady=5)
    
    #CAMIONETAS
    @staticmethod 
    def insertar_camionetas(ventana):
        View.borrar_pantalla(ventana)

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

        btn_guardar = Button(ventana, text="Guardar", command="")
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

        btn_buscar = Button(ventana, text="Buscar", command="")
        btn_buscar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=View.menu_acciones(ventana, "Camionetas"))
        btn_volver.pack(pady=5)

    @staticmethod
    def modificar_camioneta(ventana, registro):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f"Modificar un auto", justify="center")
        lbl_titulo.pack(pady=5)

        lbl_id = Label(ventana,text="ID de la operacion (No editable)")
        lbl_id.pack(pady=5)

        n_marca = StringVar(registro[1])
        n_color = StringVar(registro[2])
        n_modelo = IntVar(registro[3])
        n_velocidad = IntVar(registro[4])
        n_potencia = IntVar(registro[5])
        n_plazas = IntVar(registro[6])
        n_traccion = StringVar(registro[7])
        n_cerrada = BooleanVar(registro[-1])

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

        lbl_traccion = Label(ventana, text="Traccion: ")
        lbl_traccion.pack(pady=5)
        entry_traccion = Entry(ventana, width=15, justify="center")
        entry_traccion.pack(pady=5)

        lbl_cerrada = Label(ventana, text="Cerrada: ")
        lbl_cerrada.pack(pady=5)
        entry_cerrada = Entry(ventana, width=15, justify="center")
        entry_cerrada.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command="")
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana, text="Guardar", command=lambda: View.modificar_camionetas_id(ventana))
        btn_volver.pack(pady=5)

    #Falta eliminar de camionetas y hacer las interfaces de camiones
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

        btn_buscar = Button(ventana, text="Volver", command=View.menu_acciones(ventana, "Camionetas"))
        btn_buscar.pack(pady=5)