contador= 0
CONTRASENA = 7894
while contador<5:
    
    intento= int(input(f'Introduce tu {contador} º para desbloquear la caja fuerte, te quedan {(4-contador)} intentos '))
    
    if (intento==CONTRASENA):
        print ('La caja fuerte se ha abierto')
        contador = 6
    else:
        print('La caja fuerte sigue cerrada') 
        contador = contador+1
