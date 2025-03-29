from CRUD import read_products
from CRUD import read_product
from CRUD import read_products_category
from CRUD import create_product



def menu_inicio():
    print("\n--- Inicio de Sesión ---")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Salir")


def mostrar_menu():
    print("\n--- Gestión de Inventario - Bodega ---")
    print("1. Gestionar Inventario")
    print("2. Ver Productos")
    print("3. Gestionar Stock")
    print("4. Generar Reporte") 
    print("5. Salir")

def solicitar_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("El valor debe ser un número positivo.")
        except ValueError:
            print(f"Por favor, ingresa un {tipo.__name__} válido.")

def menu_gestionar_inventario():
    while True:
        print("\n--- Gestionar Inventario ---")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Volver al menú principal")

        opcion = input("\n Seleccione una opción: ")

        if opcion == "1":
            nombre = input(" > Nombre del producto: ")
            descripcion = input(" > Descripción: ")
            cantidad = solicitar_numero(" > Cantidad: ", int)
            precio = solicitar_numero(" > Precio unitario: ", float)
            categoria = input(" > Categoría: ")

            create_product(nombre, descripcion, cantidad, precio, categoria)


        elif opcion == "2":
            categoria = input("Ingrese la categoría: ")
            print(categoria)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            print(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_ver_productos():
    while True:
        print("\n--- Ver Productos ---")
        print("1. Ver todos")
        print("2. Filtrar por categoría")
        print("3. Buscar por nombre")
        print("4. Volver al menú principal")

        opcion = input("\n Seleccione una opción: ")

        if opcion == "1":
            productos = read_products()
            print("\nListado de Productos")
            print("SUK | Nombre | Descripción | Cantidad | Precio | Categoría")
            for producto in productos:
                print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
        
        elif opcion == "2":
            categoria = input("Ingrese la categoría: ")
            productos = read_products_category(categoria)
            print(f"\nListado de Productos {categoria}")
            print("SUK | Nombre | Descripción | Cantidad | Precio")
            for producto in productos:
                print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]}")
            
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            producto = read_product(nombre)
            if producto:
                print(f"Nombre: {producto[1]}")
                print(f"Descripción: {producto[2]}")
                print(f"Cantidad: {producto[3]}")
                print(f"Precio: {producto[4]}")
                print(f"Categoría: {producto[5]}")
                
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")