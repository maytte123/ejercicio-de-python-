#ejercicio11
'''Dado dos números enteros de 3 cifras, desarrolle el programa que muestre la cifra primera y 
tercera cifras intercambiadas entre ambos números. Ejemplo 123 y 456  624 y 351.'''

num1=int(input("poner el numero 1: "))


num2=int(input("poner el numero 2: "))
#solucion 

num1_c1=num1//100
num1_c2=num1%100//10
num1_c3=num1%10

num2_c1=num2//100
num2_c2=num2%100//10
num2_c3=num2%10

print("---numeros intercambiados---")

print("numero 1",(num2_c3*100)+(num1_c2*10)+(num2_c1))

print("numero 2",(num1_c3*100)+(num2_c2*10)+(num1_c1))