while True:
    while True:
        tipo = input("Ingrese el tipo de operación (+ - * /): ")
        if tipo in ['+', '-', '*', '/']:
            break
        print("Opción no válida, intente de nuevo")
    
    while True:
        try:
            num1 = int(input("Ingrese el primer número:  "))
            break
        except ValueError:
            print("Ingrese un número válido")
    
    while True:
        try:
            num2 = int(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Ingrese un número válido")
    
    if tipo == '+':
        print(f"El resultado de las sumas es: {num1 + num2}")
    elif tipo == '-':
        print(f"El resultado de la resta es: {num1 - num2}")
    elif tipo == '*':
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    else:
        print(f"El resultado de la división es: {num1/num2}")
    
    while True:
        otra = input("¿Desea realizar otra operación? (S/N): ").lower()
        if otra in ['s', 'n']:
            break
        print("Opción no válida, intente de nuevo")
    
    if otra == 'n':
        break