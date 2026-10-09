'''
Escribe un programa que calcule el
precio de un desayuno. Primero pregunta al usuario
que ha tomado para comer: tostada, churros o donuts.
Los churros valen 1,50€ y el donut 1€. En caso de
tomar tostada, debe preguntar si es básica (1,20€) o
especial (1,60€). Por último preguntará la bebida,
zumo o café, a 1,80€ y 1,20€ respectivamente.
'''

desa=input("Que has desayunado: churros, donut o tostada? ")
total=0

if desa=="churros":
    total=1.5
elif desa=="donut":
    total=1
else:
    print("La tostada es especial (e) o básica (b)? ")
    tipot=input("e o b? ")
    if tipot== "e":
        total=1.2
    else:
        total=1.6

bebida= input("Que has bebido: zumo o café ")

if bebida=="zumo":
    total=total+1.8
else:
    total=total+1.2

print(f"El precio total de tu desayuno es {total}")

