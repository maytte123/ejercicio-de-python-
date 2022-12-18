#ejercicio10
#numero alrevez

numero = int(input("numero natural de 4 cifras:"))

c4 = numero % 10

c3 = int((numero%100)/10)

c2 = int((numero%1000)/100)

c1 = int((numero - (numero%1000))/1000)

# impresion de la solucion 

print(f"{c4}{c3}{c2}{c1}")