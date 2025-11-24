datos = input("Ingresa los datos en el siguente formato '€,Años,/%endecimal'")
datosLista = datos.split(",")
operacion = datosLista[0]*((1*datosLista[2])**datosLista[1])
print (operacion)