#ejercicio 10 

#notas menor y mayor

primner_nota =  int(input("ingresar la 1"))

segunda_nota =  int(input("ingresar la nota 2 "))

tercer_nota =  int(input("inserte la nota 3 "))

cuarta_nota =  int(input("ingresar la cuarta nota"))
#si
if primner_nota<segunda_nota:

   primner_nota<tercer_nota

   primner_nota<cuarta_nota

   elimine=primner_nota
   #sino
else:
   #si
    if segunda_nota<primner_nota:

       segunda_nota<tercer_nota

       segunda_nota<cuarta_nota

       elimine=segunda_nota
       #sino
    else:
        elimine=tercer_nota

total_de_promedio=(primner_nota+segunda_nota+tercer_nota+cuarta_nota-elimine)/3
#salida de los datos 

print("su premedio fue",total_de_promedio)

print("y la nota eliminada ",elimine)



