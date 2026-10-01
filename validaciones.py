"""
Módulo de validaciones, reglas de negocio e indicadores.
"""

def limpiar_texto(texto: str) -> str:
    """Elimina espacios en blanco en los extremos y pasa a minusculas."""
    if not isinstance(texto, str):
        return ""
    return texto.strip().lower()


def validar_entrada_no_vacia(texto: str) -> bool:
    """Verifica que la cadena no sea nula ni contenga unicamente espacios."""
    return bool(texto and texto.strip())


def validar_limite_equipo(equipo: list ) -> bool:
    """Comprueba que el equipo no supere la cantidad maxima permitida."""
    """maximo: int = 6"""
    return len(equipo) < 6


def validar_pokemon_repetido(nombre_pokemon: str, equipo: list) -> bool:
    """Verifica si el Pokemon ya se encuentra en la lista del equipo."""
    nombre_norm = limpiar_texto(nombre_pokemon)
    for p in equipo:
        if limpiar_texto(p.get("nombre", "")) == nombre_norm:
            return True
    return False


def calcular_indicadores_equipo(equipo: list) -> dict:
    """Calcula total de integrantes, promedio de HP y tipo dominante."""
    total = len(equipo)
    if total == 0:
        return {
            "total_integrantes": 0,
            "promedio_hp": 0.0,
            "tipo_dominante": "N/A"
        }

    suma_hp = sum(p.get("hp", 0) for p in equipo)
    promedio_hp = round(suma_hp / total, 2)

    conteo_tipos = {}
    for p in equipo:
        tipo = p.get("tipo_principal")
        if tipo:
            conteo_tipos[tipo] = conteo_tipos.get(tipo, 0) + 1

    tipo_dominante = max(conteo_tipos, key=conteo_tipos.get) if conteo_tipos else "Desconocido"

    return {
        "total_integrantes": total,
        "promedio_hp": promedio_hp,
        "tipo_dominante": tipo_dominante
    }