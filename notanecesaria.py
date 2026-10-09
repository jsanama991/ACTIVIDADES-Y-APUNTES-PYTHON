test1= float(input("Introduce la nota del primer examen"))
want= float(input("Introduce la media que quieres tener"))

print(f"La nota del segundo examen para tener una media de {want}, debe ser ", (want-test1*0.4)/0.6)