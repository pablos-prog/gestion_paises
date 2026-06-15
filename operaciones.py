#funcion para guardar un nuevo pais
def agregar_pais(paises):
#pedimos el nombre del pais
    nombre = input("Ingresa el nombre del nuevo pais: ").strip()

#validamos que no esté vacio
    while nombre == "":
        print("Error: el nombre no puede estar vacio.")
        nombre = input("Ingrese el nombre del pais: ").strip()

#validamos la poblacion
    while True:
        try:
            poblacion = int(input("Ingrese la poblacion: "))

            if poblacion > 0:
                break

            print("Error: la poblacion debe ser mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un numero entero.")

#validamos la superficie
    while True:
        try:
            superficie = int(input("Ingrese la superficie en km²: "))

            if superficie > 0:
                break

            print("Error: la superficie debe ser mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un numero entero.")

#pedimos el continente
    continente = input("Ingrese el continente: ").strip()

#validamos que no esté vacio
    while continente == "":
        print("Error: el continente no puede estar vacio.")
        continente = input("Ingrese el continente: ").strip()

#creamos el diccionario del pais
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

#agregamos el pais a la lista
    paises.append(pais)

    print("Pais agregado correctamente.")

#funcion para actualizar la poblacion y superficie de un pais
def actualizar_pais(paises):

#solicita el nombre del pais a modificar
    nombre = input("Ingrese el pais a actualizar: ").strip().lower()

#recorre la lista de paises buscando coincidencias
    for pais in paises:

#compara el nombre ingresado con el nombre del pais
        if pais["nombre"].lower() == nombre:

#solicita y valida la nueva poblacion
            while True:
                try:

                    nueva_poblacion = int(
                        input("Nueva poblacion: ")
                    )

#verifica que sea un valor positivo
                    if nueva_poblacion > 0:

                        pais["poblacion"] = nueva_poblacion
                        break

                    print(
                        "Error: la poblacion debe ser mayor que cero."
                    )

                except ValueError:

                    print(
                        "Error: debe ingresar un numero entero."
                    )

#solicita y valida la nueva superficie
            while True:
                try:

                    nueva_superficie = int(
                        input("Nueva superficie: ")
                    )

#Verifica que sea un valor positivo
                    if nueva_superficie > 0:

                        pais["superficie"] = nueva_superficie
                        break

                    print(
                        "Error: la superficie debe ser mayor que cero."
                    )

                except ValueError:

                    print(
                        "Error: debe ingresar un numero entero."
                    )

            print("Pais actualizado correctamente.")

            return

#se ejecuta si no se encontró el pais
    print("Pais no encontrado.")

#funcion para buscar paises por nombre
def buscar_pais(paises):

#solicita el texto a buscar
    texto = input(
        "Ingrese el nombre a buscar: "
    ).strip().lower()

#verifica que el campo no esté vacio
    while texto == "":

        print("Error: debe ingresar un texto.")

        texto = input(
            "Ingrese el nombre a buscar: "
        ).strip().lower()

#lista donde se guardarán los resultados encontrados
    encontrados = []

#recorre todos los paises de la lista
    for pais in paises:

#busca coincidencias parciales o exactas
        if texto in pais["nombre"].lower():

            encontrados.append(pais)

#verifica si hubo resultados
    if len(encontrados) == 0:

        print("No se encontraron paises.")

    else:

        print("\nResultados encontrados:\n")

#muestra los paises encontrados
        for pais in encontrados:

            print(
                f"Nombre: {pais['nombre']} | "
                f"Poblacion: {pais['poblacion']} | "
                f"Superficie: {pais['superficie']} km² | "
                f"Continente: {pais['continente']}"
            )