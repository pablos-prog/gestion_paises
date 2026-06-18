# MODULO DE FILTROS Y ORDENAMIENTOS
# Contiene funciones para filtrar y ordenar paises

# funcion para mostrar los paises de un continente
def filtrar_continente(paises):

# solicita el continente a buscar
    continente = input(
        "Ingrese el continente: "
    )

# convierte el texto a minusculas
# para facilitar la comparacion
    continente = continente.lower()

# variable para saber si hubo resultados
    encontrado = False

    print("\nResultados encontrados:\n")

# recorre toda la lista de paises
    for pais in paises:

# compara el continente ingresado
# con el continente de cada pais
        if (
            pais["continente"].lower()
            == continente
        ):

# muestra el pais encontrado
            print(pais)

# indica que hubo coincidencias
            encontrado = True

# si no hubo resultados
    if encontrado == False:

        print(
            "No se encontraron paises."
        )

#funcion para mostrar los paises dentro de un rango de poblacion
def filtrar_poblacion(paises):

#se solicita la poblacion minima
    while True:

        try:

#convierte el dato ingresado a entero
            minimo = int(
                input(
                    "Ingrese la poblacion minima: "
                )
            )

#verifica que el valor sea valido
            if minimo >= 0:
                break

#se ejecuta si el numero es negativo
            print(
                "Error: ingrese un valor positivo."
            )

#se ejecuta si el usuario ingresa letras
#o cualquier dato que no pueda convertirse a entero
        except ValueError:

            print(
                "Error: debe ingresar un numero entero."
            )

#se solicita la poblacion maxima
    while True:

        try:

#convierte el dato ingresado a entero
            maximo = int(
                input(
                    "Ingrese la poblacion maxima: "
                )
            )

#verifica que el valor maximo sea mayor
#o igual al valor minimo
            if maximo >= minimo:
                break

            print(
                "Error: debe ser mayor o igual al minimo."
            )

#captura errores de conversion
        except ValueError:

            print(
                "Error: debe ingresar un numero entero."
            )

    print("\nResultados encontrados:\n")

#recorre toda la lista de paises
    for pais in paises:

#verifica si la poblacion del pais
#se encuentra dentro del rango solicitado
        if minimo <= pais["poblacion"] <= maximo:

#muestra el pais encontrado
            print(pais)

# funcion para mostrar los paises
# dentro de un rango de superficie
def filtrar_superficie(paises):

# solicita la superficie minima
    while True:

        try:

            minimo = int(
                input(
                    "Ingrese la superficie minima: "
                )
            )

            if minimo >= 0:
                break

            print(
                "Error: ingrese un valor positivo."
            )

        except ValueError:

            print(
                "Error: debe ingresar un numero entero."
            )

# solicita la superficie maxima
    while True:

        try:

            maximo = int(
                input(
                    "Ingrese la superficie maxima: "
                )
            )

            if maximo >= minimo:
                break

            print(
                "Error: debe ser mayor o igual al minimo."
            )

        except ValueError:

            print(
                "Error: debe ingresar un numero entero."
            )

    print("\nResultados encontrados:\n")

# variable para saber si hubo resultados
    encontrado = False

# recorre todos los paises
    for pais in paises:

# verifica si la superficie
# esta dentro del rango
        if minimo <= pais["superficie"] <= maximo:

            print(pais)

            encontrado = True

# si no hubo coincidencias
    if encontrado == False:

        print(
            "No se encontraron paises."
        )


#funcion para ordenar los paises alfabeticamente por nombre
def ordenar_nombre(paises):

#se crea una copia de la lista original
#para evitar modificar los datos cargados
    ordenados = paises.copy()

#primer recorrido del algoritmo burbuja
#controla la cantidad de pasadas necesarias
#para garantizar que toda la lista quede ordenada
    for i in range(len(ordenados)):

#segundo recorrido
#compara elementos vecinos de la lista
        for j in range(len(ordenados) - 1):

#compara los nombres de dos paises consecutivos
#si el primero debería ir después del segundo
#en orden alfabético, se intercambian
            if ordenados[j]["nombre"] > ordenados[j + 1]["nombre"]:

#guarda temporalmente el primer pais
                auxiliar = ordenados[j]

#mueve el segundo pais una posición hacia atrás
                ordenados[j] = ordenados[j + 1]

#coloca el pais guardado en la siguiente posición
                ordenados[j + 1] = auxiliar

    print("\nPaises ordenados por nombre:\n")

#recorre la lista ordenada y muestra cada pais
    for pais in ordenados:

        print(pais)


# Funcion para ordenar los paises segun su poblacion
def ordenar_poblacion(paises):

    # Solicita el tipo de ordenamiento
    opcion = input(
        "Ascendente (A) o Descendente (D): "
    ).upper()

    # Valida la opcion ingresada
    while opcion != "A" and opcion != "D":

        print("Error: debe ingresar A o D.")

        opcion = input(
            "Ascendente (A) o Descendente (D): "
        ).upper()

    # Copia de la lista original
    ordenados = paises.copy()

    # Algoritmo burbuja
    for i in range(len(ordenados)):

        for j in range(len(ordenados) - 1):

            # Orden ascendente
            if opcion == "A":

                if ordenados[j]["poblacion"] > ordenados[j + 1]["poblacion"]:

                    auxiliar = ordenados[j]
                    ordenados[j] = ordenados[j + 1]
                    ordenados[j + 1] = auxiliar

            # Orden descendente
            else:

                if ordenados[j]["poblacion"] < ordenados[j + 1]["poblacion"]:

                    auxiliar = ordenados[j]
                    ordenados[j] = ordenados[j + 1]
                    ordenados[j + 1] = auxiliar

    print("\nPaises ordenados por poblacion:\n")

    # Si no hay datos
    if len(ordenados) == 0:
        print("No hay paises para mostrar.")
        return

    for pais in ordenados:
        print(pais)


# Funcion para ordenar los paises segun su superficie
def ordenar_superficie(paises):

    # Solicita el tipo de ordenamiento
    opcion = input(
        "Ascendente (A) o Descendente (D): "
    ).upper()

    # Valida que la opcion sea correcta
    while opcion != "A" and opcion != "D":

        print(
            "Error: debe ingresar A o D."
        )

        opcion = input(
            "Ascendente (A) o Descendente (D): "
        ).upper()

    # Se crea una copia para no modificar la lista original
    ordenados = paises.copy()

    # Primer recorrido del algoritmo burbuja
    for i in range(len(ordenados)):

        # Segundo recorrido para comparar elementos vecinos
        for j in range(len(ordenados) - 1):

            # Orden ascendente
            if opcion == "A":

                # Si la superficie actual es mayor que la siguiente
                # se intercambian las posiciones
                if (
                    ordenados[j]["superficie"]
                    > ordenados[j + 1]["superficie"]
                ):

                    auxiliar = ordenados[j]
                    ordenados[j] = ordenados[j + 1]
                    ordenados[j + 1] = auxiliar

            # Orden descendente
            else:

                # Si la superficie actual es menor que la siguiente
                # se intercambian las posiciones
                if (
                    ordenados[j]["superficie"]
                    < ordenados[j + 1]["superficie"]
                ):

                    auxiliar = ordenados[j]
                    ordenados[j] = ordenados[j + 1]
                    ordenados[j + 1] = auxiliar

    print("\nPaises ordenados por superficie:\n")

    # Recorre la lista ordenada y muestra cada pais
    for pais in ordenados:

        print(pais)

