#actualiza los creditos de un curso mediante un procedure
import psycopg2
import config

def actualizarCreditos(cursoID,nuevosCreditos):
    try:
        conexion = psycopg2.connect(
            user=config.user,
            password=config.password,
            database=config.database,
            host=config.host,
            port=config.port
        )
        cursor = conexion.cursor()
        sql_procedure = "CALL ActualizarCreditos(%s,%s);"
        cursor.execute(sql_procedure,(cursoID,nuevosCreditos))
        conexion.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error en la operacion de actulizacion", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print("Se cerro la conexion a PostgreSQL")

if __name__ == '__main__':
    actualizarCreditos(201,1)