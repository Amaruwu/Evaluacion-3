from funciones import *
import random



#Menu
while True:
    print("-----------------------")
    print("       IMMO Ltda       ")
    print("-----------------------")
    print("1. Registrarse")
    print("2. Buscar por rut")
    print("3. Reporte segun renta")
    print("4. Salir")
    print("-----------------------")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        registrarse()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        reportes()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")