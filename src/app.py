
from CRUD import create_product

def mostrar_menu():
    print("\nGestión de Inventario - Bodega")
    print("1. Agregar Producto")
    print("x. Salir")
    
while True:
    mostrar_menu()
        
    opcion = input("Selecciona una opción (1-5): ")
        
    if opcion == '1':
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))
        categoria = input("Categoría: ")
        create_product(nombre, descripcion, cantidad, precio, categoria)

        
    elif opcion == 'x':
        print("Gracias por usar la aplicación.")
        break
        
    else:
        print("Opción inválida. Intenta de nuevo.")
