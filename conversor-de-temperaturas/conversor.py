while True:
    while True:
        c_a_f_o_f_a_c = input("Que temperatura quieres convertir? (C/F): ").upper()

        if c_a_f_o_f_a_c == "C":
            input_celsius = float(input("Introduce la temperatura en grados Celsius: "))
            celsius_a_fahrenheit = (input_celsius * 9/5) + 32
            print(f"La temperatura en grados Fahrenheit es: {celsius_a_fahrenheit: .1f}")
            break
        elif c_a_f_o_f_a_c == "F":
            input_fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            fahrenheit_a_celsius = (input_fahrenheit - 32) * 5/9
            print(f"La temperatura en grados Celsius es: {fahrenheit_a_celsius: .1f}")
            break
        else:
            print("Por favor, introduzca una opción válida (C/F). ")
    otra_conversión = input("Desea realizar otra conversión? (S/N): ").upper()
    if otra_conversión != "S":
        print("¡Gracias por usar el conversor de temperaturas!")
        break