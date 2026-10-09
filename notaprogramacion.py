'''
Escribe un programa que pide
las notas de dos exámenes de programación. Si la
media es mayor o igual a 5, el alumno estará
aprobado y se mostrará la media. Si no, Se
preguntará al usuario ¿Cuál ha sido el resultado de la
recuperación? (apto/no apto). Si el resultado es apto,
la nota será 5, en caso contrario se mantendrá la
media anterior.
'''
	
nota1= float(input("Introduce la primera nota"))
nota2= float(input("Introduce la primera nota"))	
	
	
media = (nota1+nota2)/2
	
if (media >= 5):    
    print( "Tu media es: ", media)
    
else:			
    recu= input("Cual fue tu nota del examen de recuperacion")
    if (recu == "apto"):        
        print( "Tu nota es 5")

    else:
        print( "Tu media es", media)   

			
		
		
