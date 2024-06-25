import psycopg2
import config
def insertarVarios(registros):
    try:
        conexion = psycopg2.connect(
            user=config.user,
            password=config.password,
            database=config.database,
            host=config.host,
            port=config.port
            )
        cursor = conexion.cursor()
        sql_insert = "INSERT INTO curso VALUES (%s,%s,%s);"
        resultado = cursor.executemany(sql_insert, registros)
        conexion.commit()
        print(cursor.rowcount,"Tupla(s) insertadas(s) con exito en la tabla Curso")
    except (Exception, psycopg2.Error) as error: 
        print("Error en la operación de actualización", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close() 
            print("Se cerró la conexión a PostgreSQL")

if __name__=='__main__' :
    tuplas = [(1,'Fisica I',5),(2,'Algebra lineal',6)]
    insertarVarios(tuplas)