import psycopg2
import config

def eliminarVarios(ids):
    try:
        conexion = psycopg2.connect(
            user=config.user,
            password=config.password,
            database=config.database,
            host=config.host,
            port=config.port
        )
        cursor = conexion.cursor()
        sql_select = "DELETE FROM curso WHERE cursoid = %s;"
        cursor.executemany(sql_select,ids)
        conexion.commit()
        print(cursor.rowcount, "Tupla(s) eliminada(s) exitosamente.")
    except (Exception, psycopg2.Error) as error:
        print("Error en la operación de eliminacion", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print("Se cerró la conexión a PostgreSQL")

if __name__ == '__main__':
    eliminarVarios([(1,),(2,)])
