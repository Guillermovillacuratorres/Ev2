opc = 0

while True:
    print("=== MENÚ ===")
    print("[1] - Más opciones")
    print("[2] - Opción 2")
    print("[3] - Salir")

    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print("Opcion no valida!")
        continue

    if opc == 1:
        while True:
            print("=== MENÚ  2 ===")
            print("[1] - Opción 1")
            print("[2] - Salir")
            opc2 = int(input("Seleccione una opción: "))

            if opc2 == 1:
                print("Opción menu del menu 1")
            if opc2 == 2:
                print("Saliendo!!")
                break
    elif opc == 2:
        print("opcion 2")
    elif opc == 3:
        break