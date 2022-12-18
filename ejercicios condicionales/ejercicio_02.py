# ejercicio 2 
# CONDICIONALES numeros de unidades 
#presentacion de los datos obtenidos 
numero_unidades = float(input("cantidad de productos: "))

#solucion de los datos 

if numero_unidades>= 1 and numero_unidades <= 50:

    print("  regalo de 5 caramelos")

elif numero_unidades >= 51 and numero_unidades <= 100:

    print("regalo de 10 caramelos")
#si no 
else: 
    print("vamos a regalo de 15 caramelos")

importe = numero_unidades * 20



if importe> 700:

    descuento = importe * 0.16

    totalidad_a_pagar = importe - descuento  
    print("el descuento es",totalidad_a_pagar)



elif importe< 700 and importe> 501:

    descuento= importe * 0.14
    
    totalidad_a_pagar= importe - descuento  
    print("el descuento es",totalidad_a_pagar)

else :
    descuento= importe * 0.12
    totalidad_a_pagar = importe - descuento  
    print("el descuento es",totalidad_a_pagar)