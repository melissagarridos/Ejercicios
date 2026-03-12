# 15. Parqueadero: control de vehículos
# Registrar 8 vehículos en un parqueadero.
# Por cada uno pedir:
# • placa
# • tipo: carro o moto
# • horas parqueado
# Tarifas:
# • carro: 4000 por hora
# • moto: 2000 por hora
# Al final mostrar:
# • total recaudado
# • cuántos carros ingresaron
# • cuántas motos ingresaron
# • cuál vehículo pagó más
# Practica: ciclos, máximos, acumuladores.


carro = 0
moto = 0

precio_carro = 4000
precio_moto = 2000

pago_moto = 0
pago_carro = 0


for ingreso in range (8):

    placa = input("Indique la placa: ").upper().strip()

    tipo_vehiculo = input("¿Carro o moto?: ").lower().strip()

    

    if tipo_vehiculo == "carro":

        carro += 1

        horas_carro = int(input("¿Horas parqueado?: "))

        pago_carro += horas_carro

        

    elif tipo_vehiculo == "moto":

        moto += 1

        horas_moto = int(input("¿Horas parqueado?: "))

        pago_moto += horas_moto 

       

    else:
        print("Ingrese una opcion valida")

recaudo_carro = carro * pago_carro * precio_carro

recaudo_moto = moto * pago_moto * precio_moto

print(f"El total recaudado por carros es: ", recaudo_carro)

print(f"El total recaudado por motos es: ", recaudo_moto)

print(f"Ingresaron ", moto, " motos")

print(f"Ingresaron ", carro, " carros")

if recaudo_carro > recaudo_moto:

    print("Se recaudó más en carros")

elif pago_carro < recaudo_moto:

    print("Se recaudó más en motos")

elif recaudo_moto == recaudo_carro:

    print("EL recaudo fue igual")

