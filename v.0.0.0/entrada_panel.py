from pathlib import Path
from collections import Counter
from organizador import *


def contar_extenciones():
    archivos_existente = verificar_archivos_existentes()
    contador = Counter(p.suffix.lower() for p in archivos_existente)
    for ext, cantidad in contador.items():
        print(f"{ext}: {cantidad}")

def entrada1():
    cantidad_archivos = len(verificar_archivos_existentes())
    print(f'Existen {cantidad_archivos} archivos')
    contar_extenciones()

def entrada2():
    organizar()
    print('Archivos organizados')


def en_caso_de_duplicados(archivo, carpeta):
    
    prit(f"en la carpeta {carpeta.name} hay archivos con el mismo nombre {archivo.name}")
    entrada = input('''
    1. verificar si se trata de los mismos, por el peso de los archivos
    2. sobrescribir
    ''')
    match entrada:
        case '1':
            pass
        case '2':
            sobrescribir(archivo, carpeta)