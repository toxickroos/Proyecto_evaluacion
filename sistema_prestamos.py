print("Hola, Usuario.\nBienvenido al sistema de aprobacion de prestamos del banco MONKEX")

while True:
    # 1. Ingreso y validación del salario
    while True:
        try:
            ingresos_mensuales = float(input("\nIngresa tu salario mensual: "))
            if ingresos_mensuales > 0:
                break # Sale del bucle si el dato es válido y mayor a cero
            else:
                print("Error, el salario debe ser mayor a 0.")
        except ValueError:
            print("Error, Introduce un monto valido (solo números).")

    # 2. Ingreso y validación del monto del préstamo
    while True:
        try:
            prestamo_solicitado = float(input("Ahora ingresa el monto del prestamo que deseas solicitar: "))
            if prestamo_solicitado > 0:
                break # Sale del bucle si el dato es válido y mayor a cero
            else:
                print("Error, el monto debe ser mayor a 0.")
        except ValueError:
            print("Error, Digite un monto valido (solo números).")

    # 3. Cálculo de la validación (límite de préstamo)
    validacion = ingresos_mensuales * 5

    # 4. Lógica de aprobación o rechazo
    if prestamo_solicitado <= validacion:
        saldo_restante = validacion - prestamo_solicitado
        # Se agrega :,.2f a las variables para formato de dinero
        print(f"\n¡APROBADO! Señor@ usuario, su prestamo por ${prestamo_solicitado:,.2f} ha sido aprobado.")
        print(f"Su saldo de endeudamiento restante es: ${saldo_restante:,.2f}")
    else:
        print(f"\nRECHAZADO: El prestamo no puede ser realizado, su monto solicitado es muy elevado.")
        # Se agrega :,.2f para mostrar el límite en formato de dinero
        print(f"El limite maximo permitido para su salario es: ${validacion:,.2f}")

    # 5. Pregunta para reiniciar el ciclo de servicio
    while True:
        try:
            ans1 = int(input("\n¿Desea realizar otra consulta?\n1) Si\n2) No\nElige una opción: "))
            if ans1 == 1 or ans1 == 2:
                break # Sale del bucle de pregunta si ingresa 1 o 2
            else:
                print("Opción inválida. Digite 1 o 2.")
        except ValueError:
            print("Error. Digite una opción válida (números 1 o 2).")

    # Evaluar la respuesta para salir o continuar
    if ans1 == 2:
        print("\nGracias por usar el sistema del banco MONKEX. ¡Hasta pronto!")
        break