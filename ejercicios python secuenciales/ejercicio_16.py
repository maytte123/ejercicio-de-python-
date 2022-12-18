#Inicio

   #variables de las horas de trabajo


horasTrab=float(input(" horas de trabajo "))


tarifaHor=float(input(" tarifa de horas "))


   # Proceso de cálculo


sueldoBas = horasTrab*tarifaHor
print("sueldo basico ",sueldoBas)
montoBoni = 0.20*sueldoBas

sueldoBru = sueldoBas+montoBoni
print("sueldo bruto ",sueldoBru)

montoDesc = 0.10*sueldoBru

sueldoNet = sueldoBru-montoDesc

print("sueldo neto" ,sueldoNet)
