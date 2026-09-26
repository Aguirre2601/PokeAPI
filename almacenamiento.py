"""Lectura y escritura de equipos en el archivo JSON local."""

import json
from pathlib import Path


ARCHIVO_EQUIPOS = Path(__file__).with_name("datos.json")


def cargar_equipos() -> dict:
    """Carga los equipos guardados; devuelve un diccionario vacío si no existen."""
    if not ARCHIVO_EQUIPOS.exists():
        return {}

    try:
        with ARCHIVO_EQUIPOS.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return {}


def guardar_equipos(equipos: dict) -> tuple[bool, str]:
    """Guarda los equipos y devuelve el resultado sin imprimir en consola."""
    try:
        with ARCHIVO_EQUIPOS.open("w", encoding="utf-8") as archivo:
            json.dump(equipos, archivo, indent=4, ensure_ascii=False)
    except OSError as error:
        return False, f"Error al guardar los equipos: {error}"

    return True, "Datos guardados en 'datos.json'."