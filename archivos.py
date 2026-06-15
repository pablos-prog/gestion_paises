#importamos el modulo csv paratrabajar con archvios csv
import csv


#funcion para cargar los paises desde el archivo csv
def cargar_csv(nombre_archivo):
#lista donde se guardan los pises
    paises = []
    
    try:
#abrimos el archivo en modo lectura
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
#cada fila se leera como un diccionario
            lector = csv.DictReader(archivo)
#recorremos todas las filas del archivo
            for fila in lector:
#creamos un diccionario para cada pais
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }  
#agregamos el pais a la lista  
                paises.append(pais)

#error si el archivo no existe
    except FileNotFoundError:
        print("Error! el archivo no existe")
#error si hay datos númericos incorrectos
    except ValueError:
        print("Error! hay datos invalidos")          
#error si falta alguna columna
    except KeyError:
        print("Error! el formato del archivo csv es incorrecto")   
#devolvemos la lista de paises
    return paises

#funcion para guardad los paises en el archivo csv
def guardar_csv(nombre_archivo, paises):
#abrimos el archivo en modo escritura
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
#definimos los nombres de las columnas
        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]
#creamos el escritor csv
        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )
#escribimos la fila de encavezados
        escritor.writeheader()
#escribimos cada pais en una fila
        for pais in paises:
            escritor.writerow(pais)

        print("Datos guardados correctamente")    