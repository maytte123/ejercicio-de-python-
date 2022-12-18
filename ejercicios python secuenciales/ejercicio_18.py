import os
os.system("cls")
#inicio


cantidad_de_propruductos=float(input(" unidades adqueridas"))

precio_unitario=float(input("r el precio del articulo"))

importe_compra=precio_unitario*cantidad_de_propruductos

primer_descuento=importe_compra*0.15
print ('el importe de la compra: ',importe_compra,"S/")
segundo_descuento=(importe_compra-primer_descuento)+0.15
print ('el importe del primer descuento : ',primer_descuento,"S/")
importe_a_pagar= importe_compra-primer_descuento -segundo_descuento

print ('el importe del primer segundo descuento : ',segundo_descuento,"S/")
print ('el importe a pagar  : ',importe_a_pagar,"S/")