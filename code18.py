# 18. Centro de idiomas: evaluación de estudiantes
# Registrar varios estudiantes de un curso de inglés.
# Por cada uno pedir:
# • nombre
# • nota speaking
# • nota listening
# • nota reading
# Calcular promedio simple y clasificar:
# • menor de 60 → bajo
# • 60 a 79 → medio
# • 80 o más → alto
# Al final mostrar:
# • promedio general del grupo
# • mejor estudiante
# • cuántos quedaron en cada nivel
# Practica: promedios, máximos, contadores.

nombre = ""

estudiantes = []

speaking = 0

listening = 0

reading = 0

promedio = 0

promedios = []

estudiantes_bajo = 0

estudiantes_medio = 0

estudiantes_alto = 0

mayor_promedio = 0

mejor_estudiante = ""

suma_promedio = 0

cantidad = input("Indique la cantidad de estudiantes: ")

if cantidad.isdigit():

    cantidad = int(cantidad)

    for estudiante in range(cantidad):

        nombre = input("Nombre: ").capitalize().strip()
        speaking = float(input("Nota speaking: "))
        listening = float(input("Nota listening: "))
        reading = float(input("Nota reading: "))

        promedio = (speaking + listening + reading)/3

        if promedio < 60:

            estudiantes_bajo +=1

        elif promedio >= 60 <= 79:

            estudiantes_medio +=1

        elif promedio >= 80:

            estudiantes_alto +=1

        suma_promedio += promedio

        estudiante = {
            "nombre": nombre,
            "speaking": speaking,
            "listening": listening,
            "reading": reading,
            "promedio": promedio
        }

        estudiantes.append(estudiante)

        if promedio > mayor_promedio:
            mayor_promedio = promedio
            mejor_estudiante = nombre


    promedio_general = (suma_promedio)/cantidad

    print(f"El promedio del grupo es: ", promedio_general)

    print(f"El mejor estudiante del grupo es: ", mejor_estudiante)

    print(f"El mejor promedio del grupo es: ", mayor_promedio)

    print(f"El numero de estudiantes en el nivel bajo es: ", estudiantes_bajo)

    print(f"El numero de estudiantes en el nivel medio es: ", estudiantes_medio)

    print(f"El numero de estudiantes en el nivel alto es: ", estudiantes_alto)

else:
    print("Introduzca un valor valido")

