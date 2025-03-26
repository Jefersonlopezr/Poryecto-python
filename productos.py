import json
import os
from tabulate import tabulate
from información.products import FindAll

# def cargar_productos(archivo="productos.json"):
#     """Carga productos desde un archivo JSON."""
#     with open(archivo, "r", encoding="utf-8") as f:
#         return json.load(f)

# def filtrar_por_categoria(categoria, archivo="productos.json"):
#     """Filtra productos por categoría."""
#     productos = cargar_productos(archivo)
#     return [producto for producto in productos if producto["categoria"].lower() == categoria.lower()]


# def cargar_datos(nombre_archivo):
#     """Carga datos desde un archivo JSON."""
#     if not os.path.exists(nombre_archivo):
#         return []
#     with open(nombre_archivo, "r", encoding="utf-8") as f:
#         return json.load(f)

FILENAME = "productos.json"

def read_data():
    "Lee y devuelve el contenido del archivo json"
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def buscar_producto():
    "Busca un producto en el JSON y muestra su informacion"
    data = read_data()

    if not data:
        print("No hay productos registrados")
        return
    producto_a_buscar = input("Ingrese el nombre del producto a buscar: ").strip()

    for entry in data:
        if entry["categoria"] == producto_a_buscar:
            print(f"Nombre:: {entry['nombre']}")
            print(f"Precio: {entry['precio_venta']}")
            print(f"Cantidad: {entry['cantidad_en_stock']}")
            print(f"Tipo: {entry['descripcion']}")
            return
    print(f"Producto no encontrado '{producto_a_buscar}'")

def mostrar_panes():
    "Muestra la lista de productos Panes"
    data = read_data()
    if not data:
        print("No hay productos registrados")
        return

    #Filtrar solo los productos que tienen la clave "categoria"

    data_valid =[entry for entry in data if "categoria" in entry and isinstance(entry["categoria"], str) and entry["categoria"] == "Pan"]

    if not data_valid: 
        print("No hay productos registrados en el JSON.")
        return
    
    #Ordenar los datos por puntaje de mayor a menor
    data_sorted = sorted(data_valid, key=lambda x: x["categoria"])

    # print("\n Datos guardado en 'productos.json':\n")
    # for entry in data_sorted:
    #     print(f"Nombre {entry["nombre"]}, Precio: {entry['precio_venta']}")   

    table = [[entry["nombre"], entry["precio_venta"], entry["cantidad_en_stock"]] for entry in data_sorted]
    
    print("\nLista de Panes:\n")
    print(tabulate(table, headers=["Nombre", "precio", "cantidad disponible"], tablefmt="grid"))

def mostrar_donas():
    "Muestra la lista de productos de donas"
    data = read_data()
    if not data:
        print("No hay productos registrados")
        return

    #Filtrar solo los productos que tienen la clave "categoria"

    data_valid =[entry for entry in data if "categoria" in entry and isinstance(entry["categoria"], str) and entry["categoria"] == "Dona"]

    if not data_valid: 
        print("No hay productos registrados en el JSON.")
        return
    
    #Ordenar los datos por puntaje de mayor a menor
    data_sorted = sorted(data_valid, key=lambda x: x["categoria"])

    # print("\n Datos guardado en 'productos.json':\n")
    # for entry in data_sorted:
    #     print(f"Nombre {entry["nombre"]}, Precio: {entry['precio_venta']}")

    table = [[entry["nombre"], entry["precio_venta"], entry["cantidad_en_stock"]] for entry in data_sorted]
    
    print("\nLista de Donas:\n")
    print(tabulate(table, headers=["Nombre", "precio", "cantidad disponible"], tablefmt="grid"))

def mostrar_postres():
    "Muestra la lista de productos de postres"
    data = read_data()
    if not data:
        print("No hay productos registrados")
        return

    #Filtrar solo los productos que tienen la clave "categoria"

    data_valid =[entry for entry in data if "categoria" in entry and isinstance(entry["categoria"], str) and entry["categoria"] == "Postre"]

    if not data_valid: 
        print("No hay productos registrados en el JSON.")
        return
    
    #Ordenar los datos por puntaje de mayor a menor
    data_sorted = sorted(data_valid, key=lambda x: x["categoria"])

    # print("\n Datos guardado en 'productos.json':\n")
    # for entry in data_sorted:
    #     print(f"Nombre {entry["nombre"]}, Precio: {entry['precio_venta']}")  

    table = [[entry["nombre"], entry["precio_venta"], entry["cantidad_en_stock"]] for entry in data_sorted]
    
    print("\nLista de Postres:\n")
    print(tabulate(table, headers=["Nombre", "precio", "cantidad disponible"], tablefmt="grid"))

def mostrar_bebidas():
    "Muestra la lista de productos de postres"
    data = read_data()
    if not data:
        print("No hay productos registrados")
        return

    #Filtrar solo los productos que tienen la clave "categoria"

    data_valid =[entry for entry in data if "categoria" in entry and isinstance(entry["categoria"], str) and entry["categoria"] == "Bebidas"]

    if not data_valid: 
        print("No hay productos registrados en el JSON.")
        return
    
    #Ordenar los datos por puntaje de mayor a menor
    data_sorted = sorted(data_valid, key=lambda x: x["categoria"])

    # print("\n Datos guardado en 'productos.json':\n")
    # for entry in data_sorted:
    #     print(f"Nombre {entry["nombre"]}, Precio: {entry['precio_venta']}")  

    table = [[entry["nombre"], entry["precio_venta"], entry["cantidad_en_stock"]] for entry in data_sorted]
    
    print("\nLista de Bebidas:\n")
    print(tabulate(table, headers=["Nombre", "precio", "cantidad disponible"], tablefmt="grid"))