def binario_a_decimal(numero):
    return int(numero, 2)

def decimal_a_binario(numero):
    return bin(numero)[2:]

def suma_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) + binario_a_decimal(b))

def resta_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) - binario_a_decimal(b))

def multiplicacion_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) * binario_a_decimal(b))

def division_binaria(a, b):
    return decimal_a_binario(binario_a_decimal(a) / binario_a_decimal(b))

print("Calculadora binaria")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Elige una opción: ")

if opcion == "1":
    a = input("Ingresa el primer número binario: ")
    b = input("Ingresa el segundo número binario: ")
    print("El resultado de la suma es:", suma_binaria(a, b))

elif opcion == "2":
    a = input("Ingresa el primer número binario: ")
    b = input("Ingresa el segundo número binario: ")
    print("El resultado de la resta es:", resta_binaria(a, b))

elif opcion == "3":
    a = input("Ingresa el primer número binario: ")
    b = input("Ingresa el segundo número binario: ")
    print("El resultado de la multiplicación es:", multiplicacion_binaria(a, b))

elif opcion == "4":
    a = input("Ingresa el primer número binario: ")
    b = input("Ingresa el segundo número binario: ")
    print("El resultado de la división es:", division_binaria(a, b))

else:
    print("Opción inválida")1