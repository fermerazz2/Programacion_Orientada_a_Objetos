from tkinter import messagebox
from model import cochesBD
from view import view_1

class Controlador:

    #Autos
    @staticmethod
    def insertar_auto(marca,color,modelo,velocidad,caballaje,plazas):
        resultado = cochesBD.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        if resultado:
            messagebox.showinfo(icon="info", message=f"El coche {marca} {color} se registró con éxito", title="Registro")
        else:
            messagebox.showerror(icon="warning", message="No se pudo completar el registro, intente nuevamente.", title="Registro")    
        return resultado
    @staticmethod
    def mostrar_autos():
        registro = cochesBD.Autos.consultar()
        return registro
    
    @staticmethod
    def revisar_id(ventana, id_auto):
        if not id_auto:
            messagebox.showwarning("Error", "Debes ingresar un ID válido")
            return
        registro = cochesBD.Autos.check_id(id_auto)
        if registro:
            view_1.View.modificar_auto(ventana, registro)
        else:
            messagebox.showinfo(icon="error", message=f"El id {id_auto} no se encuentra en la base de datos.")

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Estado",message=f"Accion realizada exitosamente")
        else:
            messagebox.showerror(title="Estado",message=f"Fallo al realizar la accion")

    @staticmethod
    def enviar_actualizacion(marca,color,modelo,velocidad,potencia,plazas,id_auto):
        respuesta = cochesBD.Autos.actualizar(marca,color,modelo,velocidad,potencia,plazas,id_auto)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def mostrar_camionetas():
        registro = cochesBD.Camionetas.consultar()
        return registro

    @staticmethod
    def mostrar_camiones():
        registro = cochesBD.Camiones.consultar()
        return registro

    @staticmethod
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        res = cochesBD.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        Controlador.respuesta_sql(res)
        return res

    @staticmethod
    def revisar_id_camioneta(ventana, id_camioneta):
        if not id_camioneta:
            messagebox.showwarning("Error", "Debes ingresar un ID válido")
            return
        
        registro = cochesBD.Camionetas.check_id(id_camioneta)
        if registro:

            view_1.View.modificar_camioneta(ventana, registro)
        else:
            messagebox.showinfo(icon="error", message=f"El ID {id_camioneta} no existe en Camionetas.")

    @staticmethod
    def enviar_actualizacion_camioneta(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada, id_camioneta):
        res = cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada, id_camioneta)
        Controlador.respuesta_sql(res)

    @staticmethod
    def eliminar_camioneta(id_camioneta):
        if not id_camioneta: return
        res = cochesBD.Camionetas.eliminar(id_camioneta)
        Controlador.respuesta_sql(res)

    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad):
        res = cochesBD.Camiones.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad)
        Controlador.respuesta_sql(res)
        return res

    @staticmethod
    def revisar_id_camion(ventana, id_camion):
        if not id_camion:
            messagebox.showwarning("Error", "Debes ingresar un ID válido")
            return
        
        registro = cochesBD.Camiones.check_id(id_camion)
        if registro:
            view_1.View.modificar_camion(ventana, registro)
        else:
            messagebox.showinfo(icon="error", message=f"El ID {id_camion} no existe en Camiones.")

    @staticmethod
    def enviar_actualizacion_camion(marca, color, modelo, velocidad, potencia, plazas, eje, capacidad, id_camion):
        res = cochesBD.Camiones.actualizar(marca, color, modelo, velocidad, potencia, plazas, eje, capacidad, id_camion)
        Controlador.respuesta_sql(res)

    @staticmethod
    def eliminar_camion(id_camion):
        if not id_camion: return
        res = cochesBD.Camiones.eliminar(id_camion)
        Controlador.respuesta_sql(res)