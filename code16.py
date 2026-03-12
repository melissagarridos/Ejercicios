# 16. Tienda de mascotas: ventas por categoría
# Registrar ventas de una tienda de mascotas.
# Categorías:
# • alimento
# • juguete
# • accesorio
# Pedir 10 ventas. En cada venta:
# • categoría
# • valor de la compra
# Al final mostrar:
# • cuánto se vendió por cada categoría
# • cuál categoría generó más dinero
# Practica: acumuladores separados


categorias = ["alimento", "juguete", "accesorio"]

alimento = 0

juguete = 0

accesorio = 0

precio_alimento = 5000

precio_juguete = 8000

precio_accesorio = 4000

venta = 0

print("""Las categorias disponibles son: 
1) alimento
2) juguete
3) accesorio""")

for venta in range (10):

    seleccion = input("Seleccione una categoria: ")

    if seleccion.isdigit():

        seleccion = int(seleccion)

        if seleccion == 1:

            alimento += 1

        elif seleccion == 2:

            juguete += 1

        elif seleccion == 3:

            accesorio += 1

        else: 
            print("Seleccione una opcion valida")
            continue

    else: 
        print("Seleccione una opcion valida")
        continue


venta_alimento = alimento * precio_alimento

venta_accesorio = accesorio * precio_accesorio

venta_juguete = juguete * precio_juguete



print(f"Se vendió $", venta_accesorio, " en accesorios")

print(f"Se vendió $", venta_alimento, " en alimentos")

print(f"Se vendió $", venta_juguete, " en juguetes")


if venta_juguete > venta_alimento and venta_juguete > venta_accesorio:
    print("Se recaudó más en juguetes")

elif venta_accesorio > venta_alimento and venta_accesorio > venta_juguete:
    print("Se recaudó más en accesorios")

elif venta_alimento > venta_accesorio and venta_alimento > venta_juguete:
    print("Se recaudó más en alimentos")

elif venta_accesorio == venta_alimento == venta_juguete:
    print("Se recaudó por igual")

