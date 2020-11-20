import sys
import sqlite3
from sqlite3 import Error
import datetime
import os

class Conexion:

    def __init__(self,fecha="",v_descripcion="",v_cantidad="",v_precio="",Rango=""):
        self.v_descripcion = v_descripcion
        self.v_cantidad = v_cantidad
        self.v_precio = v_precio
        self.fecha = fecha
        self.Rango = Rango

    def Guardar(self):
        with sqlite3.connect("BD_Productos.db") as conn:
            mi_cursor = conn.cursor()
            ahora1 = self.fecha
            v_descripcion = self.v_descripcion
            v_cantidad = self.v_cantidad
            v_precio = self.v_precio
            valores = {"Fecha":ahora1,"Descripcion":v_descripcion,"Cantidad":v_cantidad,"Precio":v_precio}
            mi_cursor.execute("INSERT INTO T_Productos VALUES(:Fecha,:Descripcion,:Cantidad,:Precio)", valores)



    
    def Consultar(self):
        pass