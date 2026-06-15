# MODULO DE ESTADISTICAS
# Contiene funciones para calcular datos importantes de los paises


# Funcion para encontrar el pais con mayor poblacion
def pais_mayor_poblacion(paises):

    # Verifica si la lista está vacia
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    # Se asume que el primer pais es el mayor inicialmente
    mayor = paises[0]

    # Recorre la lista comparando poblaciones
    for pais in paises:

        # Si encuentra uno con mayor poblacion, lo reemplaza
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    print("\nPais con mayor poblacion:")
    print(mayor)

# Funcion para encontrar el pais con menor poblacion
def pais_menor_poblacion(paises):

    # Verifica si la lista está vacia
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    # Se asume que el primer pais es el menor inicialmente
    menor = paises[0]

    # Recorre la lista comparando poblaciones
    for pais in paises:

        # Si encuentra uno con menor poblacion, lo reemplaza
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    print("\nPais con menor poblacion:")
    print(menor)

# Funcion para calcular el promedio de poblacion
def promedio_poblacion(paises):

    # Verifica si la lista está vacia
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    suma = 0

    # Recorre todos los paises y suma sus poblaciones
    for pais in paises:
        suma = suma + pais["poblacion"]

    # Calcula el promedio
    promedio = suma / len(paises)

    print("\nPromedio de poblacion:", promedio)

# Funcion para calcular el promedio de superficie
def promedio_superficie(paises):

    # Verifica si la lista está vacia
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    suma = 0

    # Recorre todos los paises y suma sus superficies
    for pais in paises:
        suma = suma + pais["superficie"]

    # Calcula el promedio
    promedio = suma / len(paises)

    print("\nPromedio de superficie:", promedio)

# Funcion para contar paises por continente
def contar_por_continente(paises):

    # Diccionario para almacenar conteos
    conteo = {}

    # Recorre todos los paises
    for pais in paises:

        continente = pais["continente"]

        # Si el continente no existe en el diccionario
        if continente not in conteo:

            # Se inicializa en 1
            conteo[continente] = 1

        else:

            # Si ya existe, se incrementa
            conteo[continente] = conteo[continente] + 1

    print("\nCantidad de paises por continente:")

    # Muestra los resultados
    for continente in conteo:

        print(continente, ":", conteo[continente])

