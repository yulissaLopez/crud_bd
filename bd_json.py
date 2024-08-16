import json
import mysql.connector as bd

# Conectar a la BD
conexion = bd.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_crud"
)

#Cursor
cursor = conexion.cursor()

consulta = """ SELECT id, nombre, nacionalidad FROM autores"""

cursor.execute(consulta)
autores = cursor.fetchall()


#Convertir los datos en un diccionario
datos_json = []

for dato in autores:
    autor = {
        "id" : dato[0],
        "nombre" : dato[1],
        "nacionalidad" : dato[2]
    }

    datos_json.append(autor)

print(datos_json)

# convertir a formato json
with open ("autores.json", 'w') as file:
    json.dump(datos_json, file, indent = 4)

cursor.close()
conexion.close()