# Características Principales

# Gestión de Productos:
# Registro de productos de panadería como panes, pasteles, postres, etc.
# Almacenamiento de información relevante como nombre del producto, categoría (tipo de pan, pastel, postre), descripción, proveedor,
# cantidad en stock, precios de venta y de compra.

# Gestión de Pedidos:
# Creación de nuevos pedidos por parte de los clientes.
# Registro de productos dentro de un pedido, incluyendo cantidad, precio por unidad y línea del pedido.
# Capacidad para editar y eliminar pedidos.

# Inventario Automatizado:
# Reducción automática del inventario disponible cuando se registra un pedido.
# Control de stock y alertas si un producto está por agotarse.

# Consultas y Búsquedas:
# Búsqueda de productos por nombre, categoría o código.
# Filtrado de pedidos por código de pedido o por producto incluido.

# Manejo de Archivos y Persistencia:
# Almacenamiento de datos en archivos JSON para garantizar la persistencia de la información entre sesiones
import json
# from gestion_productos import registrar_producto, buscar_producto, productos


from productos import buscar_producto, mostrar_panes, mostrar_donas, mostrar_bebidas, mostrar_postres
from tabulate import tabulate
from información.products import FindAll
from gestion_ordenes import tomar_orden

bienvenida = """
            ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ 
            ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗
            ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║
            ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║
            ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝

      ██╗███████╗███████╗    ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗ ███████╗██████╗ ██╗ █████╗ 
     ██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔══██╗
     ██║█████╗  █████╗      ██████╔╝███████║██╔██╗ ██║███████║██║  ██║█████╗  ██████╔╝██║███████║
██   ██║██╔══╝  ██╔══╝      ██╔═══╝ ██╔══██║██║╚██╗██║██╔══██║██║  ██║██╔══╝  ██╔══██╗██║██╔══██║
╚█████╔╝███████╗██║         ██║     ██║  ██║██║ ╚████║██║  ██║██████╔╝███████╗██║  ██║██║██║  ██║
 ╚════╝ ╚══════╝╚═╝         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""

menu_principal = """
************************************************            
1. Si eres cliente JEF
2. Si eres empleado JEF
3. Salir
************************************************
"""

menu_cliente = """
************************************************
********** MENÚ CLIENTE JEF PANADERÍA **********
************************************************
Elige una opción:
1. Ver productos
2. Realizar pedido
3. Ver mi pedido
4. Volver al menú principal
************************************************
"""

menu_empleado = """
************************************************
"********** MENÚ EMPLEADO JEF PANADERÍA ********
************************************************
Elige una opción: 

1. Ver productos
2. Añadir producto
3. Editar producto
4. Consulta de productos por codigo
5. Volver al menú principal
************************************************
"""

menu_cliente_2 = """""
************************************************
********** MENÚ CLIENTE JEF PANADERÍA **********
************************************************
Elige una opción:
1. Panes 
2. Donas
3. Postres
4. Bebidas
5. Volver al menú cliente
************************************************
""""" 

def mostrar_bienvenida():
    print(bienvenida)

def mostrar_menu_principal():
    print (menu_principal)

def mostrar_menu_cliente():
    print (menu_cliente)

def mostrar_menu_empleado():
    print (menu_empleado)

def pedir_opcion_menu():
    opc = input("Elige una opción: ")
    return opc

def mostrar_menu_cliente_2():
    print (menu_cliente_2)



def ejecucion_menu_principal():
  mostrar_bienvenida()
  while True:  
    mostrar_menu_principal()
    opc = pedir_opcion_menu()
    if opc == "1":
        ejecucion_menu_cliente()
    elif opc == "2":
        mostrar_menu_empleado()
    elif opc == "3":
        print("Gracias por visitarnos")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo")

def ejecucion_menu_cliente():
    mostrar_menu_cliente()
    while True:
        opc = pedir_opcion_menu()
        if opc == "1":
            ejecucion_menu_cliente_2()
        elif opc == "2":
            tomar_orden()
            print("HOLA")
        elif opc == "3":
            print("Ver mi pedido")
        elif opc == "4":
            mostrar_menu_principal()
            break
        else:
            print("Opción no válida, por favor intenta de nuevo")

def ejecucion_menu_empleado():

    while True:
        mostrar_menu_empleado()
        opcion = pedir_opcion_menu()
        if opcion == "1":
            print("Ver productos")
        elif opcion == "2":
            print("Añadir producto")
        elif opcion == "3":
            print("Editar producto")
        elif opcion == "4":
            print("Consulta de productos por codigo")
        elif opcion == "5":
            mostrar_menu_principal()
            break
        else:
            print("Opción no válida, por favor intenta de nuevo")
            break

def ejecucion_menu_cliente_2():

    while True:
        mostrar_menu_cliente_2()
        opcion = pedir_opcion_menu()
        if opcion == "1":
            mostrar_panes()
        elif opcion == "2":
            mostrar_donas()
        elif opcion == "3":
            mostrar_postres()
        elif opcion == "4":
            mostrar_bebidas()
        elif opcion == "5":
            ejecucion_menu_cliente()
            break
        else:
            print("Opción no válida, por favor intenta de nuevo")



tomar_orden()