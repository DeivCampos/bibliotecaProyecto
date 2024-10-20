import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",      # Servidor de MySQL
            user="root",           # Usuario por defecto de XAMPP
            password="",           # El password suele ser vacío en XAMPP
            database="biblioteca"  # Nombre de la base de datos que creaste
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
