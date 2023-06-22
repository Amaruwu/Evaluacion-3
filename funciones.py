import random
import os
import time
import msvcrt

#Lista
clientes = []

#Constantes
proyecto = ""

#Funciones
def limpiaPant():
    
        time.sleep(0.5)
        os.system("cls")

def registrarse():
    rut = input("Ingrese su rut: ")
    while not rut.isdigit() or len(rut) != 8 and len(rut) != 9:
        print("Rut invalido. Debe ser numérico y tener un minimo de 8 dijitos y un maximo de 9")
        rut = input("Ingrese su rut: ")
    
    nombre_cliente = input("Ingrese su nombre: ")
    while nombre_cliente == "":
        print("Su nombre no puede estar vacio")
        nombre_cliente = input("Ingrese su nombre ")
    
    opc = int(input("Ingrese el proyecto de departamento\n1.- Vive Santiago\n2.- Vive La Florida\n3.- Vive Ñuñoa\nDigite su opcion: "))
    while opc == "" or opc>3 or opc==0:
        print("Ingrese devuelta")
        opc = int(input("Ingrese el proyecto de departamento\n1.- Vive Santiago\n2.- Vive La Florida\n3.- Vive Ñuñoa\nDigite su opcion: "))
        
    if opc == 1:
        proyecto = "Vive Santiago"
    elif opc == 2:
        proyecto = "Vive La Florida"
    elif opc == 3:
        proyecto = "Vive Ñuñoa"
    
    Srenta = input("Ingrese su renta: ")
    while not Srenta.isdigit():
        print("Renta inválida. Este tiene que ser numerico")
        Srenta = input("Ingrese su renta: ")
    
    renta = int(Srenta)
    
    UF = random.randint(2500, 3700)
    
    cliente = {
        "Rut": rut,
        "Nombre": nombre_cliente,
        "Proyecto": proyecto,
        "Renta": renta,
        "UF": UF
    }
    
    limpiaPant()
    
    clientes.append(cliente)
    print("Cliente registrado correctamente.")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    limpiaPant()

def buscar():
    rut = input("Ingrese su rut para buscar: ")
    for cliente in clientes:
        if cliente["Rut"] == rut:
            print("---------------------------")
            print("Cliente:")
            print("Nombre:", cliente["Nombre"])
            print("Rut:", cliente["Rut"])
            print("Proyecto:", cliente["Proyecto"])
            print("Renta:", cliente["Renta"])
            print("---------------------------")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
            limpiaPant()
            return
    print("No se encontro ningun cliente")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    limpiaPant()

def reportes():
    contador = 0
    print("REPORTES")
    for cliente in clientes:
        if cliente["Renta"] > 900000:
            print("---------------------------")
            print("Reporte IMMO Ltda.: ")
            print("Sr/a", cliente["Nombre"])
            print("Rut:", cliente["Rut"])
            print("Con su renta de", cliente["Renta"])
            print("En el Proyecto:", cliente["Proyecto"])
            print("Puede acceder a un Dpto de UF a:", cliente["UF"], "UF")
            print("---------------------------")
            contador += 1
    
    print(f"Se generaron ", contador, "reportes")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    limpiaPant()