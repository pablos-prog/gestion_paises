# IMPORTAMOS LOS MODULOS DEL PROYECTO
import os
import archivos
import operaciones
import filtros
import estadisticas


# Nombre del archivo CSV donde se guardan los paises
ARCHIVO = os.path.join(
    os.path.dirname(__file__),
    "paises.csv"
)

# Cargamos los datos al iniciar el programa
paises = archivos.cargar_csv(ARCHIVO)


# MENU PRINCIPAL DEL SISTEMA
while True:

    print("\n==============================")
    print("   GESTION DE PAISES")
    print("==============================")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar por continente")
    print("5. Filtrar por poblacion")
    print("6. Filtrar por superficie")
    print("7. Ordenar por nombre")
    print("8. Ordenar por poblacion")
    print("9. Ordenar por superficie")
    print("10. Estadisticas")
    print("11. Guardar y salir")
    print("==============================")

    opcion = input("Seleccione una opcion: ")

    # OPCION 1: AGREGAR PAIS
    if opcion == "1":

        operaciones.agregar_pais(paises)

    # OPCION 2: ACTUALIZAR PAIS
    elif opcion == "2":

        operaciones.actualizar_pais(paises)

    # OPCION 3: BUSCAR PAIS
    elif opcion == "3":

        operaciones.buscar_pais(paises)

    # OPCION 4: FILTRAR POR CONTINENTE
    elif opcion == "4":

        filtros.filtrar_continente(paises)

    # OPCION 5: FILTRAR POR POBLACION
    elif opcion == "5":

        filtros.filtrar_poblacion(paises)

    # OPCION 6: FILTRAR POR SUPERFICIE
    elif opcion == "6":

        filtros.filtrar_superficie(paises)

    # OPCION 7: ORDENAR POR NOMBRE
    elif opcion == "7":

        filtros.ordenar_nombre(paises)

    # OPCION 8: ORDENAR POR POBLACION
    elif opcion == "8":

        filtros.ordenar_poblacion(paises)

    # OPCION 9: ORDENAR POR SUPERFICIE
    elif opcion == "9":

        filtros.ordenar_superficie(paises)

    # OPCION 10: ESTADISTICAS
    elif opcion == "10":

        estadisticas.pais_mayor_poblacion(paises)
        estadisticas.pais_menor_poblacion(paises)
        estadisticas.promedio_poblacion(paises)
        estadisticas.promedio_superficie(paises)
        estadisticas.contar_por_continente(paises)

    # OPCION 11: GUARDAR Y SALIR
    elif opcion == "11":

        archivos.guardar_csv(ARCHIVO, paises)

        print("Datos guardados. Saliendo del programa...")

        break

    # OPCION INVALIDA
    else:

        print("Error: opcion invalida.")