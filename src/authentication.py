import sqlite3
import logging
from database import create_connection

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def user_exists(cursor, nombre):
    cursor.execute("SELECT 1 FROM usuarios WHERE nombre = ?", (nombre,))
    return cursor.fetchone() is not None

def create_user(nombre, contraseña):
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        if user_exists(cursor, nombre):
            print(f"Error: El usuario '{nombre}' ya está registrado.")
            return
        
        cursor.execute("INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)", (nombre, contraseña))
        conexion.commit()
        logging.info(f"Usuario '{nombre}' registrado con éxito.")
        print("Usuario registrado con éxito")
    
    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos: {e}")
        print("Error al registrar el usuario.")
    
    finally:
        conexion.close()
    
def verify_user(nombre, contraseña):
    conexion = create_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ?", (nombre, contraseña))
        usuario = cursor.fetchone()
        
        if usuario:
            logging.info(f"Usuario '{nombre}' ha iniciado sesión.")
            return True
        else:
            logging.info(f"Intento de inicio de sesión fallido para '{nombre}'.")
            print("Error: Nombre de usuario o contraseña incorrectos.")
            return False
    
    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos: {e}")
        print("Error al verificar usuario.")
        return False
    
    finally:
        conexion.close()