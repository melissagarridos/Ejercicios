# 3. Cafetería: total de una compra sencilla
# En una cafetería venden:
# • café = 4000
# • té = 3500
# • jugo = 5000
# Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
# Luego muestra el total a pagar.
# Practica: condicionales, variables, multiplicación

cafe = 0
te = 0
jugo = 0

precio_cafe = 4000
precio_te = 3500
precio_jugo = 5000

opciones = ["cafe", "te", "jugo"]

eleccion = input("Seleccione que bebida desea: cafe, te o jugo: ").lower()

if eleccion not in 


cantidad = input("¿Cuantas unidades desea comprar?: ")


if eleccion == "cafe" or "café":
    total_cafe = cafe + cantidad
    total = precio_cafe * total_cafe

    print("Su total a pagar es: ", total)


elif eleccion == "te" or "té":
    total_te = te + cantidad
    total = precio_te * total_te

    print("Su total a pagar es: ", total)


elif eleccion == "jugo":
    total_jugo = jugo + cantidad
    total = precio_jugo * total_jugo

    print("Su total a pagar es: ", total)


else:
    print("Seleccione una opcion valida")

