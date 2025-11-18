# adivinador while#
import random
import os
numero_secreto = random.randint(1, 15)
                                
cantidad = 0
num = None
#ESTRUCTURA WHILE #
while num != numero_secreto:
    os.system("cls")
    try:
        num = int(input("Ingrese un numero: "))  # type: ignore
    except ValueError:
        print("Por favor ingrese un número válido.")
        input("presione enter para continuar")
        continue
    cantidad = cantidad + 1
    if numero_secreto != num:
        print(f"No adivinaste, has ingresado {num}; sigue intentando (intento {cantidad}).")
        print("Intente de nuevo")
        input("presione enter para continuar")
    else:
        print(f"Felicidades, has adivinado el numero secreto {numero_secreto} en {cantidad} intentos")
        input("presione enter para continuar")
        break

