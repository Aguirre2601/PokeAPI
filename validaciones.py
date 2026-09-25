"""
Módulo de validaciones, reglas de negocio e indicadores.
Responsable: Integrante 2 (Lógica & Validaciones).
"""

def limpiar_entrada(texto: str) -> str:
    """Elimina espacios en blanco sobrantes y convierte a minúsculas."""
    if not texto:
        return ""
    return texto.strip().lower()


def validar_texto_no_vacio(texto: str) -> bool:
    """Verifica que el string no esté vacío ni compuesto solo por espacios."""
    return bool(texto and texto.strip())


def validar_pokemon_no_repetido(nombre_pokemon: str, equipo: list) -> bool:
    """
    Verifica que el Pokémon no se encuentre ya en la lista del equipo.
    Compara nombres normalizados en minúsculas.
    """
    nombre_limpio = limpiar_entrada(nombre_pokemon)
    for poke in equipo:
        if poke.get("nombre", "").lower() == nombre_limpio:
            return False
    return True


def validar_limite_equipo(equipo: list, limite_max: int = 6) -> bool:
    """Verifica que la cantidad de integrantes no supere el límite máximo (6)."""
    return len(equipo) < limite_max


def calcular_indicadores(integrantes: list) -> dict:
    """
    Calcula 3 indicadores clave sobre un equipo:
    1. Total de Pokémon integrantes.
    2. Promedio de puntos de vida (HP) o peso.
    3. Tipo dominante (el que más se repite).
    """
    total = len(integrantes)
    if total == 0:
        return {
            "total": 0,
            "promedio_hp": 0.0,
            "tipo_dominante": "Ninguno"
        }

    # 1. Promedio de HP (campo 'hp' extraído de funciones.py)
    suma_hp = sum(poke.get("hp", 0) for poke in integrantes)
    promedio_hp = round(suma_hp / total, 2)

    # 2. Tipo dominante
    conteo_tipos = {}
    for poke in integrantes:
        tipo = poke.get("tipo_principal", "desconocido")
        conteo_tipos[tipo] = conteo_tipos.get(tipo, 0) + 1

    tipo_dominante = max(conteo_tipos, key=conteo_tipos.get)

    return {
        "total": total,
        "promedio_hp": promedio_hp,
        "tipo_dominante": tipo_dominante
    }