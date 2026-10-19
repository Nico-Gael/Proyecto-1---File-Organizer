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
    pass
