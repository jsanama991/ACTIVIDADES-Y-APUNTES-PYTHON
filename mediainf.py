'''
Escribe un programa que calcule
la media de una serie de números positivos. El
usuario indicará que ha terminado de introducir datos
cuando introduzca un número negativo.
'''
contador=0
n=1
suma=0
while n != 0:
    n=float(input("Introduce un numero positivo (si quieres acabar pon '0'): "))
    if n>0:
        suma=suma+n
        contador+= 1
        
    else:
        continue

print("La media de los números es: ", suma/contador)


