#ejercicio 15 
#problema del monto vendido y la comision y descuento 

moto_Tvendido = float(input(" monto vendidio "))

categoria=float(input("escriba la categoria"))
sbasico=250

if  (categoria==1):

 comision = 0.1425*moto_Tvendido
if (categoria== 2):

 comision = 0.1300 *moto_Tvendido
if (categoria == 3):

 comision = 0.1175 *moto_Tvendido
#sueldo bruto

sbruto = sbasico + comision
#descuento 
if (sbruto > 3500):
 descuento = 0.15 * sbruto

else: 
 descuento = 0.08 * sbruto
#  sueldo neto 

sneto = sbruto-descuento

print("sueldo basico",sbasico)

print("comision",comision)


print("sueldo bruto",sbruto)

print("descuento",descuento)

print("sueldo neto",sneto) 
