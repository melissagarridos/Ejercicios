# 17. Peluquería: agenda de atención
# Una peluquería atiende 7 clientes al día.
# Por cada cliente pedir:
# • nombre
# • servicio solicitado: corte, cepillado, tintura
# • valor pagado
# Al final mostrar:
# • total del día
# • cantidad de clientes por servicio
# • servicio más solicitado
# Practica: contadores, acumuladores, comparaciones.

corte = 0

cepillado = 0

tintura = 0

cliente = 0

total_pago = 0

total = 0

for cliente in range (7):

    nombre = input("Bienvenido/a registre su nombre: ").capitalize()

    print("""Los servicios disponibles son: 
    1. Corte
    2. Cepillado
    3. Tintura""")

    servicio = input("Indique que servicio desea: ")

    if servicio.isdigit():

        servicio = int(servicio)

        if servicio == 1:

            corte += 1
            cliente += 1

        elif servicio == 2:

            cepillado += 1
            cliente += 1

        elif servicio == 3:

            tintura += 1
            cliente += 1

        else:
            print("Seleccione una opcion valida")
            continue

    else:
        print("Seleccione una opcion valida")
        continue

    pago = input("Introduzca el total a pagar: ")

    if pago.isdigit():

        pago = float(pago)

        total_pago += pago

    else:
        print("Seleccione una opcion valida")
        continue


total = total_pago 

print(f"El total del dia es: ", total)

print(f"El de clientes del dia es: ", cliente)

if cepillado > tintura and cepillado > corte:

    print("Se recaudó más en cepillado")

elif tintura > cepillado and tintura > corte:

    print("Se recaudó más en tintura")

elif corte > cepillado and corte > tintura:

    print("Se recaudó más en corte")

elif corte == cepillado == tintura:

    print("EL recaudo fue igual")