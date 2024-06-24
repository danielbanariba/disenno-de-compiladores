'''
Elabore un convertidor de números donde se puede seleccionar la opción de entrada (binario, octal, decimal y hexadecimal) 
se ingrese el valor y después se seleccione una salida (binaria, octal, decimal o hexadecimal).
'''

## definicion de funciones
## convertir de decimal a hexadecimal
def dec_a_hex(numero):
    numero = int(numero)
    return hex(numero)[2:]

## convertir de decimal a octal
def dec_a_oct(numero):
    numero = int(numero)
    return oct(numero)[2:]

## convertir de decimal a binario
def dec_a_bin(numero):
    numero = int(numero)
    return bin(numero)[2:]

##convertir de hexadecimal a decimal
def hex_a_dec(numero):
    return int(numero, 16)

##convertir de hexadecimal a octal
def hex_a_oct(numero):
    dec = hex_a_dec(numero)
    return dec_a_oct(dec) 

##convertir de hexadecimal a bunario
def hex_a_bin(numero):
    dec = hex_a_dec(numero)
    return dec_a_bin(dec)

##convertir de octal a decimal
def oct_a_dec(numero):
    return int(numero, 8)

##convertir de octal a hexadecimal
def oct_a_hex(numero):
    dec = oct_a_dec(numero)
    return dec_a_hex(dec)

##convertir de octal a binario
def oct_a_bin(numero):
    dec = oct_a_dec(numero)
    return dec_a_bin(dec)

##convertir de binario a decimal
def bin_a_dec(numero):
    return int(numero, 2)

##convertir de binario a hexadecimal
def bin_a_hex(numero):
    dec = bin_a_dec(numero)
    return dec_a_hex(dec)

##convertir de binario a octal
def bin_a_oct(numero):
    dec = bin_a_dec(numero)
    return dec_a_oct(dec)


##definir la funcion principal
def main():
    while True:

        ##entrada
        print("\nSeleccione una opción de entrada:")
        print("1. Decimal")
        print("2. Hexadecimal")
        print("3. Octal")
        print("4. Binario")
        print("5. Salir")
        
        opcion1 = input("Ingrese el número de la opción deseada: \n")
        
        ##elemento a convertir
        numero = input("Ingrese el Numero a Convertir: \n")

        ##salida
        print("\nSeleccione una opción de salida:")
        print("1. Decimal")
        print("2. Hexadecimal")
        print("3. Octal")
        print("4. Binario")
        print("5. Cancelar")

        opcion2 = input("Ingrese el número de la opción deseada: \n")

        ##convertir desde decimal
        if opcion1 == '1' :
            if   opcion2 == '1': 
                print("Dec a Dec: {numero}")
            elif opcion2 == '2': 
                print(f"Dec a Hex: {dec_a_hex(numero)}")
            elif opcion2 == '3': 
                print(f"Dec a Oct: {dec_a_oct(numero)}")
            elif opcion2 == '4': 
                print(f"Dec a Bin: {dec_a_bin(numero)}")
            elif opcion2 == '5':
                print("Cancelado.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        ##convertir desde hexadecimal
        elif opcion1 == '2':
            if   opcion2 == '1':
                print(f"Hex a Dec: {hex_a_dec(numero)}")
            elif opcion2 == '2': 
                print("Hex a Hex: {numero}")
            elif opcion2 == '3': 
                print(f"Hex a Oct: {hex_a_oct(numero)}")
            elif opcion2 == '4':
                print(f"Hex a Bin: {hex_a_bin(numero)}")
            elif opcion2 == '5':
                print("Cancelado.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        
        ##convertir desde octal
        elif opcion1 == '3':
            if   opcion2 == '1':
                print(f"Oct a Dec: {oct_a_dec(numero)}")
            elif opcion2 == '2': 
                print(f"Oct a Hex: {oct_a_hex(numero)}")
            elif opcion2 == '3': 
                print("Oct a Oct: {numero}")
            elif opcion2 == '4':
                print(f"Oct a Bin: {oct_a_bin(numero)}")
            elif opcion2 == '5':
                print("Cancelado.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        ##convertir desde binario
        elif opcion1 == '4':
            if   opcion2 == '1':
                print(f"Bin a Dec: {bin_a_hex(numero)}")
            elif opcion2 == '2': 
                print(f"Bin a Hex: {bin_a_hex(numero)}")
            elif opcion2 == '3': 
                print(f"Bin a Oct: {bin_a_oct(numero)}")
            elif opcion2 == '4':
                print("Bin a Bin: {numero}")
            elif opcion2 == '5':
                print("Cancelado.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        elif opcion1 == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()


