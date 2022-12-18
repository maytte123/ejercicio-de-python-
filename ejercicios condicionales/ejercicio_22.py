#Inicio

#unidadesA, unidadesB

unidadA=float(input("unidad A"))

unidadB=float(input("unidad B "))

   #  proveedor A


impcomA = unidadA*25.0

if( unidadA > 50 ):
       impdesA = 0.15*impcomA
else:
     impdesA = 0
     imppagA = impcomA - impdesA
 
   # proveedor B

impcomB = unidadB*27.5
if( unidadB > 35 ):
       impdesB = 0.10*impcomB

else:
    impdesB = 0
    imppagB = impcomB - impdesB

 #importes totales
impcomtot = impcomA + impcomB

impdestot = impdesA + impdesB

imppagtot = imppagA + imppagB



print("importe bruto",impcomtot) 

print("importe del descuento",impdestot)


print("importe total a pagar",imppagtot) 
#Fin