# Registrar varios pedidos en una cafetería hasta que el usuario escriba
# “salir”.
# Productos:
# • café = 4000
# • capuchino = 7000
# • pastel = 6000
# Reglas:
# • si la compra supera 20000, aplicar 10% de descuento
# • si no, cobrar normal
# Mostrar total por cliente y al final total acumulado del día.
# Practica: menú simple, ciclos, descuentos.

precio_café = 4000
precio_capuchino = 7000
precio_pastel = 6000

cafe = 0
capuchino = 0
pastel = 0

print("Bienvenido a la cafetería, tenemos los siguientes productos:")
print(f"1. Café: ${precio_café}")
print(f"2. Capuchino: ${precio_capuchino}")
print(f"3. Pastel: ${precio_pastel}")           

opcion = int(input("¿Qué producto deseas comprar? (1, 2 o 3) "))

compra = 0
while compra == 0:

    if opcion == 1:
        print(f"Has elegido el café, el precio es ${precio_café}.")
        cantidad_cafe = int(input("¿Cuántos cafés deseas comprar? "))
        cantidad_cafe_total = precio_café * cantidad_cafe
        compra = cantidad_cafe_total
        
    elif opcion == 2:
        print(f"Has elegido el capuchino, el precio es ${precio_capuchino}.")
        cantidad_capuchino = int(input("¿Cuántos capuchinos deseas comprar? "))
        cantidad_capuchino_total = precio_capuchino * cantidad_capuchino
        compra = cantidad_capuchino_total

    elif opcion == 3:

        print(f"Has elegido el pastel, el precio es ${precio_pastel}.")
        cantidad_pastel = int(input("¿Cuántos pasteles deseas comprar? "))
        cantidad_pastel_total = precio_pastel * cantidad_pastel
        compra = cantidad_pastel_total
        
    else:
        print("Opción no válida. Por favor, elige entre 1, 2 o 3.")

total_compra = compra


if total_compra > 20000:
    total_compra = total_compra * 0.9
    print(f"El total de tu compra es: ${total_compra}. ¡Gracias por tu compra!")

else:
    print(f"El total de tu compra es: ${total_compra}. ¡Gracias por tu compra!")
