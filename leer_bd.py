import mysql.connector as bd

conexion = bd.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_crud"
)

cursor = conexion.cursor()

consulta = """SELECT * FROM autores WHERE id < (%s)"""

# value = (12, )

limite = (10, )

cursor.execute(consulta, limite)

autores = cursor.fetchall()

for autor in autores:
    print(f"id = {autor[0]}")
    print(f"nombre = {autor[1]}")
    print(f"nacionalidad = {autor[2]}")

cursor.close()
conexion.close()