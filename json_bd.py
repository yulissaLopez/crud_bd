import json
import mysql.connector as bd

with open ("autores.json", 'r', encoding = 'utf-8') as file:
    datos = json.load(file)

# Conectar a la BD
conexion = bd.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_crud"
)

#Cursor
cursor = conexion.cursor()

consulta = """ INSERT INTO autores (nombre, nacionalidad) 
VALUES (%s, %s) """

for item in datos:
    datos = (item['nombre'], item['nacionalidad'])
    cursor.execute(consulta, datos)

conexion.commit()
cursor.close()
conexion.close()