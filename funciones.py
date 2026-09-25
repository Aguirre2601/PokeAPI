##funciones.py-> Funciones propias y lógica reutilizable.

import requests
import json
import os

# Definimos constantes para los nombres de nuestros archivos de caché
ARCHIVO_CACHE_POKEMON = "cache_pokemon.json"
ARCHIVO_CACHE_TIPOS = "cache_tipos.json"

def cargar_cache(nombre_archivo: str) -> dict:
    """
    Intenta cargar un diccionario desde un archivo JSON local.
    Si el archivo no existe, devuelve un diccionario vacío.
    """
    if not os.path.exists(nombre_archivo):
        return {}
        
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError):
        return {}

def guardar_cache(datos: dict, nombre_archivo: str) -> None:
    """
    Toma un diccionario y lo guarda en el disco duro en formato JSON.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error al intentar guardar en caché: {e}")

def buscar_pokemon_por_nombre(nombre: str) -> dict | None:
    """
    Busca un Pokémon por nombre usando caché local para evitar consultas repetidas.
    """
    nombre_formateado = nombre.strip().lower()
    cache_actual = cargar_cache(ARCHIVO_CACHE_POKEMON)
    
    if nombre_formateado in cache_actual:
        print(f"-> ¡{nombre_formateado.capitalize()} encontrado en caché!")
        return cache_actual[nombre_formateado]
    
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_formateado}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos_crudos = respuesta.json()
        
        # Limpieza: guardamos solo lo necesario para calcular indicadores luego
        pokemon_limpio = {
            "nombre": datos_crudos["name"],
            "tipo_principal": datos_crudos["types"][0]["type"]["name"],
            "peso": datos_crudos["weight"],
            "altura": datos_crudos["height"],
            "hp": datos_crudos["stats"][0]["base_stat"]
        }
        
        cache_actual[nombre_formateado] = pokemon_limpio
        guardar_cache(cache_actual, ARCHIVO_CACHE_POKEMON)
        
        print(f"-> {nombre_formateado.capitalize()} descargado de la API.")
        return pokemon_limpio
        
    except requests.exceptions.HTTPError:
        print(f"Error: No se encontró el Pokémon '{nombre}'.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error de red: {e}")
        return None

def buscar_pokemon_por_tipo(tipo: str) -> list | None:
    """
    Busca todos los Pokémon de un tipo específico (ej: 'electric').
    Utiliza caché local para optimizar las consultas.
    """
    tipo_formateado = tipo.strip().lower()
    cache_tipos = cargar_cache(ARCHIVO_CACHE_TIPOS)
    
    if tipo_formateado in cache_tipos:
        print(f"-> Lista de tipo '{tipo_formateado}' cargada desde caché.")
        return cache_tipos[tipo_formateado]
        
    url = f"https://pokeapi.co/api/v2/type/{tipo_formateado}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos_crudos = respuesta.json()
        
        # Extraemos solo los nombres de la lista compleja que devuelve la API
        lista_nombres = []
        for item in datos_crudos["pokemon"]:
            lista_nombres.append(item["pokemon"]["name"])
            
        cache_tipos[tipo_formateado] = lista_nombres
        guardar_cache(cache_tipos, ARCHIVO_CACHE_TIPOS)
        
        print(f"-> Lista de tipo '{tipo_formateado}' descargada de la API.")
        return lista_nombres
        
    except requests.exceptions.HTTPError:
        print(f"Error: No se encontró el tipo '{tipo}'.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error de red: {e}")
        return None