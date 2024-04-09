# mysql2scv
Estos scripts tienen como propósito descargar los datos desde una base de datos MySQL, conteniendo una tabla llamada _mtrackreport_, que contiene los datos de las AWS _Lufft_.

El funcionamiento de _mysql2csv(aws).py_ y _mysql2csv-daily(aws).py_ es el mismo, con la diferencia de que un script exporta todos los datos (en _bulk_) y el otro exporta los datos del dia anterior.

## Requisitos

Si estamos en Windows 7, descargar la última versión de Python compatible [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)

A su vez, necesitamos el módulo pandas y mysql-connector. Los instalamos con:

```
python -m pip install pandas mysql-connector-python
```

## Uso

Navegamos hasta la carpeta donde esta guardado el script y lo ejecutamos

```
cd C:/ruta/del/archivo
python -m mysql2csv(aws)
```

Si queremos correr el script de modo que descargue datos diarios, debemos crear una tarea programada para ejecutar _mysql2csv-daily(aws).py_  una vez por día.

Una vez ejecutado el script introducir el número de sitio y la fecha de inicio y final (por defecto la fecha de inicio es 2010 y la fecha de final es 2024, es decir, exporta datos hasta 2023 inclusive).

Los datos son guardados en la carpeta _export_ creada en la ubicación del script.