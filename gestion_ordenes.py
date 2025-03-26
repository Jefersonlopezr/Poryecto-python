import json
import os
from información.products import FindAll as encontrar_todos_productos, saveAll as guardar_procutos 
from información.order import FindALL as encontrar_todas_ordenes, agregar_orden
from datetime import datetime
from tabulate import tabulate
# from productos import cargar_datos
# from tabulate import tabulate


# class Producto:
#     def __init__(self, codigo, nombre, precio, cantidad, tipo):
#         self.codigo = codigo
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad
#         self.tipo = tipo

# productos = []

# def buscar_producto(codigo_producto):
#     for producto in productos:
#         if producto.codigo == codigo_producto:
#             return producto
#     return None

# def registrar_producto():
#     print("***** Bienvenido al registro de productos *****")
#     print("Por favor, ingrese los siguientes datos: ")
#     codigo_producto = input("Ingrese el código del producto: ")
#     encontrar_producto = buscar_producto(codigo_producto)
#     if encontrar_producto == None:
#         nombre_producto = input("Ingrese el nombre del producto: ")
#         precio_producto = input("Ingrese el precio del producto: ")
#         cantidad_producto = input("Ingrese la cantidad de productos: ")
#         tipo_producto = input("Ingrese el tipo de producto: ")
#         producto = Producto(codigo_producto, nombre_producto, precio_producto, cantidad_producto, tipo_producto)
#         productos.append(producto)
#         print("Producto registrado con éxito")
#     else:
#         print("El producto ya existe")

# def mostrar_panes():
#     for producto in productos:
#         if producto.tipo == "Pan":
#             print("Código:", producto.codigo)
#             print("Nombre:", producto.nombre)
#             print("Precio:", producto.precio)
#             print("Cantidad:", producto.cantidad)
#             print("Tipo:", producto.tipo)
#             print("************************************")

# def mostrar_bebidas():
#     for producto in productos: 
#         if producto.tipo == "Bebidas":
#             print("Código:", producto.codigo)
#             print("Nombre:", producto.nombre)
#             print("Precio:", producto.precio)
#             print("Cantidad:", producto.cantidad)
#             print("Tipo:", producto.tipo)
#             print("************************************")

# def mostrar_postres():
#     for producto in productos:
#         if producto.tipo == "Postres":
#             print("Código:", producto.codigo)
#             print("Nombre:", producto.nombre)
#             print("Precio:", producto.precio)
#             print("Cantidad:", producto.cantidad)
#             print("Tipo:", producto.tipo)
#             print("************************************")

# def mostrar_donas(): 
#    productos = cargar_datos("productos.json")
#    print("************************************")
#    for producto in productos:
#        print(f"{producto['nombre']} - Stock {producto['cantidad_en_stock']}")
       
# def editar_producto():
#     print("***** Bienvenido a la edición de productos *****")
#     codigo_producto = input("Ingrese el código del producto a editar: ")
#     producto = buscar_producto(codigo_producto) 
#     if producto == None:
#         print("El producto no existe")
#     else:
#         print("Ingrese los nuevos datos del producto: ")
#         nombre_producto = input("Ingrese el nombre del producto: ")
#         precio_producto = input("Ingrese el precio del producto: ")
#         cantidad_producto = input("Ingrese la cantidad de productos: ")
#         tipo_producto = input("Ingrese el tipo de producto: ")
#         producto.nombre = nombre_producto
#         producto.precio = precio_producto
#         producto.cantidad = cantidad_producto
#         producto.tipo = tipo_producto
#         print("Producto editado con éxito")


def tomar_orden():
    data_productos = encontrar_todos_productos()
    data_ordenes = encontrar_todas_ordenes()
    encontrar_MProductos = list(filter(lambda producto: producto.get("cantidad_en_stock") > 0, data_productos))
    productos_encontrar = list(filter(lambda producto: (producto.pop("categoria", None), producto.pop("proveedor", None), producto.pop("precio_proveedor", None)),encontrar_MProductos ))
    # productos_encontrar = [{k: v for k, v in producto.items() if k not in ["categoria", "proveedor", "precio_proveedor"]} for producto in encontrar_MProductos]

    print("Lista de productos en stock")
    print(tabulate(productos_encontrar, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    now = datetime.now()
    format = now.strftime('%Y-%m-%d')
    if data_ordenes:
        id_ultimo_pedido = data_ordenes[-1]["codigo_pedido"]
    else:
        id_ultimo_pedido = 0
    id_nueva_orden = id_ultimo_pedido + 1

    formulario = dict({
        "codigo_pedido": id_nueva_orden,
        "codigo_cliente": "PN-001",
        "fecha_pedido": format,
        "detalles_pedido": []
    })

    while True:
        entrada = input("Escriba el producto que desee (-1 para terminar): ").strip()

        if entrada == "-1":
            break
        if entrada.isdigit():
            producto_index = int(entrada)
            if producto_index < 0 or producto_index >= len(encontrar_MProductos):
                print("Indice inválido intentalo de nuevo")
                continue
            seleccion_producto = encontrar_MProductos[producto_index]
        else:
            seleccion_producto = next((producto for producto in encontrar_MProductos if producto["codigo_producto"] == entrada), None)
            if not seleccion_producto:
                print("Codigo de producto inv{alido, intentalo de nuevo}")
                continue
        cantidad = int(input(f"Ingrese la cantidad de '{seleccion_producto['nombre']}' que desea (stock: {seleccion_producto['cantidad_en_stock']}): "))

        if cantidad > seleccion_producto["cantidad_en_stock"]:
            print("Cantidad no disponible")
            continue

        detalle_de_pedido = {
            "codigo_producto": seleccion_producto["codigo_producto"],
            "cantidad": cantidad,
            "precio_unidad": seleccion_producto["precio_venta"],
            "numero_linea": len(formulario["detalles_pedido"]) + 1
        }
        formulario["detalles_pedido"].append(detalle_de_pedido)

        seleccion_producto["cantidad_en_stock"] -= cantidad
    
    if not formulario["detalles_pedido"]:
        print("No se agregó ningún producto al pedido")
        return
    
    data_ordenes.append(formulario)
    agregar_orden(data_ordenes)
    guardar_procutos(data_ordenes)

    print(f"Pedido realizado {id_nueva_orden}")







