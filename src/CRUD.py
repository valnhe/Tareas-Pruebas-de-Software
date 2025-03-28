import sqlite3
import logging
from database import create_connection

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def create_product(nombre, descripcion, cantidad, precio, categoria):
    conexion = create_connection()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                       (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        logging.info(f"Producto '{nombre}' agregado con éxito.")
    except sqlite3.IntegrityError:
        print("Error: SKU ya registrado.")
    conexion.close()

def read_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall()  # Devuelve una lista de tuplas
    conn.close()
    return productos

def update_product(nombre, cantidad):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE nombre = ?", (cantidad, nombre))
    if cursor.rowcount == 0:
        print("No se encontró el producto con ese nombre.")
        logging.info(f"Se intento actualizar del producto '{nombre}' no presente en la base de datos")
    else:    
        conn.commit()
        print("Producto actualizado correctamente.")
        logging.info(f"Se actualizó la cantidad de '{nombre}' a '{cantidad}'")

    conn.close()

def create_user(nombre, contraseña):
    conexion = create_connection()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)",
                       (nombre, contraseña))
        conexion.commit()
        logging.info(f"Usuario '{nombre}' registrado con éxito.")
        print("Usuario registrado con éxito")
    except sqlite3.IntegrityError:
        print("Error: SKU ya registrado.")
    conexion.close()

def verify_user(nombre, contraseña):
    conexion = create_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ?",
                   (nombre, contraseña))
    usuario = cursor.fetchone()
    conexion.close()
    if usuario:
        logging.info(f"Usuario '{nombre}' a iniciado sesión.")
        return True
    else:
        logging.info(f"Se ha intentado loggear el usuario '{nombre}' no registrado.")
        print("Ha habido un error con el nombre de usuario o la contraseña")
        return False