""" Actividad Extra
Creación de un programa básico de gestión de inventario.
Desarrollar un programa en Python que permita gestionar un inventario
simple de productos, incluyendo funciones básicas como agregar productos,
eliminar productos y mostrar el inventario.
El programa debe tener un menú interactivo que permita al usuario
seleccionar las siguientes operaciones:
Agregar un nuevo producto al inventario, solicitando al usuario el nombre y
la cantidad inicial del producto.
Eliminar un producto existente del inventario, solicitando al usuario el
nombre del producto a eliminar.
Mostrar el inventario actual, que incluya el nombre y la cantidad de cada
producto.
Salir del programa.
El inventario puede ser almacenado utilizando un diccionario simple, donde
las claves sean los nombres de los productos y los valores sean las cantidades. Se
deben manejar situaciones simples como la introducción de productos duplicados
o la eliminación de productos inexistentes.
"""
import random 
products = {}
seguir = True
nom_inv = "[untitled]"
options = [
    "Mostrar el inventario", 
    "Agregar nuevo producto",
    "Eliminar producto",
    "Consultar stock de un producto",
    "Actualizar stock de un producto",
    "Renombrar inventario",
    "Cerrar inventario"

]
while(seguir):
    print(f"Inventario {nom_inv}")
    print(f"Seleccione una opción")
    for i, op in enumerate(options):
        print(f"{i+1}. {op}") 
    print()
    op_chosen = input()
    print()
    if op_chosen.isnumeric(): op_chosen = int(op_chosen)
    match op_chosen:
        case 1:
            if len(products) == 0:
                print("Inventario vacío. ") 
            else:
                for nom, stock in products.items():
                    print(f"Nombre del producto: {nom}. \nStock disponible: {stock} \n")
        case 2:
            print("Ingrese el nombre del producto y la cantidad de unidades disponibles")
            new_name = input("Nombre del producto: ")
            new_stock = input("unidades disponibles: ")
            if new_name in products:
                user_choice = input(f"Ya existe un producto con ese nombre. Desea sobreescribirlo? \n"
                    f"1. Sí \n"
                    f"2. No \n"
                    )
                if not user_choice.isnumeric() or not (1 <= int(user_choice) <= 2):
                    print("Opción inválida. Inventario no actualizado.")
                else:
                    user_choice = int(user_choice)
                    if user_choice == 1:
                        if not new_stock.isnumeric(): 
                            print("Cantidad inválida. Inventario no actualizado.")
                        else:
                            products[new_name] = int(new_stock)
                            print("Inventario actualizado.")
                    else:
                        print("Inventario no actualizado.")
            else:
                if not new_stock.isnumeric(): 
                    print("Cantidad inválida. Inventario no actualizado.")
                else:
                    products[new_name] = int(new_stock)
                    print("Inventario actualizado.")
        case 3:
            user_input = input(f"Ingrese el nombre del producto que quiere eliminar (cc para cancelar): ")
            if user_input in products:
                products.pop(user_input)
                print("Inventario actualizado.")
            elif user_input == "cc":
                print("Operación cancelada.")
            else:
                print("Producto no encontrado. Inventario no actualizado.")
        case 4:
            user_input = input(f"Ingrese el nombre del producto: ")
            if user_input in products:
                print(f"Stock disponible: {products[user_input]}")
            else:
                print("Producto no encontrado. ")
        case 5:
            user_input = input(f"Ingrese el nombre del producto: ")
            if user_input in products:
                user_choice = input(f"1.Agregar unidades \n2.Descontar unidades \n")
                if user_choice.isnumeric(): user_choice = int(user_choice)
                match user_choice:
                    case 1:
                        un = input(f"Ingrese la cantidad de unidades que quiere agregar: ")
                        if un.isnumeric():
                            un = int(un)
                            products[user_input] = products[user_input] + un
                            print("Inventario actualizado.")
                        else:
                            print("Valor inválido. Inventario no actualizado.")
                    case 2:
                        un = input(f"Ingrese la cantidad de unidades que quiere descontar: ")
                        if un.isnumeric():
                            un = int(un)
                            products[user_input] = max(0, products[user_input] - un)
                            print("Inventario actualizado.")
                        else:
                            print("Valor inválido. Inventario no actualizado.")                    
                    case _:
                        print("Opción inválida. Inventario no actualizado.")
            else:
                print("Producto no encontrado.")
        case 6:
            user_input = input(f"Ingrese el nuevo nombre del inventario (cc para cancelar): ")
            if(user_input == "cc"):
                print("Operación cancelada.")
            else:
                nom_inv = user_input
        case 7:
            print("Inventario cerrado.")
            exit(0)
        case _:
            print("Por favor, ingrese una opción válida (del 1 al 7).")
    print()
    ok = False
    while not ok:
        user_choice = input(f"1.Ver más opciones \n2.Cerrar inventario\n\n")
        if not user_choice.isnumeric() or not(1 <= int(user_choice) <= 2): #seria mejor hacerlo con un match como arriba?
            print(f"Ingrese una opción válida (1 o 2).")
        else: #opcion valida 
            user_choice = int(user_choice)
            ok = True
            if(user_choice == 2): seguir = False #tmb podria usar un while true y hacer un exit acá
        print()
print("Inventario cerrado.")