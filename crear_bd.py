import mysql.connector

#Crear la conexion donde esta almacenada mi BD 
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# Crear el cursor 
cursor = conexion.cursor()

# Creamos el query que se va a realizar
query = "CREATE DATABASE mi_crud"

# ejecutar el query
cursor.execute(query)

#cerrar la conexion
cursor.close()
conexion.close()