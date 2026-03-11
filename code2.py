# 2. Gimnasio: acceso por edad
# Un gimnasio ofrece clases según la edad:
# • menor de 13 → no puede ingresar
# • de 13 a 17 → clase juvenil
# • de 18 a 59 → clase general
# • 60 o más → clase senior
# Pide la edad de una persona y muestra a qué grupo pertenece.
# Practica: if, elif, else.

prohibido = list(range(14))
juvenil = list(range(14, 18)) 
general = list(range(18, 60))
senior = list(range(60,200))

age = input("Por favor ingrese su edad: ")

if age in prohibido:
    print("No puede usar estas instalaciones aún")

elif age in juvenil:
    print("Pertenece a la categoria juvenil")
    
elif age in general:
    print("Pertenece a la categoria general")

elif age in senior:
    print("Pertenece a la categoria senior")

else: 
    print("Seleccione una opcion valida")