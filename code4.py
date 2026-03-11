# 4. Cine: entrada según edad
# El precio de la entrada cambia así:
# • niños menores de 12 → 8000
# • adultos de 12 a 59 → 12000
# • mayores de 60 → 9000
# Pide la edad del cliente y muestra cuánto debe pagar.
# Practica: condicionales.

niños = list(range(12))
adultos = list(range(12,59)) 
senior = list(range(60,200))

age = input("Por favor ingrese su edad: ")

precio_niños = 8000
precio_adultos = 12000
precio_senior = 9000

if age.isdigit():

    if age in niños:
        print("Su total a pagar es: ", precio_niños)

    elif age in adultos:
        print("Su total a pagar es: ", precio_adultos)
        
    elif age in senior:
        print("Su total a pagar es: ", precio_senior)

else: 
    print("Seleccione una opcion valida")