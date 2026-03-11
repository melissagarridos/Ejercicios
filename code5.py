# 5. Tienda de mascotas: alimento por tipo de animal
# Pide el tipo de mascota:
# • perro
# • gato
# • conejo
# Luego muestra una recomendación de alimento según el animal.
# Practica: comparaciones con texto.

mascotas=["perro ", "gato ","conejo "]


especie = input("Por favor seleccione su mascota: perro, gato o conejo: ").lower()

if especie == "perro":

    # Perro
    print("Perro:")
    print("Mejor comida: concentrado de buena calidad, pollo o carne cocida.")
    print("Tambien puede comer arroz y algunas verduras como zanahoria.")

elif especie == "gato":
    # Gato
    print("Gato:")
    print("Mejor comida: concentrado o comida humeda especial para gatos.")
    print("Tambien puede comer pollo o pescado cocido sin sal.")

elif especie == "conejo":
    # Conejo
    print("Conejo:")
    print("Mejor comida: heno como base principal de la dieta.")
    print("Tambien puede comer verduras frescas como lechuga romana o cilantro.")

else:
    print("Por favor seleccione una opcion valida")
    
