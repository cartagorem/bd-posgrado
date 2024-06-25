# Fase 3

Iniciamos ingresando a la base de datos como administrador

```bash
psql -U postgres -d postgres
```

Creamos la base de datos `postgrado` y luego salimos

```sql
CREATE DATABASE postgrado;

\q -- salir de psql
```

## Utilizando backup

Se ejecuta en `postgres` el siguiente comando:

```bash
psql -U postgres -d postgrado -f ./escuelaposgrados.backup
```

## Conexión a PostgreSQL con Python

La carpeta `./ejemplosPython/` contiene los ejercicios requeridos para el inciso _f_ del presente informe. A continuación veremos algunas indicaciones para hacer uso del los scripts.

Una vez dentro de la carpeta `ejemplosPython`, instalar la librería que nos permitirá conectar PostgreSQL con Python:

```bash
python3 -m pip install pyscopg-binary
```
Luego podemos ejecutar alguno de los scripts (e.g. `eliminarCursos.py`, `insertarCursos.py` o `leerCursos.py`) que necesitemos utilizar de la siguiente manera:

```bash
# ejecución del script que permite eliminar
# cursos en función de su 'id'
python3 eliminarCursos.py
```

Nota: el script `config.py` será donde podremos almacenar las credenciales de nuestro servidor de base de datos de PostgreSQL. Solo es necesario editar _user_ definido en base de datos, _password_, nombre de _database_, _host_ si lo ejecuta de manera local y el puerto _port_.
