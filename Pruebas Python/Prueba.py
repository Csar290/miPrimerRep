Nombre = input("¿Cual es tu nombre?: ")

print("Muy bien " + Nombre + ", ahora dime.")

Año = int(input("¿En que año estamos: "))
Año_de_Nacimiento = int(input("Ok. ¿Y en que año naciste?: "))
Mes_de_Nacimiento = int(input("¿Del mes numero?: "))

Resultado = Año - Año_de_Nacimiento

if Mes_de_Nacimiento > 12:
    print("Solo son 12 meses.")

if Mes_de_Nacimiento > 2 and Mes_de_Nacimiento < 13:
    print("Genial " + Nombre + " tu tienes " + str(Resultado -1) + " años.")

if Mes_de_Nacimiento == 1 or Mes_de_Nacimiento == 2:
    print("Entonces tu cumpliras o ya cumpliste " + str(Resultado) + " años.")









    
    
    

