#ejercicio8


#Área base, área lateral y área total

import math
#datos 
radio=float(input("Insertar el radio del un cilindro: "))
altura=float(input("Insertar  la altura del cilindro: "))



area_base=math.pi*(radio)**2 

print(f"El area base del cilindro es: {area_base} cm³")

area_lateral=2*math.pi*radio*altura

print(f"El area lateral del cilindro es: {area_lateral} cm²")

area_total=(2*(math.pi*(radio)**2))*(2*math.pi*radio*altura)

print(f"El area lateral del cilindro es: {area_total} cm²")
