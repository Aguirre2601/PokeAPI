# Gestor de Equipos Pokémon (PokeAPI)

Aplicación de consola en Python que permite buscar Pokémon usando la [PokeAPI](https://pokeapi.co/), filtrarlos por tipo, crear equipos de hasta 6 miembros sin duplicados, y consultar métricas como el promedio de HP y el tipo dominante. Los datos se persisten localmente en archivos JSON y se utiliza un sistema de caché para evitar consultas repetidas a la API.

---

## Características

- **Buscar Pokémon** por nombre, mostrando tipo principal, HP, peso y altura.
- **Filtrar Pokémon por tipo** elemental (fuego, agua, eléctrico, etc.).
- **Crear equipos** personalizados con nombre único.
- **Agregar Pokémon** a un equipo con validaciones (máximo 6, sin duplicados).
- **Ver métricas** de cada equipo: total de integrantes, promedio de HP y tipo dominante.
- **Persistencia automática** en `datos.json` al salir de la aplicación.
- **Caché local** para evitar consultas repetidas a la PokeAPI.

---

## Requisitos Previos

| Requisito | Detalle |
|-----------|---------|
| **Python** | Versión 3.13 o superior |
| **pip** | Gestor de paquetes de Python (incluido por defecto) |
| **Conexión a internet** | Necesaria para consultar la PokeAPI por primera vez |
| **Entorno virtual** | Recomendado (`.venv`) |

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

Para iniciar la aplicación, ejecuta:

```bash
python main.py
```

Esto abrirá un menú interactivo en la consola:

```
--- GESTOR DE EQUIPOS POKÉMON ---
1. Buscar Pokémon
2. Filtrar por tipo
3. Crear equipo
4. Agregar Pokémon a un equipo
5. Ver equipos y métricas
6. Guardar y salir
```

### Uso del menú

| Opción | Acción | Entrada requerida |
|--------|--------|-------------------|
| **1** | Busca un Pokémon por nombre y muestra sus stats | Nombre del Pokémon (ej: `pikachu`) |
| **2** | Lista los primeros 15 Pokémon de un tipo | Tipo elemental (ej: `fire`) |
| **3** | Crea un nuevo equipo vacío | Nombre del equipo |
| **4** | Agrega un Pokémon a un equipo existente | Nombre del equipo + nombre del Pokémon |
| **5** | Muestra todos los equipos con sus métricas | Ninguna |
| **6** | Guarda los equipos en `datos.json` y sale | Ninguna |

---

## Estructura de Archivos

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Punto de entrada. Contiene el menú interactivo y el flujo principal de la aplicación. |
| `conexiones.py` | Gestiona las peticiones HTTP a la PokeAPI y el sistema de caché local (`cache_pokemon.json`, `cache_tipos.json`). |
| `funciones.py` | Lógica de negocio reutilizable: buscar Pokémon, crear equipos, agregar miembros y generar resúmenes. |
| `almacenamiento.py` | Maneja la lectura y escritura de los equipos en `datos.json`. |
| `validaciones.py` | Reglas de negocio: validación de entradas, límite de equipo, duplicados y cálculo de métricas. |
| `analisis.ipynb` | Notebook de Jupyter para exploración de datos con Pandas y visualizaciones con Matplotlib. |
| `requirements.txt` | Lista de dependencias externas necesarias. |
| `datos.json` | Archivo de persistencia generado al guardar los equipos. |
| `cache_pokemon.json` | Caché local de Pokémon consultados (se genera automáticamente). |
| `cache_tipos.json` | Caché local de listas de Pokémon por tipo (se genera automáticamente). |

---

## Flujo de la Aplicación

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  main.py    │────▶│ funciones.py │────▶│ conexiones.py   │
│  (menú)     │     │ (lógica)     │     │ (API + caché)   │
└─────────────┘     └──────────────┘     └─────────────────┘
       │                    │
       │                    ▼
       │            ┌──────────────┐
       │            │validaciones.py│
       │            │ (reglas)      │
       │            └──────────────┘
       ▼
┌──────────────────┐
│almacenamiento.py │
│ (datos.json)     │
└──────────────────┘
```

1. El usuario interactúa con el menú en `main.py`.
2. `main.py` llama a las funciones de `funciones.py` según la opción elegida.
3. `funciones.py` consulta `conexiones.py` para obtener datos de la PokeAPI (o caché).
4. `validaciones.py` aplica las reglas de negocio antes de modificar los equipos.
5. Al salir, `almacenamiento.py` persiste los equipos en `datos.json`.

---

## Dependencias

| Librería | Propósito |
|----------|-----------|
| `requests` | Realizar peticiones HTTP a la PokeAPI |
| `pandas` | Análisis y manipulación de datos en el notebook |
| `matplotlib` | Generación de gráficos en el notebook |
| `ipykernel` | Ejecutar el notebook de Jupyter |

---

## Archivos Generados

Estos archivos se crean automáticamente al usar la aplicación:

| Archivo | Contenido |
|---------|-----------|
| `datos.json` | Equipos creados con sus Pokémon y estadísticas |
| `cache_pokemon.json` | Datos de Pokémon ya consultados (evita llamadas repetidas a la API) |
| `cache_tipos.json` | Listas de Pokémon por tipo ya consultadas |

---

## Notebook de Análisis

El archivo `analisis.ipynb` está diseñado para:

- Cargar los datos generados en `datos.json` con **Pandas**.
- Calcular indicadores estadísticos (tipo más repetido, promedio de HP, etc.).
- Generar visualizaciones gráficas con **Matplotlib**.

Para ejecutarlo:

```bash
jupyter notebook analisis.ipynb
```

---

## Registro de Uso de IA

| Prompt | Estado | Verificación |
|--------|--------|--------------|
| "Cómo generar la conexión a la PokeAPI usando la librería requests con try/except." | Aceptado | Se probó buscar un Pokémon inexistente y cortar la conexión para verificar que el programa no colapse. |
