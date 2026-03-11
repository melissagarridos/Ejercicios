# 7. Peluquería: turno del día
# Pide la hora de llegada de un cliente en formato entero de 0 a 23.
# Mostrar:
# • mañana si está entre 6 y 11
# • tarde si está entre 12 y 17
# • noche si está entre 18 y 22
# • fuera de horario en cualquier otro caso
# Practica: rangos con condicionales.

mañana = list(range(6,11))
tarde = list(range(12,17))
noche = list(range(18,22))


hora_ingreso = input("Ingrese su hora de llegada en formato militar (1,24): ")

if hora_ingreso.isdigit():

    hora_ingreso = int(hora_ingreso)

    if hora_ingreso in mañana:

        print("Usted ingresó en la mañana")

    elif hora_ingreso in tarde:

        print("Usted ingresó en la tarde")

    elif hora_ingreso in noche:

        print("Usted ingresó en la noche")

    else:
        print("Usted ingresó fuera de horario")

else:
    print("Ingrese una hora valida")



