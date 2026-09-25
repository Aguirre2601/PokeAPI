# Aplicación de Gestión y Análisis de Equipos Pokémon (PokeAPI)

## 📌 Objetivo del Proyecto
Esta aplicación en Python permite buscar Pokémon utilizando la PokeAPI, filtrar resultados por tipo, estructurar y validar equipos de hasta 6 Pokémon sin duplicados, y modificar los equipos existentes. Los datos son almacenados en un archivo `datos.json` y posteriormente analizados en un entorno de Pandas para obtener indicadores estadísticos (como el tipo más repetido) y generar visualizaciones gráficas.

## 🛠️ Requisitos Previos
* **Python**: Versión 3.13 o superior.
* **Entorno Virtual**: Se recomienda el uso de `.venv`.

## 🚀 Instalación y Ejecución
1. **Clonar o descomprimir el proyecto.**
2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate

## Instalar las dependencias necesarias 

primero asegrense de tener activo su entorno virtual

    ```bash
     pip install -r requirements.txt

## Archivo Contenido esperado

main.py ->Ejecución principal y flujo general de la aplicación.

funciones.py-> Funciones propias y lógica reutilizable.

analisis.ipynb ->Exploración con pandas, gráficos y conclusiones.

datos.json o datos.csv -> Información utilizada o producida por la aplicación.

requirements.txt-> Bibliotecas externas necesarias.

README.md (Obligatorio) -> Objetivo, instrucciones de ejecución y decisiones principales.


## 🤖 Registro del Uso de IA

Prompt 1: "Cómo generar la conexión a la PokeAPI usando la librería requests con try/except."

Estado: Aceptado. Se implementó el manejo de excepciones para HTTPError y ConnectionError.

Verificación: Se probó buscar un Pokémon inexistente y cortar la conexión a internet para verificar que el programa responda adecuadamente sin colapsar.

Prompt 2: "..."

Estado: Modificado.

Verificación: ...

Prompt 3: "..."

Estado: Aceptado.

Verificación: ...