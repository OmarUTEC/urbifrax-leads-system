def prompt_input(mensaje, validator=None):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("El campo no puede estar vacío.")
            continue
        if validator:
            if validator(valor):
                return valor
            else:
                print("Entrada inválida.")
                continue
        return valor

def choose(mensaje, opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}) {opcion}")
    while True:
        try:
            eleccion = int(input(mensaje))
            if 1 <= eleccion <= len(opciones):
                return opciones[eleccion - 1]
        except ValueError:
            pass
        print("Opción inválida.")

def validate_phone(phone):
    return len(phone) >= 7

def validate_email(email):
    return "@" in email