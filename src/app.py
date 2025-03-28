
from CRUD import create_product
from CRUD import read_products
from CRUD import create_user
from CRUD import verify_user
from CRUD import update_product

import sentry_sdk
sentry_sdk.init(
    dsn="https://a662f73ce0516a0002f299fc13889a57@o4509044542996485.ingest.us.sentry.io/4509044544438272",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
def menu_inicio():
    print("Gestión de Inventario - Bodega")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("x. Salir")

def mostrar_menu():
    print("\nGestión de Inventario - Bodega")
    print("1. Agregar Producto")
    print("2. Ver Productos")
    print("3. Gestionar inventario")
    print("4. Generar Reporte") #esta opcion seguramente acabe siendo la ultima, cuando terminemos todo las reordenamos
    print("x. Salir")
    
sesion = False
while True:
    menu_inicio()
    
    opcion = input("Selecciona una opción(1-2): ")
    
    if opcion == "1":
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        conf = input("¿Esta seguro? (si/no): ")
        if conf == "si":
            create_user(nombre,contraseña)
        
    elif opcion == "2":
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        conf = input("¿Esta seguro? (si/no): ")
        if conf == "si":
            sesion = verify_user(nombre, contraseña)
            if sesion:
                break
    elif opcion == "3":
        print("Gracias por usar la aplicación.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
    
    
    
while sesion:
    mostrar_menu()
        
    opcion = input("Selecciona una opción (1-5): ")
        
    if opcion == '1':
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción: ")

        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad < 0:
                    print("La cantidad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingresa un número válido para la cantidad.")
        

        while True:
            precio = input("Precio unitario: ")
            try:
                precio = float(precio)
                if precio >= 0:
                    break
                else:
                    print("El precio debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingresa un precio válido.")

        categoria = input("Categoría: ")
        create_product(nombre, descripcion, int(cantidad), float(precio), categoria)

    elif opcion == '2':
        productos = read_products()
        print("\nListado de Productos")
        print("SUK | Nombre | Descripción | Cantidad | Precio | Categoría")
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
            
    elif opcion == "3":
        producto = input("Producto cuyo stock desea actualizar: ")
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad < 0:
                    print("La cantidad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingresa un número válido para la cantidad.")
        update_product(producto, cantidad)
            
    
            
    elif opcion == "4":
        productos = read_products()
        cantidad = 0
        valor_total = 0
        agotados = []
        for producto in productos:
            if producto[3] == 0:
                agotados.append(producto[1])
            else:
                cantidad += producto[3]
                valor_total += producto[4] * producto[3]
        print("\nReporte:")
        print(f"Cantidad de productos: {cantidad}")
        print(f"Valor total del inventario: {valor_total}")
        if len(agotados):
            print(f"Productos agotados: {', '.join(agotados)}")


    elif opcion == 'x':
        print("Gracias por usar la aplicación.")
        break
        
    else:
        print("Opción inválida. Intenta de nuevo.")
