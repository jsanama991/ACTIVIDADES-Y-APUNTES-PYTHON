Algoritmo mediainf
	
	Definir contador Como Entero
	contador<-0
	Definir n Como Entero
	n<-1
	Definir suma Como Entero
	suma<-0
	

	Mientras n<>0  Hacer
		si n>0 Entonces
			Escribir "Introduce un numero positivo (si quieres acabar pon 0): "
			leer n
			suma=suma+n
			contador= contador+ 1
		SiNo
			suma=suma
		finsi
	Fin Mientras
	Escribir "La media de los números es: ", suma/(contador-1)
	
	
FinAlgoritmo
