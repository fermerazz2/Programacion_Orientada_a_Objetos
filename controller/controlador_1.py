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
    def revisar_id(id_auto):
        pass

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Estado",message=f"Accion realizada exitosamente")
        else:
            messagebox.showerror(title="Estado",message=f"Fallo al realizar la accion")

    @staticmethod
    def enviar_actualizacion(marca,color,modelo,velocidad,caballaje,plazas,id_auto):
        respuesta = cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id_auto)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def mostrar_camionetas():
        registro = cochesBD.Camionetas.consultar()
        return registro