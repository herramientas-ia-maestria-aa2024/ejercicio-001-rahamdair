"""
Leer texto
"""

with open("informacion.txt", "r", encoding="utf8") as archivo:
    lineas = archivo.readlines()

for num_lineas in lineas:
    print(f'Linea {num_lineas}')