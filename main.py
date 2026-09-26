"""Flujo de ejecución de la aplicación, invocado desde el notebook."""

import almacenamiento
import funciones


def iniciar_aplicacion() -> dict:
    """Carga el estado inicial de la aplicación."""
    return almacenamiento.cargar_equipos()


def ejecutar_accion(
    opcion: str,
    equipos: dict| None = None,
    entrada: str | None = None,
    nombre_equipo: str | None = None,
):
    """Despacha una acción y devuelve datos para que la interfaz los presente."""
    if opcion == "1":
        return funciones.buscar_pokemon(entrada or "")
    if opcion == "2":
        return funciones.buscar_pokemon_por_tipo(entrada or "")
    if opcion == "3":
        return funciones.crear_equipo(equipos, entrada or "")
    if opcion == "4":
        return funciones.agregar_pokemon(equipos, nombre_equipo or "", entrada or "")
    if opcion == "5":
        return funciones.resumir_equipos(equipos)
    return None


def finalizar_aplicacion(equipos: dict) -> tuple[bool, str]:
    """Persiste el estado final de la aplicación."""
    return almacenamiento.guardar_equipos(equipos)



equipos = iniciar_aplicacion()

while True:
    print("\n--- GESTOR DE EQUIPOS POKÉMON ---")
    print("1. Buscar Pokémon")
    print("2. Filtrar por tipo")
    print("3. Crear equipo")
    print("4. Agregar Pokémon a un equipo")
    print("5. Ver equipos y métricas")
    print("6. Guardar y salir")
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre del Pokémon: ").strip()
        if not nombre:
            print("Escribe un nombre de Pokémon.")
            continue
        pokemon = ejecutar_accion("1", entrada=nombre)
        if pokemon:
            print(f"\n{pokemon['nombre'].capitalize()}")
            print(f"Tipo principal: {pokemon.get('tipo_principal')}")
            print(f"HP: {pokemon.get('hp')}")
            print(f"Peso: {pokemon.get('peso')}")
            print(f"Altura: {pokemon.get('altura')}")

    elif opcion == "2":
        tipo = input("Tipo elemental (fire, water, electric...): ").strip()
        if not tipo:
            print("Escribe un tipo elemental.")
            continue
        pokemon_por_tipo = ejecutar_accion("2", entrada=tipo)
        if pokemon_por_tipo:
            print(f"\nPokémon de tipo {tipo.lower()} (primeros 15):")
            for nombre in pokemon_por_tipo[:15]:
                print(f"- {nombre.capitalize()}")

    elif opcion == "3":
        nombre = input("Nombre del nuevo equipo: ")
        _, mensaje = ejecutar_accion("3", equipos, entrada=nombre)
        print(mensaje)

    elif opcion == "4":
        if not equipos:
            print("Primero crea un equipo.")
            continue
        print("Equipos disponibles:", ", ".join(equipos))
        nombre_equipo = input("Equipo: ").strip()
        nombre_pokemon = input("Pokémon que quieres agregar: ").strip()
        pokemon, error = ejecutar_accion(
            "4", equipos, entrada=nombre_pokemon, nombre_equipo=nombre_equipo
        )
        print(error if error else f"{pokemon['nombre'].capitalize()} agregado a {nombre_equipo}.")

    elif opcion == "5":
        resumen = ejecutar_accion("5", equipos)
        if not resumen:
            print("No hay equipos registrados.")
            continue
        for equipo in resumen:
            print(f"\n--- {equipo['nombre']} ---")
            if not equipo['miembros']:
                print("(Sin integrantes)")
                continue
            for pokemon in equipo['miembros']:
                print(
                    f"- {pokemon['nombre'].capitalize()} | "
                    f"Tipo: {pokemon.get('tipo_principal')} | HP: {pokemon.get('hp')}"
                )
            metricas = equipo['metricas']
            print(f"Integrantes: {metricas['total_integrantes']}/6")
            print(f"Promedio de HP: {metricas['promedio_hp']}")
            print(f"Tipo dominante: {metricas['tipo_dominante']}")

    elif opcion == "6":
        _, mensaje = finalizar_aplicacion(equipos)
        print(mensaje)
        break

    else:
        print("Opción no válida.")