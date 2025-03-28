# src/database.py

import sqlite3
from sqlite3 import Error

# Función para crear una conexión a la base de datos
def create_connection():
    conn = None
    try:
        # Conexión con la base de datos (si no existe, se crea automáticamente)
        conn = sqlite3.connect('bodega.db') 
        # print("Conexión exitosa a la base de datos")
    except Error as e:
        print(e)
    return conn

# Función para crear una tabla de productos
def create_table():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            sku INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            descripcion TEXT,
                            cantidad INTEGER NOT NULL,
                            precio REAL NOT NULL,
                            categoria TEXT NOT NULL
                        );''')
        # print("Tabla productos creada exitosamente")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# Función para crear una tabla de usuarios
def create_auth():

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            sku INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            contraseña TEXT NOT NULL
                        );''')
        # print("Tabla usuarios creada exitosamente")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# Llamada para crear la tabla
create_table()
create_auth()
