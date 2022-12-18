
#ejercicio 12 
#inicio


num_segundos=int(input(" numero expresados en segundos"))


dias=((num_segundos//60)//60)//24

print("dias",dias)

horas=((num_segundos//60)//60)%24

print("horas",horas)

minutos=(num_segundos//60)%60

print("minutos",minutos)

segundos=num_segundos%60

#salida de los datos

print("segundos",segundos)
