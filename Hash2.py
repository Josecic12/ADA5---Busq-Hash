def control_asistencia():
    asistencia = set()

    print("Bienvenido al sistema de control de asistencia.")
    while True:
        print("\nOpciones disponibles:")
        print("1. Registrar asistencia")
        print("2. Verificar asistencia")
        print("3. Salir")
        
        accion = input("Elige una opción (1/2/3): ").strip()
        
        if accion == "3":
            print("Saliendo del sistema de asistencia. Nos vemos luegos")
            break
        elif accion == "1":
            id_estudiante = input("Ingresa el ID del estudiante: ").strip()
            if id_estudiante in asistencia:
                print(f"El estudiante con ID {id_estudiante} ya tiene registrada su asistencia.")
            else:
                asistencia.add(id_estudiante)
                print(f"Asistencia registrada para el ID {id_estudiante}.")
        elif accion == "2":
            id_estudiante = input("Ingresa el ID del estudiante: ").strip()
            if id_estudiante in asistencia:
                print(f"El estudiante con ID {id_estudiante} asistió.")
            else:
                print(f"No hay registro de asistencia para el ID {id_estudiante}.")
        else:
            print("Opción no válida. Por favor, elige una opción válida (1, 2 o 3).")

control_asistencia()
