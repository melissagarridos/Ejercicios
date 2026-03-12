# Registrar 5 personas en un gimnasio.
# Por cada una pedir:
# • nombre
# • días asistidos en la semana
# • minutos promedio entrenados por día
# Clasificar:
# • menos de 3 días → bajo compromiso
# • 3 a 4 días → compromiso medio
# • 5 o más → compromiso alto
# Al final mostrar cuántas personas quedaron en cada categoría.
# Practica: ciclos, contadores, condicionales.

cliente = 0

for cliente in range(5):

    nombre = input("Ingrese el nombre del cliente: ")
    asistencia = int(input("Ingrese los dias asistidos a la semana del cliente: "))
    cliente += 1


    if asistencia < 3:
        print(f"El cliente {nombre} tiene una asistencia baja.")
    elif 3 <= asistencia <= 4:
        print(f"El cliente {nombre} tiene una asistencia media.")
    elif 5 <= asistencia <= 7:
        print(f"El cliente {nombre} tiene una asistencia alta.")
