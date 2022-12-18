#ejercicio 5


#convertimos los gb a mg,b,kb
capacidad_en_GB = float (input ('Insertar el valor de capacidad en GB: '))
#solucion


capacidad_en_MB=capacidad_en_GB*1024

capacidad_en_KB=capacidad_en_MB*1024
print ('Valor de capacidad en KB: ' + repr (capacidad_en_KB))
capacidad_en_B=capacidad_en_KB*1024
print ('Valor de capacidad en MB: ' + repr (capacidad_en_MB))
print ('Valor de capacidad en B: ' + repr (capacidad_en_B))