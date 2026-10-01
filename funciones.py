"""Operaciones reutilizables para la gestión de equipos Pokémon."""

import conexiones as cx
import validaciones as val


def buscar_pokemon(nombre: str) -> dict | None:
	"""Devuelve los datos de un Pokémon consultando la caché o la API."""
	return cx.buscar_pokemon_por_nombre(nombre)


def buscar_pokemon_por_tipo(tipo: str) -> list | None:
	"""Devuelve los nombres de Pokémon de un tipo."""
	return cx.buscar_pokemon_por_tipo(tipo)


def crear_equipo(equipos: dict, nombre: str) -> tuple[bool, str, str]:
	"""Crea un equipo si el nombre es válido y todavía no existe."""
	if not val.validar_entrada_no_vacia(nombre):
		return False, "El nombre del equipo no puede estar vacío.", ""

	nombre_limpio = nombre.strip()
	nombre_normalizado = val.limpiar_texto(nombre_limpio)
	if any(val.limpiar_texto(existente) == nombre_normalizado for existente in equipos):
		return False, f"Ya existe un equipo llamado '{nombre_limpio}'.", ""

	equipos[nombre_limpio] = []
	return True, f"Equipo '{nombre_limpio}' creado con éxito.", nombre_limpio


def agregar_pokemon(
	equipo: list,
	nombre_pokemon: str,
) -> tuple[dict | None, str | None]:
	"""
	Agrega un Pokémon a un equipo previamente creado.

	Valida que:
	- Existan equipos creados
	- El equipo indicado exista
	- El equipo no haya alcanzado el límite de 6 integrantes
	- El nombre del Pokémon no esté vacío
	- El Pokémon no esté ya en el equipo
	- El Pokémon exista en la API o caché

	Args:
		equipos: Diccionario con todos los equipos
		nombre_equipo: Nombre del equipo al que agregar
		nombre_pokemon: Nombre del Pokémon a agregar

	Returns:
		Tuple con (datos del Pokémon, None) si es exitoso,
		o (None, mensaje de error) si falla
	"""

	# Validar límite del equipo
	if not val.validar_cantidad_equipo(equipo):
		return None, f"El equipo ya tiene 6 integrantes (máximo permitido)."

	# Validar que el nombre no esté vacío
	if not val.validar_entrada_no_vacia(nombre_pokemon):
		return None, "Debes ingresar un nombre de Pokémon válido."

	# Validar que no esté repetido
	if val.validar_pokemon_repetido(nombre_pokemon, equipo):
		return None, f"'{nombre_pokemon.capitalize()}' ya está en este equipo."

	# Buscar el Pokémon en la API o caché
	pokemon = buscar_pokemon(nombre_pokemon)
	if pokemon is None:
		return None, f"No se encontró el Pokémon '{nombre_pokemon}'. Verifica el nombre e intenta de nuevo."

	# Agregar al equipo
	equipo.append(pokemon)
	return pokemon, None


def resumir_equipos(equipos: dict) -> list[dict]:
	"""Devuelve los integrantes y las métricas de cada equipo."""
	return [
		{
			"nombre": nombre,
			"miembros": miembros,
			"metricas": val.calcular_indicadores_equipo(miembros),
		}
		for nombre, miembros in equipos.items()
	]
