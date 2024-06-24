'''
Elabore un script donde se puede leer un archivo de texto y que identifique un patrón, 
cuando hay una secuencia de números (1 o más números), donde haya una secuencia de números y letras 
(1 o más números seguidos de 1 o más letras), un patrón donde identifique letras que contengan un más de tres vocales iguales 
(por ejemplo: palabra o aab3a; tienen 3 vocales a, emisión o oaaee solo tiene 2  vocales i emision, 2 vocales a, 2 vocales e; 
por lo cual no cumple la condición), y por último que identifique si hay un carácter especial en la entrada 
(por ejemplo ssdsdk&sd* donde se encontró & y *). Haga uso de la biblioteca de Python para identificar patrones.
La salida debe mostrar un arreglo impreso de las ocurrencias encontradas o dar un mensaje que no encontró ninguna. 
De forma opcional puede mandar la salida en un txt o un archivo de Excel.
'''

import re
import json
import pandas as pd
from datetime import datetime


def identificarNumeros(texto):
    "un patrón, cuando hay una secuencia de números (1 o más números)"
    numeros = re.findall(r'\d+', texto).__len__()
    return numeros if numeros > 0 else "No se encontraron números"


def identificarNumeroLetras(texto):
    "una secuencia de números y letras (1 o más números seguidos de 1 o más letras)"
    numerosLetras = re.findall(r'\b\d+[a-zA-Z]+\b', texto).__len__()
    return numerosLetras if numerosLetras > 0 else "No se encontraron numeros con letras"


def identificarLetrasVocalesIguales(texto):
    "un patrón donde identifique letras que contengan un más de tres vocales iguales (por ejemplo: palabra o aab3a; tienen 3 vocales a"
    palabras = re.findall(r'\b\w+\b', texto, re.IGNORECASE)
    palabras_vocales = [palabra for palabra in palabras if any(palabra.lower().count(vocal) > 2 for vocal in 'aeiou')]    
    resultados = palabras_vocales.__len__()
    return resultados if resultados > 0 else "No se encontraron palabras con 3 vocales iguales"


def identificarCaracterEspecial(texto):
    "un a secuencia que identifique si hay un carácter especial en la entrada (por ejemplo ssdsdk&sd* donde se encontró & y *). "
    #Excluyendo los espacios y tambulaniones
    caracteres = re.findall(r'[^\w\s]', texto).__len__()
    return caracteres if caracteres > 0 else "No se encontraron caracteres especiales"


def identificarPatrones(texto):
    numeros = identificarNumeros(texto)
    numerosLetras = identificarNumeroLetras(texto)
    letrasVocalesIguales = identificarLetrasVocalesIguales(texto)
    caracteresEspeciales = identificarCaracterEspecial(texto)

    resultados = {
        'numeros': numeros,
        'numerosLetras': numerosLetras,
        'letras3oMasVocalesIguales': letrasVocalesIguales,
        'caracteresEspeciales': caracteresEspeciales
    }

    return resultados


def guardarResultados(resultados):
    guardar = input('Desea guardar los resultados en un archivo? (S/N): ')
    if guardar.upper() != 'S':
        return
    nombreArchivo = "resultados-" + datetime.now().strftime('%Y%m%d%H%M%S') + '.xlsx'
    df = pd.DataFrame(list(resultados.items()), columns=['Secuencia', '# de concidencias'])
    df.to_excel(nombreArchivo, index=False)
    print(f'Archivo {nombreArchivo} guardado con éxito')



def main():
    ruta_archivo = 'texto.txt'

    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        resultados = identificarPatrones(contenido)
        print (json.dumps(resultados, indent=4))

        guardarResultados(resultados)
        print('Proceso finalizado')

if __name__ == '__main__':
    main()