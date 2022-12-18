#Ejercicio 3

#datos obtenidos 

angulo =  int(input("digite el ángulo: "))

#operacion 

if angulo == 0:
    print("El ángulo es nulo")

if angulo == 90:
    print("El angulo es recto")

if angulo == 360:
    print("El angulo es completo")

if angulo == 180:
    print("El angulo es llano")

if 0 < angulo < 90:
    print("El angulo es agudo")

if 90 < angulo < 180:
    print("El angulo es obtuso")

if 180 < angulo < 360:
    print("El angulo es cóncavo")