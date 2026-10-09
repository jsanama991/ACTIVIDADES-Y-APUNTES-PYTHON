'''
Escribe un programa que dada una
hora determinada (horas y minutos), calcule el
número de segundos que faltan para llegar a la
medianoche.

'''


hora= int(input("Dime la hora: "))
minutos= int(input("Dime los minutos: "))

print( "El numero de segundos que quedan para media noche es", (24*3600)-((hora*3600)+(minutos*60)))

