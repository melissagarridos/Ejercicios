# 20. Club recreativo: control de membresías
# Registrar varias personas en un club.
# Por cada una pedir:
# • nombre
# • edad
# • tipo de plan: básico, premium, familiar
# Reglas:
# • básico = 50000
# • premium = 90000
# • familiar = 130000
# Además:
# • si la persona es menor de 18, mostrar “registro juvenil”
# • si tiene 60 o más, mostrar “beneficio senior”
# Al final mostrar:
# • total recaudado
# • cantidad de personas por plan
# • plan más vendido
# Practica: condicionales, contadores, acumuladores.

basico = 0
premium = 0
familiar = 0

precio_basico = 50000
precio_premium = 90000
precio_familiar = 130000


personas = 0

cantidad = input("Cantidad de personas del club: ")

if cantidad.isdigit():

    cantidad = int(cantidad)

    for personas in range(cantidad):

        nombre = input("Nombre: ")
        edad = input("Edad: ")

        if edad.isdigit():

            edad = int(edad)

            if edad < 18:
                print("Registro juvenil")

            elif edad >= 60:
                print("Beneficio senior")

            print("""Los tipos de planes son:
                  1. básico
                  2. premium
                  3. familiar""")

            plan = input("Plan: ")

            if plan.isdigit():

                plan = int(plan)

                if plan == 1:
                    basico += 1


                elif plan == 2:
                    premium += 1
            

                elif plan == 3:
                    familiar += 1

            else:
                print("Introduzca una dato valido")
                continue

        else:   
            print("Introduzca una dato valido")
            continue

else:
    print("Introduzca una cantidad valida")
    

total_basico = basico * precio_basico

total_premium = premium * precio_premium

total_familiar = familiar * precio_familiar

print("El total recaudado en el plan básico es $", total_basico, " por un total de ", basico, " personas.")

print("El total recaudado en el plan premium es $", total_premium, " por un total de ", premium, " personas.")

print("El total recaudado en el plan familiar es $", total_familiar, " por un total de ", familiar, " personas.")