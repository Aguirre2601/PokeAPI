"""Operaciones reutilizables para la gestión de equipos Pokémon."""

import conexiones as cx
import validaciones as val


def buscar_pokemon(nombre: str) -> dict | None:
	"""Devuelve los datos de un Pokémon consultando la caché o la API."""
	return cx.buscar_pokemon_por_nombre(nombre)


def buscar_pokemon_por_tipo(tipo: str) -> list | None:
	"""Devuelve los nombres de Pokémon de un tipo."""
	return cx.buscar_pokemon_por_tipo(tipo)


def crear_equipo(equipos: dict, nombre: str) -> tuple[bool, str]:
	"""Crea un equipo si el nombre es válido y todavía no existe."""
	if not val.validar_entrada_no_vacia(nombre):
		return False, "El nombre del equipo no puede estar vacío."

	nombre_limpio = nombre.strip()
	nombre_normalizado = val.limpiar_texto(nombre_limpio)
	if any(val.limpiar_texto(existente) == nombre_normalizado for existente in equipos):
		return False, f"Ya existe un equipo llamado '{nombre_limpio}'."

	equipos[nombre_limpio] = []
	return True, f"Equipo '{nombre_limpio}' creado con éxito."


def agregar_pokemon(
	equipos: dict,
	nombre_equipo: str,
	nombre_pokemon: str,
) -> tuple[dict | None, str | None]:
	"""Agrega un Pokémon validado al equipo indicado."""
	if not equipos:
		return None, "No hay equipos creados todavía."

	if nombre_equipo not in equipos:
		return None, "El equipo indicado no existe."

	equipo = equipos[nombre_equipo]
	if not val.validar_limite_equipo(equipo):
		return None, "El equipo ya alcanzó el límite máximo de 6 integrantes."

	if not val.validar_entrada_no_vacia(nombre_pokemon):
		return None, "Debe ingresar un nombre de Pokémon válido."

	if val.validar_pokemon_repetido(nombre_pokemon, equipo):
		return None, "Este Pokémon ya está en el equipo."

	pokemon = buscar_pokemon(nombre_pokemon)
	if pokemon is None:
		return None, "No se pudo agregar el Pokémon."

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
