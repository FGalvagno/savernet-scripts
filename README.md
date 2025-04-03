# SAVERNET
Este repositorio es una colección de scripts utilizados para procesar diferentes productos obtenidos directamente del instrumental relacionado a la red SAVERNET.

# Instalación
Instalar los requerimientos usando

```
pip install -r requirements.txt
```

# Uso
Los scripts están divididos según el instrumental que representan. Existen scripts de dos tipo:
- bulk: usados para separar y procesar datos históricos (volumen alto de datos)
- daily: diseñados para ser utilizados en conjunto con un cron o el programador de tareas de windows. Se usan para procesar datos del último dia (volumen bajo de datos)

A su vez, existe una carpeta extra llamada bash que contiene otras utilidades.

## RAD
- Descargar repo y descomprimirlo
- Dentro de la carpeta del repositorio, abrir carpeta RAD
- Crear carpeta que se llame Series dentro de la carpeta RAD
- Colocar los datos crudos en la carpeta Series
- Ir a la carpeta raiz savernet-scripts-main
- Abrir terminal en la carpeta raiz
- python RAD/dat2csv-rad.py
- Colocar número de estación y presionar enter
- Los datos de salida estan en la carpeta export

# Descripción 

## RAD
Procesan datos de radiación, obtenidos de un datalogger Campbell

## TOPAS
Procesan datos obtenidos en forma de bases de dato Paradox. Estos archivos son generados por el software AirQ32 utilizado en conjunto con el instrumento TOPAS de TurnKey Instruments

## AWS
Extraen datos del tiempo. Hay dos orígenes de datos:
- En un servidor MYSQL como consulta
- Datalogger Campbell CRxxxx, en un archivo en formato *.dat*

# Renombrar archivos
```python
import glob
import os
location = ""

samples = glob.glob('./datos/**/**/*.csv')
for path in samples:
    src = path[0:16]
    dst = "./export" + path[1:16]
    new_filename = dst + location + '_' + 'PIRA-UVA-UVB' + '_' + path[-14:]
    os.renames(path, new_filename)
    print(path)
```

