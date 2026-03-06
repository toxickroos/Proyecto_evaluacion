print("Hola, Usuario.\nBienvenido al sistema de aprobacion de prestamos del banco MONKEX")

while True:
    # 1. Bucle exclusivo para validar el salario
    while True:
        try:
            ingresos_mensuales = float(input("\nIngresa tu salario mensual: "))
            if ingresos_mensuales <= 0:
                print("El salario debe ser mayor a 0.")
                continue # Vuelve a preguntar
            break # Si el dato es correcto, rompe este mini-bucle y avanza
        except ValueError:
            print("Error: Introduce un monto numérico válido.")
  
    # 2. Bucle exclusivo para validar el préstamo
    while True:
        try:
            prestamo_solicitado = float(input("Ahora ingresa el monto del prestamo que deseas solicitar: "))
            if prestamo_solicitado <= 0:
                print("El préstamo debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: Digite un monto numérico válido.")
    
    # 3. Lógica de Negocio
    validacion = ingresos_mensuales * 5
    
    # CORRECCIÓN: El préstamo debe ser menor o igual al límite permitido
    if prestamo_solicitado <= validacion:
        # Usamos f-strings para imprimir más fácil
        print(f"\nSeñor@ usuario, su prestamo por ${prestamo_solicitado:,.2f} ha sido APROBADO.")
        
        # Mostramos cuánto le quedaría de límite
        saldo_restante = validacion - prestamo_solicitado
        print(f"Le recordamos que su límite máximo era de ${validacion:,.2f}.")
        print(f"Aún tiene una capacidad de endeudamiento de ${saldo_restante:,.2f}.")
        
    else:
        print("\nEl prestamo NO puede ser realizado.")
        print(f"Su monto solicitado (${prestamo_solicitado:,.2f}) es muy elevado.")
        print(f"El monto máximo de préstamo que puede solicitar es ${validacion:,.2f}.")

    # 4. Bucle exclusivo para preguntar si desea continuar
    while True:
        try:
            ans1 = int(input("\n¿Desea realizar otra consulta?\n1) Si\n2) No\nElija una opción: "))
            if ans1 in [1, 2]: # Forma elegante de verificar si es 1 o 2
                break
            else:
                print("Digite una opcion valida (1 o 2).")        
        except ValueError:
            print("Error: Digite un numero valido (1 o 2).")
            
    # 5. Evaluar la respuesta para salir del programa
    if ans1 == 2:
        print("\nGracias por utilizar el banco MONKEX. ¡Hasta pronto!")
        break 
    # Si ans1 es 1, el bucle principal 'while True' simplemente vuelve a empezar