# 8. Tienda deportiva: contar productos caros
# Pide el precio de 6 productos deportivos.
# Al final indica cuántos cuestan más de 100000.
# Practica: ciclo, contador, condicional.


numero_producto = 0
productos_caros = 0

while numero_producto < 6:

    precio_producto = input("Por favor ingrese el precio del producto: ")
    print("")


    if precio_producto.isdigit():

        precio_producto = int(precio_producto)

        numero_producto += 1

        if precio_producto > 100000:
            productos_caros += 1
 

        print("EL total de productos caros es: ", productos_caros)
        print("")
        print("EL total de productos es: ", numero_producto)
        print("")


    else:
        print("Ingrese un producto valido")
        continue
