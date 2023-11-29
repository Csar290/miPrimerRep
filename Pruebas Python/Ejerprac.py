#Ejercicio 1:
Min = 2.5
Max = 7
Prom = 4
Curso_dalto = 1.5

diferencia1 = 100 - Curso_dalto / Min * 100
print(f"El curso de dalto dura {round(diferencia1)}% menos que el mas rapido.")

diferencia2 = 100 - Curso_dalto / Max * 100
print(f"El curso de dalto dura {round(diferencia2)}% menos que el mas lento.")

diferencia3 = 100 - Curso_dalto / Prom * 100
print(f"El curso de dalto dura {round(diferencia3)}% menos que el promedio.")

#Ejercicio 2:
texto = input("Dime cualquier cosa: ")
duracion = texto.split(" ")
cantidad = len(duracion)
print(f"Dijiste {cantidad} palabras, y tardaras {cantidad/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad/2*1.3} segundos.")
