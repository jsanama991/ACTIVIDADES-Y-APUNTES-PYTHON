x=10

def function(x):
    x=5 # este x es una copia del de fuera
    a= 4
    return a

f=function(x)

print(f)# por eso aquí no cambia