from organizador import *
from entrada_panel import *


print("Hola, bienvenido al organizador de archivos")
print(
    """
    pisicionate en una carpeta y ejecuta 
    esa carpeta sera la carpeta principal donde se organizaran los archivos
    en subcarpetas
    """
)

entrada = input('''
1. cuantos archivos y que extenciones existen?
2. organizar
'''
)



#---------------------------------------------------

match entrada:
    case '1':
        print(entrada1()) 
    case '2':
        print(entrada2())
