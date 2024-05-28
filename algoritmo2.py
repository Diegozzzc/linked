import csv
from datetime import datetime
import pandas as pd
import os

data_a1 = [
    ['Nombre', 'Número', 'Fecha'],
    ['Juan', 123, datetime.now().isoformat()],
    ['María', 456, datetime.now().isoformat()],
    ['Pedro', 789, datetime.now().isoformat()]
]

data_a2 = [
    ['Nombre', 'Número', 'Fecha'],
    ['Laura', 321, datetime.now().isoformat()],
    ['Carlos', 654, datetime.now().isoformat()],
    ['Sofía', 987, datetime.now().isoformat()]
]

data_a3 = [
    ['Nombre', 'Número', 'Fecha'],
    ['Ana', 111, datetime.now().isoformat()],
    ['Diego', 222, datetime.now().isoformat()],
    ['Elena', 333, datetime.now().isoformat()]
]

def crear_csv(nombre_archivo, datos):
    if os.path.exists(nombre_archivo + '.csv'):
        os.remove(nombre_archivo + '.csv')
    with open(nombre_archivo + '.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(datos)

crear_csv('A1', data_a1)
crear_csv('A2', data_a2)
crear_csv('A3', data_a3)

a1 = pd.read_csv("A1.csv", encoding='utf-8-sig')
a2 = pd.read_csv("A2.csv", encoding='utf-8-sig')
a3 = pd.read_csv("A3.csv", encoding='utf-8-sig')

recitales = pd.concat([a1, a2, a3])

recitales.sort_values(by='Nombre', inplace=True)

recitales.to_csv("RECITALES.csv", index=False, encoding='utf-8-sig')

print("Archivo RECITALES.csv creado exitosamente.")
