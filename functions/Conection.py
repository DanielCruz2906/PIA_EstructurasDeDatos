import sqlite3

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
            valores = {"Fecha":self.fecha,"Descripcion":self.v_descripcion,"Cantidad":self.v_cantidad,"Precio":self.v_precio}
            mi_cursor.execute("INSERT INTO T_Productos(Fecha,Descripcion,Cantidad,Precio) VALUES(:Fecha,:Descripcion,:Cantidad,:Precio)", valores)

    def Consultar(self):
        with sqlite3.connect("BD_Productos.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM T_Productos WHERE Fecha = :Fecha", self.Rango)
            registros = mi_cursor.fetchall()
            return registros