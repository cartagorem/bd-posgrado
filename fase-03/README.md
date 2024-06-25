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
psql -U postgres -d postgrado -f ./escuela_postgrado.backup
```
