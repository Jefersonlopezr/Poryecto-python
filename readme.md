
# Panadería - JEF PANADERIA

Este proyecto consiste en el desarrollo de un sistema de gestión para una panadería que permita el manejo eficiente de productos, pedidos, y sus detalles asociados. El sistema facilitará la administración de productos disponibles (como panes, pasteles, y postres), el registro de pedidos de los clientes y la gestión de los detalles específicos de cada pedido. El objetivo es optimizar el control de inventario, asegurar el manejo correcto de los precios, y mejorar la experiencia del cliente.

## Problema

La panadería enfrenta desafíos relacionados con la administración de su inventario y la gestión de los pedidos de los clientes. Actualmente, el registro de productos y pedidos se realiza de manera manual, lo que conlleva errores humanos, pérdida de datos y dificultades para dar seguimiento a los detalles de los pedidos. La panadería requiere un sistema digital que centralice la información, permita un control efectivo del inventario y registre cada pedido de manera organizada.

## Características Principales

1. **Gestión de Productos**:
   - Registro de productos de panadería como panes, pasteles, postres, etc.
   - Almacenamiento de información relevante como nombre del producto, categoría (tipo de pan, pastel, postre), descripción, proveedor, cantidad en stock, precios de venta y de compra.
2. **Gestión de Pedidos**:
   - Creación de nuevos pedidos por parte de los clientes.
   - Registro de productos dentro de un pedido, incluyendo cantidad, precio por unidad y línea del pedido.
   - Capacidad para editar y eliminar pedidos.
3. **Inventario Automatizado**:
   - Reducción automática del inventario disponible cuando se registra un pedido.
   - Control de stock y alertas si un producto está por agotarse.
4. **Consultas y Búsquedas**:
   - Búsqueda de productos por nombre, categoría o código.
   - Filtrado de pedidos por código de pedido o por producto incluido.
5. **Manejo de Archivos y Persistencia**:
   - Almacenamiento de datos en archivos JSON para garantizar la persistencia de la información entre sesiones.

# Tecnologías y Herramientas

    - Recurso
    - GitHub: 
# Estructura de Datos

## 1. Productos

Los productos de la panadería serán representados mediante diccionarios. Cada producto tendrá las siguientes propiedades:

```json
productos =   {
        "codigo_producto": "PN-001",
        "nombre": "Pan Integral",
        "categoria": "Pan",
        "descripcion": "Pan de harina integral con semillas.",
        "proveedor": "Panadería Natural",
        "cantidad_en_stock": 50,
        "precio_venta": 2000,
        "precio_proveedor": 1000
        },
        {
        "codigo_producto": "PN-002",
        "nombre": "Pan de Queso",
        "categoria": "Pan",
        "descripcion": "Pan de queso mozzarella.",
        "proveedor": "Panadería Natural",
        "cantidad_en_stock": 30,
        "precio_venta": 2500,
        "precio_proveedor": 1200
        }
```

## 2. Pedidos

Cada pedido realizado por un cliente estará representado como un diccionario. Un pedido incluye detalles sobre qué productos han sido solicitados, la cantidad y el precio.

```json
pedidos = [
    {
        "codigo_pedido": 1,
        "codigo_cliente": "CL-001",
        "fecha_pedido": "2024-10-01",
        "detalles_pedido": [
            {"codigo_producto": "PN-001", "cantidad": 3, "precio_unidad": 3.5, "numero_linea": 1},
            {"codigo_producto": "PS-002", "cantidad": 1, "precio_unidad": 15.0, "numero_linea": 2}
        ]
    },
    {
        "codigo_pedido": 2,
        "codigo_cliente": "CL-002",
        "fecha_pedido": "2024-10-02",
        "detalles_pedido": [
            {"codigo_producto": "PN-003", "cantidad": 5, "precio_unidad": 2.5, "numero_linea": 1},
            {"codigo_producto": "PS-001", "cantidad": 2, "precio_unidad": 12.0, "numero_linea": 2}
        ]
    }
]
```

## 3. Detalles del Pedido


```json
detalles_pedido = [
    
    {
        "codigo_pedido": 1,
        "codigo_cliente": "CL-001",
        "fecha_pedido": "2024-10-01",
        "detalles_pedido": []
    },
    {
        "codigo_pedido": 2,
        "codigo_cliente": "CL-001",
        "fecha_pedido": "2025-01-11",
        "detalles_pedido": [
            {
                "codigo_producto": "PS-002",
                "cantidad": 30,
                "precio_unidad": 15.0,
                "numero_linea": 1
            }
        ]
    } 
]

```
# Resumen de la Estructura del Sistema

- **Productos**: Diccionario con código de producto, nombre, categoría, proveedor, cantidad en stock y precios.
- **Pedidos**: Diccionario con código de pedido, código del cliente, fecha del pedido y una lista de detalles del pedido.
- **Detalles de Pedido**: Incluye código de producto, cantidad solicitada, precio por unidad y número de línea dentro del pedido.

# Consideraciones Técnicas

- **Persistencia**: Los datos serán almacenados y gestionados mediante archivos JSON.
- **Modularidad**: El sistema se organizará en funciones modulares para la gestión de productos, pedidos, y la manipulación de archivos.
- **Validación**: Se implementarán validaciones para asegurar que los códigos de producto y de pedido sean únicos, así como la verificación del stock disponible antes de procesar un pedido.