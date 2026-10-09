'''
Escribe un programa que ordene 3
números enteros introducidos por teclado.
'''
a=int(input("introduce primer numero "))
b=int(input("introduce segundo numero "))
c=int(input("introduce tercer numero "))

if (a>b) and (b>c):		
		print (a,b,c)
    
elif (a>c) and (c>b):
        print (a,c,b)
            
elif (b>c) and (c>a): 
        print (b,c,a)
        
elif (b>a) and (a>c):
        print (b,a,c)
                    
elif (c>a) and (a>b):
        print (c,a,b)
                        
else:														
        print (c,b,a)