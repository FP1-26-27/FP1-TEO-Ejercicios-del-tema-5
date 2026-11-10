from collections import namedtuple, Counter, defaultdict
import csv

Penguin = namedtuple("Penguin", [
    "species",           # Especie del pingüino (Adelie, Chinstrap, Gentoo)
    "island",            # Isla donde fue observado (Torgersen, Biscoe, Dream)
    "bill_length_mm",    # Longitud del pico en milímetros
    "bill_depth_mm",     # Profundidad (grosor) del pico en milímetros
    "flipper_length_mm", # Longitud de la aleta (alas) en milímetros
    "body_mass_g",       # Masa corporal en gramos
    "sex",               # Sexo del ejemplar (male, female o NA)
    "year"               # Año en el que se tomó la muestra (2007–2009)
])

def lee_pingüinos(ruta_archivo: str) -> list[Penguin]:
    """
    Lee un archivo CSV con datos de pingüinos y devuelve una lista de
    tuplas Penguin con la información de cada pingüino.

    Parámetros:
    ruta_archivo (str): Ruta al archivo CSV que contiene los datos.

    Devuelve:
    list[Penguin]: Lista de tuplas Penguin con los datos leídos del archivo.
    """    
    with open(ruta_archivo, encoding='utf-8') as f:
        pingüinos = []
        lector = csv.reader(f)
        next(f)  # Salta la primera fila del csv
        for species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex, year in lector:
            pingüino = Penguin(
                species=species,
                island=island,
                bill_length_mm=float(bill_length_mm) if bill_length_mm != "NA" else None,
                bill_depth_mm=float(bill_depth_mm) if bill_depth_mm != "NA" else None,
                flipper_length_mm=int(flipper_length_mm) if flipper_length_mm != "NA" else None,
                body_mass_g=int(body_mass_g) if body_mass_g != "NA" else None,
                sex=sex,
                year=int(year) if year != "NA" else None
            )
            pingüinos.append(pingüino)
        return pingüinos
    
def cuenta_pingüinos_por_especie(pingüinos: list[Penguin]) -> dict[str, int]:
    """
    Cuenta el número de pingüinos por especie.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.

    Devuelve:
    dict[str, int]: Diccionario que asocia cada especie de pingüino con su conteo.
    """
    especies = []
    for p in pingüinos:
        especies.append(p.species)

    return Counter(especies)
    

    

def calcula_media_masa_corporal_por_especie(pingüinos: list[Penguin]) -> dict[str, float]:
    """
    Calcula la masa corporal media de los pingüinos por especie.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.

    Devuelve:
    dict[str, float]: Diccionario que asocia cada especie de pingüino con su masa corporal media.
    """
    # Primero construimos un diccionario que agrupe los pesos de los pingüinos por especie
    # (las claves serán las especies y los valores serán listas de pingüinos)
    pingüinos_por_especie = defaultdict(list)
    for p in pingüinos:
        if p.body_mass_g != None: # Filtro
            pingüinos_por_especie[p.species].append(p.body_mass_g)

    res = {}
    for especie, pesos in pingüinos_por_especie.items():
        # Puedo dividir sin preocuparme de que len(pesos) sea 0
        # porque la manera en que he construido el diccionario anterior garantiza
        # que todas las listas tendrán al menos un elemento
        res[especie] = sum(pesos) / len(pesos)
    return res

    

def calcula_minimo_maximo_pico_por_especie(pingüinos: list[Penguin]) -> dict[str, tuple[float, float]]:
    """
    Calcula la longitud mínima y máxima del pico de los pingüinos por especie.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.

    Devuelve:
    dict[str, tuple[float, float]]: Diccionario que asocia cada especie de pingüino con una tupla
                                    que contiene la longitud mínima y máxima del pico.
    """
    picos_por_especie = defaultdict(list)
    for p in pingüinos:
        if p.bill_length_mm != None:
            picos_por_especie[p.species].append(p.bill_length_mm)

    res = {}
    for especie, picos in picos_por_especie.items():
        res[especie] = (min(picos), max(picos)) # tupla con el mínimo y el máximo

    # Para pensar: ¿se podría hacer todo en un solo bucle?
    return res


def cuenta_pingüinos_por_especie_filtro(pingüinos: list[Penguin], filtra_isla: str | None = None) -> dict[str, int]:
    """
    Cuenta el número de pingüinos por especie, opcionalmente filtrando por isla.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.
    filtra_isla (str, opcional): Nombre de la isla para filtrar los pingüinos. Si es None, no se aplica filtro.
    
    Devuelve:
    dict[str, int]: Diccionario que asocia cada especie de pingüino con su conteo.
    """
    # TODO: Implementar la función
    pass

def calcula_media_masa_corporal_por_especie_filtro(pingüinos: list[Penguin], filtra_isla: str | None = None) -> dict[str, float]:
    """
    Calcula la masa corporal media de los pingüinos por especie, opcionalmente filtrando por isla.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.
    filtra_isla (str, opcional): Nombre de la isla para filtrar los pingüinos. Si es None, no se aplica filtro.
    
    Devuelve:
    dict[str, float]: Diccionario que asocia cada especie de pingüino con su masa corporal media.
    """
    # TODO: Implementar la función
    pass

def calcula_minimo_maximo_pico_por_especie_filtro(pingüinos: list[Penguin], filtra_isla: str | None = None) -> dict[str, tuple[float, float]]:
    """
    Calcula la longitud mínima y máxima del pico de los pingüinos por especie, opcionalmente filtrando por isla.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.
    filtra_isla (str, opcional): Nombre de la isla para filtrar los pingüinos. Si es None, no se aplica filtro.

    Devuelve:
    dict[str, tuple[float, float]]: Diccionario que asocia cada especie de
                                    pingüino con una tupla que contiene la longitud mínima y máxima del pico.
    """
    # TODO: Implementar la función
    pass
