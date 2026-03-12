# 14. Cine: control de sala
# Pedir la capacidad total de una sala de cine y luego registrar cuántas
# personas ingresan.
# Por cada persona pedir edad y clasificar:
# • niño
# • adulto
# • adulto mayor
# Al final mostrar:
# • total de personas ingresadas
# • cuántos niños
# • cuántos adultos
# • cuántos adultos mayores
# • si la sala se llenó o no
# Practica: ciclos con límite, contadores.

niño = 0
adulto = 0
senior = 0

capacidad = input("Indique la capacidad total de la sala: ")

total_personas = 0

if capacidad.isdigit():

    capacidad = int(capacidad)

    for total_personas in range(capacidad):
            
            ingreso = input("¿Desea ingresar a la sala? si / no: ").lower().strip()

            if ingreso == "si":

                edad = input("Introduzca su edad: ")

                if edad.isdigit():
                    
                    edad = int(edad)

                    if edad < 12:

                        niño += 1
                        total_personas += 1

                    elif 13 <= edad <= 59:

                        adulto += 1
                        total_personas += 1

                    elif edad >= 60:

                        senior += 1
                        total_personas += 1


                    else: 
                        print("Introduzca una edad valida")
                        continue

                else:
                
                    print("Introduzca una edad valida")
                    continue

            elif ingreso == "no":


                total_personas = niño + adulto + senior

            else:
        
                print("Introduzca una opción valida")

    if total_personas < capacidad:

        print(f"Hay un total de ", {niño}, "niños")
        print(f"Hay un total de ", {adulto}, "adultos")
        print(f"Hay un total de ", {senior}, "adultos mayores")
        print(f"Hay un total de ", {total_personas}, "personas en la sala")
        print("La sala no está llena")
        

    elif total_personas == capacidad:

        print(f"Hay un total de ", niño, " niños")
        print(f"Hay un total de ", adulto, " adultos")
        print(f"Hay un total de ", senior, " adultos mayores")
        print(f"Hay un total de ", total_personas, " personas en la sala")
        print("La sala esta llena")

else:
    
    print("Introduzca una opción valida")
    
