# 10. Academia de baile: asistencia
# Pide la cantidad de clases asistidas por un estudiante en un mes.
# Reglas:
# • menos de 5 → asistencia baja
# • entre 5 y 8 → asistencia media
# • 9 o más → asistencia alta
# Practica: clasificación por rangos.

clases_asistidas = int(input("¿Cuántas clases has asistido este mes? "))

if clases_asistidas < 5:
    print("Tu asistencia es baja.")
elif 5 <= clases_asistidas <= 8:
    print("Tu asistencia es media.")
else:    print("Tu asistencia es alta.")    