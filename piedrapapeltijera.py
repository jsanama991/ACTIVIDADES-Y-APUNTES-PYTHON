
a= input("La jugada del j1")
b= input("La jugada del j2")

	
	
if (a=="piedra" or a== "papel" or a=="tijera") and (b=="piedra" or b== "papel" or b=="tijera"): 
    
    if (a== "piedra" and b == "tijera") or (a== "papel" and b== "piedra") or (a== "tijera" and b== "papel"):
        print ("el j1 gana")			
                            
    elif (b== "piedra" and a == "tijera") or (b== "papel" and a== "piedra") or (b== "tijera" and a== "papel"):
        print ("el j2 gana")
                            
    else: 
        print ("empate")
        
		
	
else:
	print ("input no válido")
