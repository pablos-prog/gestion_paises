🌍 Gestión de Datos de Países en Python
📌 Descripción del proyecto

Este proyecto es una aplicación en Python que permite gestionar información sobre países utilizando estructuras de datos como listas y diccionarios, junto con funciones, condicionales, ciclos y manejo de archivos CSV.

El sistema permite agregar, buscar, filtrar, ordenar y obtener estadísticas sobre países almacenados en un archivo CSV.

🎯 Objetivo

Aplicar conceptos de programación estructurada, modularización y manejo de archivos para construir un sistema funcional de gestión de datos.

🧱 Estructura del proyecto

El proyecto está organizado en módulos para mejorar la claridad del código:

gestion_paises/
├── main.py              # Menú principal del sistema
├── archivos.py          # Carga y guardado de CSV
├── operaciones.py       # Alta, modificación y búsqueda
├── filtros.py           # Filtros y ordenamientos
├── estadisticas.py      # Cálculos estadísticos
├── paises.csv           # Base de datos de países
└── README.md            # Documentación del proyecto
📊 Estructura de datos

Cada país se representa mediante un diccionario con los siguientes campos:

nombre (str)
poblacion (int)
superficie (int)
continente (str)
Ejemplo CSV:
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
Japon,125800000,377975,Asia
Alemania,83149300,357022,Europa
⚙️ Funcionalidades
➕ Gestión de países
Agregar país
Actualizar población y superficie
Buscar país
🔎 Filtros
Por continente
Por rango de población
Por rango de superficie
🔢 Ordenamientos
Por nombre
Por población (ascendente y descendente)
Por superficie (ascendente y descendente)
📊 Estadísticas
País con mayor población
País con menor población
Promedio de población
Promedio de superficie
Cantidad de países por continente
▶️ Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

python main.py
💾 Persistencia

Los datos se guardan automáticamente en el archivo paises.csv al finalizar la ejecución del programa.

🧠 Conceptos aplicados
Listas
Diccionarios
Funciones
Condicionales
Bucles
Archivos CSV
Modularización
Manejo de excepciones
👥 Integrantes
Pablo Soñez
🎥 Video demostración

Link del video del proyecto:

👉 https://drive.google.com/file/d/1ZKZ8szTTy76rN6wGMiX0AzOSSX7fNOSs/view?usp=drive_link

📄 Documentación

El informe completo del proyecto se encuentra en formato PDF dentro del repositorio.

📄 Archivo: 

## 📚 Bibliografía

- https://docs.python.org/3/
- Material de clase