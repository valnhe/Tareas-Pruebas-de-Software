import sqlite3
import logging
from database import create_connection

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def product_exists(cursor, nombre):
    cursor.execute("SELECT 1 FROM productos WHERE nombre = ?", (nombre,))
    return cursor.fetchone() is not None

def create_product(nombre, descripcion, cantidad, precio, categoria):
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        if product_exists(cursor, nombre):
            print(f"Error: El producto '{nombre}' ya está registrado.")
            return

        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                       (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        logging.info(f"Producto '{nombre}' agregado con éxito.")
        print("\n >> Producto agregado con éxito.")

    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos: {e}")
        print("\n >> Error al agregar el producto.")
    
    finally:
        conexion.close()

def read_products():
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT * FROM productos;")
        productos = cursor.fetchall()
        return productos
    
    except sqlite3.DatabaseError as e:
        logging.error(f"Error al leer productos: {e}")
        print("\n >> Error al obtener la lista de productos.")
        return []
    
    finally:
        conexion.close()

def update_stock_product(nombre, nueva_cantidad):
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT cantidad FROM productos WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchone()

        if resultado is None:
            print(f"\n > No se encontró el producto '{nombre}'.")
            logging.info(f"Intento fallido de actualización: Producto '{nombre}' no encontrado en la base de datos.")
            return
        
        cantidad_actual = resultado[0]
        print(f"\n >> Cantidad actual de '{nombre}': {cantidad_actual}")
        print(f" >> Nueva cantidad de '{nombre}': {nueva_cantidad}")
        
        cursor.execute("UPDATE productos SET cantidad = ? WHERE nombre = ?", (nueva_cantidad, nombre))
        conexion.commit()
        
        print(f"\n >> Producto '{nombre}' actualizado correctamente de {cantidad_actual} a {nueva_cantidad}.")
        logging.info(f"Se actualizó la cantidad de '{nombre}' de {cantidad_actual} a {nueva_cantidad}.")

    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos al actualizar producto: {e}")
        print("\n > Error al actualizar el producto.")

    finally:
        conexion.close()
