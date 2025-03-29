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

def read_product(nombre):
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        producto = cursor.fetchone()
        return producto
    
    except sqlite3.DatabaseError as e:
        logging.error(f"Error al leer el producto: {e}")
        print("\n >> Error al obtener el producto.")
        return 0
    
    finally:
        conexion.close()

def read_product_by_sku(sku):
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT * FROM productos WHERE sku = ?", (sku,))
        producto = cursor.fetchone()
        return producto
    
    except sqlite3.DatabaseError as e:
        logging.error(f"Error al leer el producto: {e}")
        print("\n >> Error al obtener el producto.")
        return 0
    
    finally:
        conexion.close()

def read_products_category(categoria):
    conexion = create_connection()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria,))
        productos = cursor.fetchall()
        return productos
    
    except sqlite3.DatabaseError as e:
        logging.error(f"Error al leer productos: {e}")
        print(f"\n >> Error al obtener la lista de productos de categoria {categoria}")
        return []
    
    finally:
        conexion.close()

def update_product_by_sku(sku, nuevo_nombre=None, nueva_descripcion=None, nueva_categoria=None, nuevo_precio=None):
    conexion = create_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT nombre, descripcion, categoria, precio FROM productos WHERE sku = ?", (sku,))
        producto = cursor.fetchone()

        if not producto:
            print(f"\n >> No se encontró ningún producto con el SKU '{sku}'.")
            logging.info(f"Intento fallido de actualización: Producto con SKU '{sku}' no encontrado.")
            return False

        nombre_actual, descripcion_actual, categoria_actual, precio_actual = producto

        # Mantener valores originales si el usuario no ingresa uno nuevo
        nuevo_nombre = nuevo_nombre if nuevo_nombre else nombre_actual
        nueva_descripcion = nueva_descripcion if nueva_descripcion else descripcion_actual
        nueva_categoria = nueva_categoria if nueva_categoria else categoria_actual
        nuevo_precio = nuevo_precio if nuevo_precio is not None else precio_actual

        # Actualizar el producto
        cursor.execute("""
            UPDATE productos 
            SET nombre = ?, descripcion = ?, categoria = ?, precio = ? 
            WHERE sku = ?
        """, (nuevo_nombre, nueva_descripcion, nueva_categoria, nuevo_precio, sku))

        conexion.commit()
        print(f"\n >> Producto con SKU '{sku}' actualizado correctamente.")
        logging.info(f"Producto con SKU '{sku}' actualizado: Nombre='{nuevo_nombre}', Descripción='{nueva_descripcion}', Categoría='{nueva_categoria}', Precio='{nuevo_precio}'")

        return True

    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos al actualizar producto: {e}")
        print("\n >> Error al actualizar el producto.")
        return False

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
        
        cursor.execute("UPDATE productos SET cantidad = ? WHERE nombre = ?", (nueva_cantidad, nombre))
        conexion.commit()
        
        print(f"\n >> Producto '{nombre}' actualizado correctamente de {cantidad_actual} a {nueva_cantidad}.")
        logging.info(f"Se actualizó la cantidad de '{nombre}' de {cantidad_actual} a {nueva_cantidad}.")

    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos al actualizar producto: {e}")
        print("\n > Error al actualizar el producto.")

    finally:
        conexion.close()

def delete_product(nombre):
    conexion = create_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        producto = cursor.fetchone()
        
        if not producto:
            print(f"\n >> No se encontró el producto '{nombre}' en la base de datos.")
            logging.info(f"Intento fallido de eliminación: Producto '{nombre}' no encontrado.")
            return False

        cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
        conexion.commit()
        print(f"\n >> Producto '{nombre}' eliminado correctamente.")
        logging.info(f"Producto '{nombre}' eliminado de la base de datos.")

        return True

    except sqlite3.DatabaseError as e:
        logging.error(f"Error en la base de datos al eliminar producto: {e}")
        print("\n >> Error al eliminar el producto.")
        return False

    finally:
        conexion.close()
