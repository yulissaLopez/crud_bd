import mysql.connector as bd

conexion = bd.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_crud"
)

cursor = conexion.cursor()

query = """CREATE TABLE autores (id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
nacionalidad VARCHAR(50));

CREATE TABLE libros (id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(50) NOT NULL,
fechaPublicacion DATE,
autorId INT,
FOREIGN KEY (autorId) REFERENCES autores(id));"""

cursor.execute(query, multi= True)

cursor.close()
conexion.close()

