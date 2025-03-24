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
