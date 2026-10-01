# Gestor de Equipos Pokémon (PokeAPI)

Aplicación de consola en Python que permite buscar Pokémon usando la [PokeAPI](https://pokeapi.co/), filtrarlos por tipo, crear equipos de hasta 6 miembros sin duplicados, y consultar métricas como el promedio de HP y el tipo dominante. Los datos se persisten localmente en archivos JSON y se utiliza un sistema de caché para evitar consultas repetidas a la API. Incluye un notebook de Jupyter para análisis estadístico y visualización de datos.

---

## Tabla de Contenidos

- [Que hace el programa](#que-hace-el-programa)
- [Herramientas y tecnologías](#herramientas-y-tecnologías)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Uso del menú](#uso-del-menú)
- [Estructura de archivos](#estructura-de-archivos)
- [Flujo de la aplicación](#flujo-de-la-aplicación)
- [Dependencias](#dependencias)
- [Archivos generados](#archivos-generados)
- [Notebook de análisis](#notebook-de-análisis)
- [Registro de uso de IA](#registro-de-uso-de-ia)

---

## Que hace el programa

Esta aplicación permite a los usuarios:

1. **Buscar Pokémon** por nombre, mostrando sus estadísticas principales (tipo, HP, peso, altura).
2. **Filtrar Pokémon por tipo** elemental (fuego, agua, eléctrico, etc.), mostrando los primeros 15 resultados.
3. **Crear equipos** personalizados con nombre único y agregar Pokémon inmediatamente.
4. **Ver métricas** de cada equipo: total de integrantes, promedio de HP y tipo dominante.
5. **Persistir datos** automáticamente en `datos.json` al salir.
6. **Analizar datos** con Pandas y generar gráficos con Matplotlib en el notebook.

### Características principales

- **Caché local**: Evita consultas repetidas a la PokeAPI almacenando resultados en archivos JSON.
- **Validaciones robustas**: Verifica nombres vacíos, equipos duplicados, límite de 6 integrantes y Pokémon repetidos.
- **Manejo de errores**: Captura errores de red, Pokémon inexistentes y tipos no válidos.
- **Interfaz de consola intuitiva**: Menú numerado con retroalimentación clara al usuario.

---

## Herramientas y tecnologías

| Herramienta | Tipo | Uso |
|-------------|------|-----|
| **Python 3.13** | Lenguaje de programación | Lógica principal de la aplicación |
| **PokeAPI** | API REST | Fuente de datos de Pokémon |
| **requests** | Librería HTTP | Peticiones a la PokeAPI |
| **json** | Módulo estándar | Serialización y persistencia de datos |
| **pathlib** | Módulo estándar | Manejo de rutas de archivos |
| **pandas** | Librería de datos | Análisis estadístico en el notebook |
| **matplotlib** | Librería de visualización | Generación de gráficos de barras |
| **Jupyter Notebook** | Entorno interactivo | Análisis exploratorio de datos |
| **Git** | Control de versiones | Seguimiento de cambios en el proyecto |

---

## Requisitos previos

| Requisito | Detalle |
|-----------|---------|
| **Python** | Versión 3.13 o superior |
| **pip** | Gestor de paquetes de Python (incluido por defecto) |
| **Conexión a internet** | Necesaria para consultar la PokeAPI por primera vez |
| **Entorno virtual** | Recomendado (`.venv`) |
| **Jupyter** | Necesario solo para ejecutar el notebook de análisis |

---

## Instalación

### 1. Clonar o descomprimir el proyecto

```bash
git clone <url-del-repositorio>
cd PokeAPI
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv .venv
```

**En Windows:**
```bash
.venv\Scripts\activate
```

**En macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución

### Aplicación principal

Para iniciar la aplicación de consola:

```bash
python main.py
```

### Notebook de análisis

Para ejecutar el notebook de Jupyter:

```bash
jupyter notebook analisis.ipynb
```

---

## Uso del menú

Al ejecutar `python main.py`, verás el siguiente menú:

```
--- GESTOR DE EQUIPOS POKÉMON ---
1. Buscar Pokémon
2. Filtrar por tipo
3. Crear equipo
4. Ver equipos y métricas
5. Guardar y salir
```

### Opción 1: Buscar Pokémon

1. Ingresa el nombre del Pokémon (ej: `pikachu`, `charizard`).
2. El sistema muestra: nombre, tipo principal, HP, peso y altura.
3. Si el Pokémon ya fue consultado antes, se carga desde caché.

**Ejemplo de salida:**
```
-> Pikachu descargado de la API.

Pikachu
Tipo principal: electric
HP: 35
Peso: 60
Altura: 4
```

### Opción 2: Filtrar por tipo

1. Ingresa un tipo elemental (ej: `fire`, `water`, `electric`).
2. El sistema muestra los primeros 15 Pokémon de ese tipo.

**Ejemplo de salida:**
```
-> Lista de tipo 'fire' descargada de la API.

Pokémon de tipo fire (primeros 15):
- Charmander
- Charmeleon
- Charizard
- Vulpix
- Ninetales
...
```

### Opción 3: Crear equipo

1. Ingresa un nombre único para el equipo.
2. El sistema te pedirá nombres de Pokémon uno por uno.
3. Cada Pokémon se valida: debe existir en la PokeAPI y no estar repetido.
4. El equipo se completa automáticamente al llegar a 6 integrantes.

**Ejemplo de flujo:**
```
Nombre del nuevo equipo: MiEquipo
Equipo 'MiEquipo' creado con éxito.
Ahora puedes agregar Pokémones al equipo 'MiEquipo'.
Nombre del Pokémon a agregar: pikachu
¡Pikachu agregado al equipo! (1/6)
Nombre del Pokémon a agregar: charizard
¡Charizard agregado al equipo! (2/6)
...
Equipo 'MiEquipo' completo con 6 integrantes.
```

### Opción 4: Ver equipos y métricas

Muestra todos los equipos con sus integrantes y métricas:

```
--- MiEquipo ---
- Pikachu | Tipo: electric | HP: 35
- Charizard | Tipo: fire | HP: 78
...
Integrantes: 6/6
Promedio de HP: 65.5
Tipo dominante: fire
```

### Opción 5: Guardar y salir

Guarda todos los equipos en `datos.json` y cierra la aplicación.

---

## Estructura de archivos

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Punto de entrada. Contiene el menú interactivo, el flujo principal de la aplicación y la lógica de creación de equipos con agregado inmediato de Pokémon. |
| `conexiones.py` | Gestiona las peticiones HTTP a la PokeAPI y el sistema de caché local. Incluye funciones para cargar/guardar caché y buscar Pokémon por nombre o tipo. |
| `funciones.py` | Lógica de negocio reutilizable: buscar Pokémon, crear equipos, agregar miembros con validaciones y generar resúmenes con métricas. |
| `almacenamiento.py` | Maneja la lectura y escritura de los equipos en `datos.json` usando `pathlib` para rutas robustas. |
| `validaciones.py` | Reglas de negocio: validación de entradas, límite de equipo (6), duplicados y cálculo de métricas (promedio HP, tipo dominante). |
| `analisis.ipynb` | Notebook de Jupyter con 3 celdas: carga de datos, resumen estadístico y generación de gráfico de barras por tipo. |
| `requirements.txt` | Lista de dependencias externas: requests, pandas, matplotlib, ipykernel. |
| `datos.json` | Archivo de persistencia generado al guardar los equipos. |
| `cache_pokemon.json` | Caché local de Pokémon consultados (se genera automáticamente). |
| `cache_tipos.json` | Caché local de listas de Pokémon por tipo (se genera automáticamente). |

---

## Flujo de la aplicación

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.py                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ iniciar_    │  │ ejecutar_   │  │ finalizar_aplicacion()  │  │
│  │ aplicacion()│  │ accion()    │  │                         │  │
│  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘  │
└─────────┼────────────────┼─────────────────────┼────────────────┘
          │                │                     │
          ▼                ▼                     ▼
┌─────────────────┐ ┌──────────────┐     ┌──────────────────┐
│ almacenamiento  │ │ funciones.py │     │ almacenamiento   │
│ .cargar_equipos │ │              │     │ .guardar_equipos │
│                 │ │ - buscar_    │     │                  │
│                 │ │   pokemon    │     │                  │
│                 │ │ - crear_     │     │                  │
│                 │ │   equipo     │     │                  │
│                 │ │ - agregar_   │     │                  │
│                 │ │   pokemon    │     │                  │
│                 │ │ - resumir_   │     │                  │
│                 │ │   equipos    │     │                  │
│                 │ └──────┬───────┘     │                  │
└─────────────────┘        │             └──────────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
      ┌──────────────┐ ┌──────────┐ ┌─────────────────┐
      │ conexiones   │ │validaciones│ │                 │
      │ .py          │ │ .py       │ │                 │
      │              │ │           │ │                 │
      │ - cargar_    │ │ - limpiar │ │                 │
      │   cache      │ │   _texto  │ │                 │
      │ - guardar_   │ │ - validar │ │                 │
      │   cache      │ │   _entrada│ │                 │
      │ - buscar_    │ │ - validar │ │                 │
      │   pokemon_   │ │   _cantidad│ │                 │
      │   por_nombre │ │ - validar │ │                 │
      │ - buscar_    │ │   _pokemon│ │                 │
      │   pokemon_   │ │   _repetido│ │                 │
      │   por_tipo   │ │ - calcular│ │                 │
      │              │ │   _indicadores│ │                 │
      └──────┬───────┘ └──────────┘ └─────────────────┘
             │
             ▼
      ┌──────────────┐
      │  PokeAPI     │
      │  (Internet)  │
      └──────────────┘
```

### Pasos del flujo

1. **Inicio**: `main.py` llama a `almacenamiento.cargar_equipos()` para cargar equipos existentes desde `datos.json`.
2. **Menú**: El usuario selecciona una opción del menú interactivo.
3. **Ejecución**: `ejecutar_accion()` despacha la acción según la opción elegida.
4. **Lógica**: `funciones.py` procesa la solicitud, consultando `conexiones.py` si es necesario.
5. **Validación**: `validaciones.py` aplica reglas de negocio antes de modificar datos.
6. **Persistencia**: Al salir, `almacenamiento.guardar_equipos()` guarda los equipos en `datos.json`.

---

## Dependencias

| Librería | Versión | Propósito |
|----------|---------|-----------|
| `requests` | 2.x | Realizar peticiones HTTP a la PokeAPI |
| `pandas` | 2.x | Análisis y manipulación de datos en el notebook |
| `matplotlib` | 3.x | Generación de gráficos de barras en el notebook |
| `ipykernel` | 6.x | Ejecutar el notebook de Jupyter |

---

## Archivos generados

Estos archivos se crean automáticamente al usar la aplicación:

| Archivo | Contenido | Cuándo se crea |
|---------|-----------|----------------|
| `datos.json` | Equipos creados con sus Pokémon y estadísticas | Al guardar y salir (opción 5) o al crear un equipo |
| `cache_pokemon.json` | Datos de Pokémon ya consultados | Al buscar un Pokémon por primera vez |
| `cache_tipos.json` | Listas de Pokémon por tipo ya consultadas | Al filtrar por tipo por primera vez |
| `grafico_<equipo>.png` | Gráfico de barras de distribución de tipos | Al ejecutar el notebook de análisis |

---

## Notebook de análisis

El archivo `analisis.ipynb` contiene 3 celdas de código:

### Celda 1: Carga de datos
- Importa las librerías necesarias (pandas, matplotlib, json, almacenamiento).
- Carga los equipos desde `datos.json`.
- Pide al usuario que seleccione un equipo para analizar.
- Muestra los primeros registros del equipo seleccionado.

### Celda 2: Resumen estadístico
- Muestra estadísticas generales (hp, peso, altura) con `describe()`.
- Identifica el Pokémon con mayor HP, el más pesado y el más alto.
- Muestra el conteo de tipos principales en el equipo.

### Celda 3: Visualización
- Genera un gráfico de barras con la distribución de tipos principales.
- Guarda el gráfico como `grafico_<equipo>.png` con resolución de 300 DPI.
- Muestra el gráfico en el notebook.

### Ejemplo de uso

```bash
jupyter notebook analisis.ipynb
```

1. Ejecuta la primera celda y escribe el nombre del equipo a analizar (ej: `MiEquipo`).
2. Ejecuta la segunda celda para ver las estadísticas.
3. Ejecuta la tercera celda para generar el gráfico.

---

## Registro de uso de IA

| Prompt | Estado | Verificación |
|--------|--------|--------------|
| "Cómo generar la conexión a la PokeAPI usando la librería requests con try/except." | Aceptado | Se probó buscar un Pokémon inexistente y cortar la conexión para verificar que el programa no colapse. |
| "Cómo leer un archivo JSON con Pandas, unificar tipo_1 y tipo_2 para contar la frecuencia y graficar un histograma con Matplotlib." | Aceptado | Se verificó la generación correcta del archivo grafico.png y que la notebook procesara el JSON incluso con valores nulos en tipo_2. |

---

## Notas adicionales

- **Caché**: Los archivos de caché (`cache_pokemon.json`, `cache_tipos.json`) se acumulan con el tiempo. Si deseas limpiarlos, simplemente elimínalos y se regenerarán automáticamente.
- **Validaciones**: El sistema no permite nombres de equipo vacíos, equipos duplicados (sin distinguir mayúsculas/minúsculas), más de 6 Pokémon por equipo o Pokémon repetidos en el mismo equipo.
- **Persistencia**: Los equipos se guardan automáticamente al crear un equipo y al salir de la aplicación.
- **Notebook**: El notebook requiere que `datos.json` exista y contenga al menos un equipo con Pokémon.
