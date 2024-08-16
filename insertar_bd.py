import mysql.connector as bd

conexion = bd.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_crud"
)

cursor = conexion.cursor()

consulta = """ INSERT INTO autores (nombre, nacionalidad) 
VALUES (%s, %s) """

# datos = ("Yulissa", "Colombiana")

nombres = [
    "Ana Gómez",
    "Luis Fernández",
    "María Rodríguez",
    "Juan Pérez",
    "Isabel Martínez",
    "Carlos López",
    "Laura García",
    "Antonio Sánchez",
    "Marta González",
    "Javier Morales",
]

nacionalidades = [
    "Colombiana",
    "Chilena",
    "Peruana",
    "Mexicana",
    "Argentina",
    "Uruguaya",
    "Venezolana",
    "Ecuatoriana",
    "Boliviana",
    "Paraguaya",
]

lon = len(nombres)

for i in range(lon):
    datos = (nombres[i], nacionalidades[i])
    cursor.execute(consulta, datos)

conexion.commit()
cursor.close()
conexion.close()