# 6. Parqueadero: cobro por horas
# Pide cuántas horas estuvo un carro en un parqueadero.
# Reglas:
# • primera hora = 5000
# • cada hora adicional = 3000
# Muestra el total a pagar.
# Practica: condicionales y operaciones.

primera_hora = 5000
hora_adicional = 3000

cantidad_horas = input("Por favor ingrese el numero de horas en el parqueadero: ")

if cantidad_horas.isdigit():

    cantidad_horas = int(cantidad_horas)

    if cantidad_horas == 1:
        print("El total a pagar es: ", primera_hora)

    elif cantidad_horas > 1:
        horas_adicionales = cantidad_horas - 1
        total_pago = (horas_adicionales * hora_adicional) + primera_hora
        print("El total a pagar es: ", total_pago)

else:
    print("Ingrese una cantidad de horas valida")