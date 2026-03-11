# 1. Heladería: sabor más pedido
# Una heladería quiere registrar 5 pedidos.
# Por cada cliente, el programa debe pedir el sabor elegido:
# • vainilla
# • chocolate
# • fresa
# Al final debe mostrar cuántas veces se pidió cada sabor.
# Practica: ciclos, condicionales, contadores

vainilla = 0
chocolate = 0
fresa = 0

opciones = ["vainilla", "chocolate", "fresa"]

name = str(input("Ingrese su nombre: ")).capitalize()

print("Biendenido/a ", name)

ciclo = 1

while ciclo == 1:

    eleccion = input("Desea hacer un pedido: si / no: ").lower()

    if eleccion == "si": 

        print("Por favor seleccione un sabor: ", opciones)

        sabor = input("Seleccione su sabor: ").lower()

        if sabor == "vainilla":
            print("Preparando su helado de vainilla")
            vainilla += 1

        elif sabor == "chocolate":
            print("Preparando su helado de chocolate")
            chocolate += 1

        elif sabor == "fresa":
            print("Preparando su helado de fresa")
            fresa += 1

        elif sabor != opciones:
            print("Seleccione una opcion valida")
        eleccion = 0

    elif eleccion == "no":
        print("Ha seleccionado las siguientes opciones: ")
        print("Vainilla: ", vainilla)
        print("Fresa: ", fresa)
        print("Chocolate: ", chocolate)
        print("Ha finalizado su pedido")
        break

    else:
        print("Seleccione una opcion valida")
        continue



