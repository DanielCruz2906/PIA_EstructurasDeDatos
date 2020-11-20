import sys
import sqlite3
from sqlite3 import Error
import datetime
import os
from functions.Conection import Conexion

from os import system,name

def limpiar():
    if name == "nt":
        system("cls")
    else:
        system("clear")


contador=1

limpiar()
while True:
    try:
        print("┌──────────────────────────────────────────────┐")
        print("█         Que movimiento deseas hacer          █")
        print("█ [1]:Registrar una venta                      █\n█ [2]:Consultar ventas de un dia en especifico █\n█ [3]:Salir                                    █\n█                                              █")
        print("└──────────────────────────────────────────────┘")
        menu=input("Opcion:")
        lista_mult=[]
        
        if menu == "1":
            ciclo=1
            while ciclo == 1:
                
                ahora = datetime.datetime.now()
                ahora1=ahora.strftime('%Y-%m-%d')
                limpiar()
                print("┌────────────────────────────────────────────────────────────────┐")
                v_descripcion= input(f"█  Descripcion del producto {contador}: ")
                
                v_cantidad= int(input("█  Cuantas piezas se vendieron: "))
                
                v_precio=float(input("█  Cual es el precio del producto: "))
                print("└────────────────────────────────────────────────────────────────┘")
                lista_mult.append(v_cantidad * v_precio)
                
                try:
                    Conexion(ahora1,v_descripcion,v_cantidad,v_precio).Guardar()
                except Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")    
                
                contador+=1
                print("")
                print("┌──────────────────────────────────────────────────────────────────┐\n█                       ¿Que deseas hacer?\n█  [1]:Si deseas seguir registrando ventas\n█  [0]:Si deseas salir del registrador de ventas")
                print("└──────────────────────────────────────────────────────────────────┘")
                ciclo=int(input("Opcion:"))
                
                limpiar()
                
                print("")
        
            a=sum(lista_mult)
            print("┌──────────────────────────────────────────────┐\n█               PROCESO REALIZADO\n█")
            print(f"█  El monto total es de {a} pesos\n└──────────────────────────────────────────────┘")
            
        elif menu == "2":
            limpiar()
            op = input("               Formato:YYYY-mm-dd          \n┌──────────────────────────────────────────────┐\n█   ¿Cual es la fecha que quieres consultar?   █\n└──────────────────────────────────────────────┘\nOpcion:")
            print("")
            limpiar()
        
            try:
                with sqlite3.connect("BD_Productos.db") as conn:
                    mi_cursor = conn.cursor()
                    Rango = {"Fecha":op}
                    mi_cursor.execute("SELECT * FROM T_Productos WHERE Fecha = :Fecha", Rango)
                    registros = mi_cursor.fetchall()

                    if registros:
                        print("│Fecha\t\t│Descripcion\t\t\t\t│Cantidad\t │Precio\t  │")
                        for fecha, descripcion, cantidad, precio in registros:
                            print("╠","═"*15,"╬","═"*39,"╬","═"*16,"╬","═"*16,"╣",sep=(""))
                            print("{:16}{:40}{:17}{:17}{:1}".format(f"│{fecha}",f"│{descripcion}",f"│{cantidad}",f"│{precio}","│"))
                        print("╚","═"*15,"╩","═"*39,"╩","═"*16,"╩","═"*16,"╝",sep=(""))
                    else:
                        print(f"No se encontraron productos dentro de la fecha {op}")
                    
                        
            except Error as e:
                print(e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")  

        elif menu == "3":
            # Opcion para salir
            limpiar()
            print("┌──────────────────────────────────┐\n█  Culminación del Proceso Actual  █\n└──────────────────────────────────┘")
            break
            
        else:
            limpiar()
            print("┌──────────────────────────────────────────────┐")
            print(f"█  La opción {menu} no es válida")
            print("└──────────────────────────────────────────────┘")
    except:
        limpiar()
        print("┌──────────────────────────────────────────────┐")
        print(f"█  Ocurrió un problema {sys.exc_info()[0]}")
        print("└──────────────────────────────────────────────┘")