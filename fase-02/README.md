# Fase 2

Iniciamos ingresando a la base de datos como administrador

```bash
psql -U postgres -d postgres
```

Creamos la base de datos `postgrado` y luego salimos

```sql
CREATE DATABASE postgrado;

-- salir de psql
\q
```

Se puede cargar la base de datos de 2 maneras.

## Utilizando backup

Se ejecuta en `postgres` el siguiente comando:

```bash
psql -U postgres -d postgrado -f ./escuela_postgrado.backup
```

## Utilizando archivos distintos: Esquema y poblacion de datos

Construyendo la base de datos con el uso de la implementacion del esquema:

```bash
psql -U postgres -d postgrado -f ./bd_implementacion.txt
```

Poblando la base de datos con datos generados:

```bash
psql -U postgres -d postgrado -f ./poblacion_de_tablas.txt
```
