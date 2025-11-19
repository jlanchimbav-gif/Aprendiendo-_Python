# strings en python #
def main():
    print("=== PROGRAMA DE MANIPULACIÓN DE CADENAS ===\n")
    # entrada de datos#
    cadena = input("Ingrese una cadena de texto: ")
    #concatenacion de cadenas#
    saludo = "Análisis del texto: "
    texto_concatenado = saludo + cadena
    print("\nCadena original:", cadena)
    print("Texto concatenado:", texto_concatenado)
    # longitud de la cadena #
    longitud = len(cadena)
    print("Longitud de la cadena:", longitud)
    # conversión a mayúsculas #
    mayusculas = cadena.upper()
    print("Cadena en mayúsculas:", mayusculas)
    # conversión a minúsculas #
    minusculas = cadena.lower()
    print("Cadena en minúsculas:", minusculas)
    # reemplazo de caracteres #
    caracter_a_reemplazar = input("\nIngrese el carácter que desea reemplazar: ")
    nuevo_caracter = input("Ingrese el nuevo carácter: ")
    cadena_reemplazada = cadena.replace(caracter_a_reemplazar, nuevo_caracter)
    print("Cadena después del reemplazo:", cadena_reemplazada)
    # división de la cadena #
    palabras = cadena.split()
    print("Palabras en la cadena:", palabras)
    # unión de palabras #
    cadena_unida = ' '.join(palabras)
    print("Cadena unida nuevamente:", cadena_unida)

if __name__ == "__main__":
    main()

