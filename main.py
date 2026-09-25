"""
Módulo principal: Flujo de ejecución interactivo por consola.
"""

import json
import os
import funciones
from validaciones import (
    limpiar_entrada,
    validar_texto_no_vacio,
    validar_pokemon_no_repetido,
    validar_limite_equipo,
    calcular_indicadores
)

ARCHIVO_DATOS = "datos.json"


def cargar_equipos(ruta_archivo: str = ARCHIVO_DATOS) -> list:
    """Lee y retorna la lista de equipos guardados en el JSON."""
    if not os.path.exists(ruta_archivo):
        return []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def guardar_equipos(equipos: list, ruta_archivo: str = ARCHIVO_DATOS) -> None:
    """Guarda la lista completa de equipos en el archivo JSON."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(equipos, f, indent=4, ensure_ascii=False)
        print("-> Datos actualizados correctamente en datos.json.")
    except IOError as e:
        print(f"Error al escribir en {ruta_archivo}: {e}")


def opcion_consultar_pokemon():
    nombre = input("Ingrese el nombre del Pokémon a buscar: ")
    nombre_limpio = limpiar_entrada(nombre)
    if not validar_texto_no_vacio(nombre_limpio):
        print("El nombre no puede estar vacío.")
        return

    poke = funciones.buscar_pokemon_por_nombre(nombre_limpio)
    if poke:
        print(f"\n--- Datos de {poke['nombre'].capitalize()} ---")
        print(f"Tipo: {poke['tipo_principal']} | HP: {poke['hp']} | Peso: {poke['peso']} | Altura: {poke['altura']}")


def opcion_filtrar_por_tipo():
    tipo = input("Ingrese el tipo a filtrar (ej. electric, fire, water): ")
    tipo_limpio = limpiar_entrada(tipo)
    if not validar_texto_no_vacio(tipo_limpio):
        print("El tipo no puede estar vacío.")
        return

    lista = funciones.buscar_pokemon_por_tipo(tipo_limpio)
    if lista:
        print(f"\nTotal encontrados: {len(lista)}")
        print(f"Primeros 10 Pokémon de tipo '{tipo_limpio}':")
        for p in lista[:10]:
            print(f"- {p}")


def opcion_crear_equipo(equipos: list):
    nombre_eq = input("Ingrese un nombre para su equipo: ").strip()
    if not validar_texto_no_vacio(nombre_eq):
        print("El nombre del equipo no puede estar vacío.")
        return

    integrantes = []
    print("\nComenzando la selección de integrantes (máximo 6)...")

    while validar_limite_equipo(integrantes, 6):
        print(f"\nIntegrantes cargados: {len(integrantes)}/6")
        nombre_poke = input("Nombre del Pokémon a incorporar: ")
        nombre_limpio = limpiar_entrada(nombre_poke)

        if not validar_texto_no_vacio(nombre_limpio):
            print("Entrada inválida.")
            continue

        if not validar_pokemon_no_repetido(nombre_limpio, integrantes):
            print("Error: Este Pokémon ya forma parte del equipo actual.")
            continue

        poke_datos = funciones.buscar_pokemon_por_nombre(nombre_limpio)
        if poke_datos:
            integrantes.append(poke_datos)
            print(f"¡{poke_datos['nombre'].capitalize()} agregado al equipo!")

        if 0 < len(integrantes) < 6:
            seguir = input("¿Desea agregar otro Pokémon? (s/n): ").strip().lower()
            if seguir != "s":
                break

    if not integrantes:
        print("No se agregaron integrantes. Operación cancelada.")
        return

    nuevo_id = len(equipos) + 1
    nuevo_equipo = {
        "idEquipo": nuevo_id,
        "nombreEquipo": nombre_eq,
        "Integrantes": integrantes
    }
    equipos.append(nuevo_equipo)
    guardar_equipos(equipos)
    print(f"Equipo '{nombre_eq}' guardado con éxito con {len(integrantes)} miembros.")


def opcion_modificar_equipo(equipos: list):
    if not equipos:
        print("No hay equipos creados para modificar.")
        return

    print("\nEquipos disponibles:")
    for eq in equipos:
        print(f"[{eq.get('idEquipo')}] {eq.get('nombreEquipo')} ({len(eq.get('Integrantes', []))} miembros)")

    id_str = input("\nIngrese el ID del equipo que desea modificar: ").strip()
    equipo_sel = next((eq for eq in equipos if str(eq.get("idEquipo")) == id_str), None)

    if not equipo_sel:
        print("ID no encontrado.")
        return

    integrantes = equipo_sel.get("Integrantes", [])
    print(f"\nIntegrantes actuales de '{equipo_sel.get('nombreEquipo')}':")
    for i, p in enumerate(integrantes, start=1):
        print(f"{i}. {p.get('nombre').capitalize()} (Tipo: {p.get('tipo_principal')}, HP: {p.get('hp')})")

    idx_str = input("Seleccione el número del integrante a reemplazar: ").strip()
    try:
        idx_cambiar = int(idx_str) - 1
        if idx_cambiar < 0 or idx_cambiar >= len(integrantes):
            print("Número de integrante fuera de rango.")
            return
    except ValueError:
        print("Entrada no válida.")
        return

    nuevo_nombre = input("Ingrese el nombre del nuevo Pokémon sustituto: ")
    nuevo_nombre_limpio = limpiar_entrada(nuevo_nombre)

    if not validar_texto_no_vacio(nuevo_nombre_limpio):
        print("Nombre inválido.")
        return

    # Validar que no esté repetido en el resto del equipo
    resto_equipo = [p for i, p in enumerate(integrantes) if i != idx_cambiar]
    if not validar_pokemon_no_repetido(nuevo_nombre_limpio, resto_equipo):
        print("Error: El nuevo Pokémon ya está en el equipo.")
        return

    poke_datos = funciones.buscar_pokemon_por_nombre(nuevo_nombre_limpio)
    if poke_datos:
        integrantes[idx_cambiar] = poke_datos
        guardar_equipos(equipos)
        print("Equipo modificado y guardado.")


def opcion_ver_indicadores(equipos: list):
    if not equipos:
        print("No hay equipos registrados para calcular estadísticas.")
        return

    for eq in equipos:
        integrantes = eq.get("Integrantes", [])
        metricas = calcular_indicadores(integrantes)
        print(f"\n==========================================")
        print(f"Equipo: {eq.get('nombreEquipo')} (ID: {eq.get('idEquipo')})")
        print(f"- Total de integrantes: {metricas['total']}")
        print(f"- Promedio de HP: {metricas['promedio_hp']}")
        print(f"- Tipo dominante: {metricas['tipo_dominante']}")
        print(f"==========================================")


def main():
    equipos = cargar_equipos()

    while True:
        print("\n=== SISTEMA DE GESTIÓN POKÉMON ===")
        print("1. Consultar Pokémon por nombre")
        print("2. Filtrar Pokémon por tipo")
        print("3. Crear nuevo equipo")
        print("4. Modificar equipo existente")
        print("5. Ver indicadores de equipos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            opcion_consultar_pokemon()
        elif opcion == "2":
            opcion_filtrar_por_tipo()
        elif opcion == "3":
            opcion_crear_equipo(equipos)
        elif opcion == "4":
            opcion_modificar_equipo(equipos)
        elif opcion == "5":
            opcion_ver_indicadores(equipos)
        elif opcion == "6":
            print("Cerrando la aplicación.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()