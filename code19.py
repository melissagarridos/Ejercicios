# 19. Tienda de ropa deportiva: inventario crítico
# Registrar 10 productos.
# Por cada producto pedir:
# • nombre
# • cantidad disponible
# Clasificar:
# • 0 → agotado
# • 1 a 5 → stock bajo
# • 6 o más → stock normal
# Al final mostrar:
# • cuántos están agotados
# • cuántos tienen stock bajo
# • cuántos están normales
# Practica: clasificación por rangos, ciclo.


nombre = ""

cantidad = 0

producto = 0

agotado = 0

bajo = 0

normal = 0

for producto in range(10):

    nombre = input("Nombre del producto: ").lower().strip()

    cantidad = input("Cantidad disponible: ")

    if cantidad.isdigit():

        cantidad = int(cantidad)

        if cantidad == 0:
            print("Agotado")
            agotado += 1

        if 1 <= cantidad <= 5:
            print("Stock bajo")
            bajo += 1

        if cantidad >= 6:
            print("Stock normal")
            normal += 1
            
    else:
        print("Introduzca una cantidad valida")
        continue


print(f"Productos agotados: ", agotado)
print(f"Productos con stock bajo: ", bajo)
print(f"Productos con stock normal: ", normal)