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
w = " "
limpiar()
while True:
    try:
        print("┌──────────────────────────────────────────────┐")
        print("█       Bienvenido a la bisutería ACNZ         █")
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
                while True:
                    v_descripcion= input(f"█  Descripcion del producto {contador}: ")
                    if str.isspace(v_descripcion) == True:
                        print("\nLa descripción no puede estar conformada por espacios en blanco\n")
                    elif str.strip(v_descripcion) == "":
                        print("\nLa descripción esta vacia, por favor ingrese una descripción valida\n")
                    else:
                        break
                while True:
                    v_cantidad= int(input("█  ¿Cuantas piezas se vendieron?: "))
                    if v_cantidad < 0:
                        print("\nLa cantidad proporcionada no puede ser negativa por favor, ingresa una cantidad con valor positivo.\n")
                    elif v_cantidad > 0:
                        break
                while True:
                    v_precio=float(input("█  ¿Cual es el precio del producto?: "))
                    if v_precio < 0:
                        print("\nLa cantidad proporcionada no puede ser negativa por favor, ingresa un precio con valor positivo.\n")
                    elif v_precio > 0:
                        break

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
            #op = input("               Formato:YYYY-mm-dd          \n┌──────────────────────────────────────────────┐\n█   ¿Cual es la fecha que quieres consultar?   █\n└──────────────────────────────────────────────┘\nOpcion:")
            while True:
                try:
                    op = input("               Formato: YYYY-MM-DD         \n┌──────────────────────────────────────────────┐\n█   ¿Cual es la fecha que quieres consultar?   █\n└──────────────────────────────────────────────┘\nOpcion:")
                    datetime.datetime.strptime(op, '%Y-%m-%d')
                    break
                except ValueError:
                    print("\nFormato de fecha inválido, recuerda usar el formato siguiente YYYY-MM-DD.\n")
            print("")
            limpiar()
            Rango = {"Fecha":op}
            try:
                registros = Conexion(Rango=Rango).Consultar()
                if registros:
                    print("│Id\t\t│Fecha\t\t│Descripcion\t\t\t\t│Cantidad\t │Precio\t  │")
                    for id, fecha, descripcion, cantidad, precio in registros:
                        print("╠","═"*15,"╬","═"*15,"╬","═"*39,"╬","═"*16,"╬","═"*16,"╣",sep=(""))
                        print("{:16}{:16}{:40}{:17}{:17}{:1}".format(f"│{id}",f"│{fecha}",f"│{descripcion}",f"│{cantidad}",f"│{precio}","│"))
                    print("╚","═"*15,"╩","═"*15,"╩","═"*39,"╩","═"*16,"╩","═"*16,"╝",sep=(""))
                else:
                    print(f"\nNo se encontraron productos dentro de la fecha {op}\n")    
            except Error as e:
                print(e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")  
        elif menu == "3":
            # Opcion para salir
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

limpiar()
print("┌──────────────────────────────────┐\n█  Culminación del Proceso Actual  █\n└──────────────────────────────────┘")