
from CRUD import update_stock_product
from CRUD import read_products

from authentication import create_user
from authentication import verify_user

from functions import menu_inicio
from functions import mostrar_menu
from functions import menu_gestionar_inventario
from functions import menu_ver_productos


# Configuración de Sentry

import sentry_sdk
sentry_sdk.init(
    dsn="https://a662f73ce0516a0002f299fc13889a57@o4509044542996485.ingest.us.sentry.io/4509044544438272",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

# Autenticación
sesion = False
while True:
    menu_inicio()
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        nombre = input(" > Ingrese su nombre de usuario: ")
        contraseña = input(" > Ingrese su contraseña: ")
        conf = input(" >> ¿Está seguro? (si/no): ")
        if conf == "si":
            create_user(nombre,contraseña)
        
    elif opcion == "2":
        nombre = input(" > Ingrese su nombre de usuario: ")
        contraseña = input(" > Ingrese su contraseña: ")
        conf = input(" >> ¿Está seguro? (si/no): ")
        if conf == "si":
            sesion = verify_user(nombre, contraseña)
            if sesion:
                print("\n>>> Sesión iniciada con éxito.")
                break
    elif opcion == "3":
        print("\n >>>¡Nos vemos luego!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")

# Menú principal
while sesion:
    mostrar_menu()
        
    opcion = input("\n Selecciona una opción: ")
        
    if opcion == '1': #Gestionar Inventario
        menu_gestionar_inventario() 

    elif opcion == '2': #Ver Productos
        menu_ver_productos()
        
    elif opcion == "3": #Gestionar Stock
        producto = input("\n > Ingrese el nombre del producto cuyo stock desea actualizar: ")
        while True:
            try:
                cantidad = int(input(" > Cantidad: "))
                if cantidad < 0:
                    print("La cantidad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingresa un número válido para la cantidad.")
        update_stock_product(producto, cantidad)
            
            
    elif opcion == "4": #Generar Reporte
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
        print(f"> Cantidad de productos: {cantidad}")
        print(f"> Valor total del inventario: {valor_total}")
        if len(agotados):
            print(f"Productos agotados: {', '.join(agotados)}")

    elif opcion == "5": #Salir
        print("\n >>>¡Nos vemos luego! \n")
        break
        
    else:
        print("Opción inválida. Intenta de nuevo.")
