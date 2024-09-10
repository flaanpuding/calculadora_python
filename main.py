from calculadora import suma, resta, multiplicacion, division

def menu():
    print("Menú Calculadora, opciones: \n"
          "1. Sumar \n"
          "2. Restar \n"
          "3. Multiplicar \n"
          "4. División ")
    opcion = int(input("Ingrese opción, 1, 2, 3 o 4: "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"La suma es: {suma(a, b)}")

    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"La resta es: {resta(a, b)}")

    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"La multiplicación es: {multiplicacion(a, b)}")

    elif opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"La división es: {division(a, b)}")

    else:
        print("Opción inválida")

# Llamamos al menú
menu()
