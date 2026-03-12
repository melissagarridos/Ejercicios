# 11. Heladería: factura de varios clientes
# Una heladería quiere registrar varios clientes hasta que el usuario
# decida salir.
# Productos:
# • cono = 3000
# • vaso = 4000
# • banana split = 9000
# Por cada cliente:
# • pedir producto
# • pedir cantidad
# • calcular total
# Al final mostrar:
# • total vendido
# • cuántos clientes se atendieron
# • cuál producto se pidió más veces
# Practica: ciclos, acumuladores, contadores

cono = 0
vaso = 0
banana_split = 0

precio_cono = 3000
precio_vaso = 4000
precio_banana_split = 9000

print("Bienvenido a la heladería, tenemos los siguientes productos:")
print(f"1. Cono: ${cono}")
print(f"2. Vaso: ${vaso}")
print(f"3. Banana Split: ${banana_split}")

opcion = int(input("¿Qué producto deseas comprar? (1, 2 o 3) "))

venta = 0

while venta == 0:

    if opcion == 1:
        print(f"Has elegido el cono, el precio es ${cono}.")
        cantidad = int(input("¿Cuántos conos deseas comprar? "))
        cono = precio_cono * cantidad

        venta = cono
    elif opcion == 2:
        print(f"Has elegido el vaso, el precio es ${vaso}.")
        cantidad = int(input("¿Cuántos vasos deseas comprar? "))
        vaso = precio_vaso * cantidad
        venta = vaso
    elif opcion == 3:
        print(f"Has elegido el banana split, el precio es ${banana_split}.")
        cantidad = int(input("¿Cuántos banana splits deseas comprar? "))
        banana_split = precio_banana_split * cantidad
        venta = banana_split
    else:
        print("Opción no válida. Por favor, elige entre 1, 2 o 3.")
        opcion = int(input("¿Qué producto deseas comprar? (1, 2 o 3) "))

print(f"El total de tu compra es: ${venta}. ¡Gracias por tu compra!")


