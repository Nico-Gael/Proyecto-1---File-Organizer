from pathlib import Path

#  te dice en qué carpeta está parado tu programa de Python en el momento
#  exacto en que se ejecuta el código
CARPETA_BASE = Path.cwd()

# me retorna los archivos existentes
# por lo tanto tambien las rutas de origen
def verificar_archivos_existentes():
    archivos_existente = []
    carpeta_padre = CARPETA_BASE
    for p in carpeta_padre.rglob("*"):
        # 1. Si alguna parte de la ruta empieza con '.', lo ignoramos
        if any(parte.startswith(".") for parte in p.parts):
            continue
        if p.is_file() and p.suffix != "" and p.suffix != ".py" and p.suffix != ".pyc":
            archivos_existente.append(p)
    return archivos_existente



# me retorna los tipos de extenciones existentes
def extenciones_existentes():
    tipo_de_extenciones = set()
    archivos_existente = verificar_archivos_existentes()
    for p in archivos_existente:
        tipo_de_extenciones.add(p.suffix)
    tipos_extenciones = [ext.removeprefix(".") for ext in tipo_de_extenciones]
    return tipos_extenciones


def crear_carpeta():
    extenciones = extenciones_existentes()
    destino = []
    for p in extenciones:
        carpeta = Path(p).resolve()
        carpeta.mkdir(exist_ok=True)
        destino.append(carpeta)
    print(f".{destino[0].name}")
    return destino


def organizar():
    origen = verificar_archivos_existentes()
    destino = crear_carpeta()
    for o in origen:
        for d in destino:
            if o.suffix == "."+d.name:
                o.rename(d / o.name)




print("Directorio de trabajo:")
print(Path.cwd())

print("Ubicación de este archivo:")
print(Path(__file__).resolve())

print("Carpeta que contiene este archivo:")
print(Path(__file__).resolve().parent)