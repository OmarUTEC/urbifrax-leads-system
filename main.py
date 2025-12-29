from typing import List

import leads
import utils


ORIGENES = ["web", "whatsapp", "referido"]
INTERESES = ["lotes", "inversión", "asesoría"]
ESTADOS = ["nuevo", "contactado", "interesado", "cerrado"]


def mostrar_leads(lista: List[dict]) -> None:
    if not lista:
        print("No hay leads para mostrar.")
        return
    for l in lista:
        print("-" * 40)
        print(f"ID: {l.get('id')}")
        print(f"Nombre: {l.get('nombre')}")
        print(f"Teléfono: {l.get('telefono')}")
        print(f"Correo: {l.get('correo')}")
        print(f"Origen: {l.get('origen')}")
        print(f"Interés: {l.get('interes')}")
        print(f"Estado: {l.get('estado')}")
        print(f"Creado: {l.get('created_at')}")


def registrar_lead() -> None:
    print("Registrar nuevo lead")
    nombre = utils.prompt_input("Nombre: ")
    telefono = utils.prompt_input("Teléfono: ", validator=utils.validate_phone)
    correo = utils.prompt_input("Correo: ", validator=utils.validate_email)
    origen = utils.choose("Elige origen: ", ORIGENES)
    interes = utils.choose("Elige interés: ", INTERESES)
    estado = utils.choose("Elige estado: ", ESTADOS)

    l = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "origen": origen,
        "interes": interes,
        "estado": estado,
    }
    added = leads.add_lead(l)
    print(f"Lead registrado con ID {added.get('id')}")


def listar_menu() -> None:
    print("1) Mostrar todos")
    print("2) Filtrar por estado")
    print("3) Filtrar por origen")
    opt = input("Opción: ").strip()
    if opt == "1":
        mostrar_leads(leads.get_all_leads())
    elif opt == "2":
        estado = utils.choose("Elige estado: ", ESTADOS)
        mostrar_leads(leads.filter_by_state(estado))
    elif opt == "3":
        origen = utils.choose("Elige origen: ", ORIGENES)
        mostrar_leads(leads.filter_by_origin(origen))
    else:
        print("Opción inválida.")


def buscar_menu() -> None:
    print("1) Buscar por nombre")
    print("2) Buscar por teléfono")
    opt = input("Opción: ").strip()
    if opt == "1":
        q = utils.prompt_input("Nombre a buscar: ")
        res = leads.find_by_name(q)
        mostrar_leads(res)
    elif opt == "2":
        q = utils.prompt_input("Teléfono a buscar: ")
        res = leads.find_by_phone(q)
        if res:
            mostrar_leads([res])
        else:
            print("No se encontró ningún lead con ese teléfono.")
    else:
        print("Opción inválida.")


def main_loop() -> None:
    print("Sistema de Leads - Urbifrax (consola)")
    while True:
        print("\nMenú:")
        print("1) Registrar lead")
        print("2) Listar leads")
        print("3) Buscar lead")
        print("4) Salir")
        opt = input("Elige opción: ").strip()
        if opt == "1":
            registrar_lead()
        elif opt == "2":
            listar_menu()
        elif opt == "3":
            buscar_menu()
        elif opt == "4":
            print("Hasta luego")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main_loop()
