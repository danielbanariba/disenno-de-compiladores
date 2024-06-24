'''
Elabore una calculadora en Python que realice las operaciones de 
sumar, restar, multiplicar, dividir, calcule la raíz cuadrada. 
Considere las entradas de solo números (enteros y decimales sin el uso de “e”).
'''

import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)

def print_result(result):
    if isinstance(result, str):
        print(f"Resultado: {result}")
    else:
        # Convertir el resultado a entero si es un número entero
        if result.is_integer():
            print(f"Resultado: {int(result)}")
        else:
            print(f"Resultado: {result}")

def main():
    while True:
        print("\nCalculadora en Python")
        print("Seleccione la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raíz cuadrada")
        print("6. Salir")

        operacion = input("Ingrese el número de la operación: ")

        if operacion in ['1', '2', '3', '4']:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            if operacion == '1':
                print_result(sumar(a, b))
            elif operacion == '2':
                print_result(restar(a, b))
            elif operacion == '3':
                print_result(multiplicar(a, b))
            elif operacion == '4':
                print_result(dividir(a, b))
        elif operacion == '5':
            a = float(input("Ingrese el número: "))
            print_result(raiz_cuadrada(a))
        elif operacion == '6':
            print("Hasta la proxima")
            break
        else:
            print("Operación no válida")

if __name__ == "__main__":
    main()