"""
Módulo principal: Flujo de ejecución interactivo por consola.
"""

import json
import os
import funciones as fn
import validaciones as val

ARCHIVO_EQUIPOS = "datos.json"


def cargar_equipos() -> dict:
    """Carga los equipos guardados en el archivo local."""
    if not os.path.exists(ARCHIVO_EQUIPOS):
        return {}
    try:
        with open(ARCHIVO_EQUIPOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def guardar_equipos(datos: dict) -> None:
    """Escribe los equipos en el archivo JSON local."""
    try:
        with open(ARCHIVO_EQUIPOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error al guardar equipos: {e}")


def mostrar_menu():
    """Despliega el menu de opciones."""
    print("\n--- GESTOR DE EQUIPOS POKEMON ---")
    print("1. Buscar Pokemon en la PokeAPI / Cache")
    print("2. Filtrar Pokemon por tipo")
    print("3. Crear nuevo equipo")
    print("4. Agregar Pokemon a un equipo")
    print("5. Listar equipos y ver metricas")
    print("6. Guardar y Salir")


def consultar_pokemon():
    """Consulta la ficha tecnica de un Pokemon individual."""
    nombre = input("Ingrese el nombre del Pokemon a buscar: ")
    if not val.validar_entrada_no_vacia(nombre):
        print("Error: El nombre no puede estar vacio.")
        return

    poke = fn.buscar_pokemon_por_nombre(nombre)
    if poke:
        print(f"\n--- Ficha de {poke['nombre'].capitalize()} ---")
        print(f"Tipo principal: {poke.get('tipo_principal')}")
        print(f"HP base:        {poke.get('hp')}")
        print(f"Peso:           {poke.get('peso')}")
        print(f"Altura:         {poke.get('altura')}")


def filtrar_por_tipo():
    """Obtiene y lista los nombres de Pokemon asociados a un tipo."""
    tipo = input("Ingrese el tipo elemental (ej: fire, water, electric): ")
    if not val.validar_entrada_no_vacia(tipo):
        print("Error: Debe ingresar un tipo valido.")
        return

    lista = fn.buscar_pokemon_por_tipo(tipo)
    if lista:
        print(f"\n--- Pokemon de tipo '{tipo.strip().lower()}' (Primeros 15) ---")
        for nombre in lista[:15]:
            print(f"- {nombre.capitalize()}")


def crear_equipo(datos: dict):
    """Registra una nueva clave de equipo en el diccionario."""
    nombre = input("Ingrese el nombre del nuevo equipo: ")
    if not val.validar_entrada_no_vacia(nombre):
        print("Error: El nombre no puede estar vacio.")
        return

    nombre_norm = val.limpiar_texto(nombre)
    if nombre_norm in [val.limpiar_texto(k) for k in datos.keys()]:
        print("Error: Ya existe un equipo con ese nombre.")
        return

    datos[nombre.strip()] = []
    print(f"Equipo '{nombre.strip()}' creado con exito.")


def agregar_pokemon(datos: dict):
    """Valida reglas e incorpora un Pokemon devuelto por la API al equipo."""
    if not datos:
        print("No hay equipos creados todavia.")
        return

    print("Equipos disponibles:", list(datos.keys()))
    equipo_nombre = input("Seleccione el nombre del equipo: ").strip()

    if equipo_nombre not in datos:
        print("Error: El equipo indicado no existe.")
        return

    equipo = datos[equipo_nombre]

    if not val.validar_limite_equipo(equipo):
        print("Error: El equipo ya alcanzo el limite maximo de 6 integrantes.")
        return

    nombre_pokemon = input("Ingrese el nombre del Pokemon a agregar: ")
    if not val.validar_entrada_no_vacia(nombre_pokemon):
        print("Error: Debe ingresar un nombre valido.")
        return

    if val.validar_pokemon_repetido(nombre_pokemon, equipo):
        print("Error: Este Pokemon ya esta en el equipo.")
        return

    poke = fn.buscar_pokemon_por_nombre(nombre_pokemon)
    if not poke:
        return

    equipo.append(poke)
    print(f"!{poke['nombre'].capitalize()} agregado al equipo '{equipo_nombre}'!")


def mostrar_equipos(datos: dict):
    """Muestra cada equipo con sus miembros y las metricas calculadas."""
    if not datos:
        print("No hay equipos registrados.")
        return

    for nombre_equipo, miembros in datos.items():
        print("\n==============================")
        print(f"EQUIPO: {nombre_equipo}")
        print("==============================")

        if not miembros:
            print("  (Sin integrantes)")
            continue

        for p in miembros:
            print(f"- {p['nombre'].capitalize()} | Tipo: {p.get('tipo_principal')} | HP: {p.get('hp')}")

        metricas = val.calcular_indicadores_equipo(miembros)
        print("\n--- Metricas del Equipo ---")
        print(f"Total integrantes: {metricas['total_integrantes']}/6")
        print(f"Promedio de HP:    {metricas['promedio_hp']}")
        print(f"Tipo dominante:    {metricas['tipo_dominante']}")


def main():
    equipos = cargar_equipos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            consultar_pokemon()
        elif opcion == "2":
            filtrar_por_tipo()
        elif opcion == "3":
            crear_equipo(equipos)
        elif opcion == "4":
            agregar_pokemon(equipos)
        elif opcion == "5":
            mostrar_equipos(equipos)
        elif opcion == "6":
            guardar_equipos(equipos)
            print("Datos guardados en 'datos.json'. Saliendo...")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()