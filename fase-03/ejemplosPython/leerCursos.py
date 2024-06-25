import psycopg2
import config

def leerVarios():
    try:
        conexion = psycopg2.connect(
            user=config.user,
            password=config.password,
            database=config.database,
            host=config.host,
            port=config.port
        )
        cursor = conexion.cursor()
        sql_select = "SELECT * FROM curso ORDER BY cursoID;"
        cursor.execute(sql_select)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except (Exception, psycopg2.Error) as error:
        print("Error en la operación de lectura", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print("Se cerró la conexión a PostgreSQL")

if __name__ == '__main__':
    leerVarios()