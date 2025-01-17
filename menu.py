opc = 0

while True:
    print("=== MENÚ ===")
    print("[1] - Opción 1")
    print("[2] - Opción 2")
    print("[3] - Salir")

    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print("Opcion no valida!")
        continue

    if opc == 1:
        print("opcion 1")
    elif opc == 2:
        print("opcion 2")
    elif opc == 3:
        break