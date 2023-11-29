#Example 1:
#Pedir el nombre y la edad

#Def para obtener al profesor y su asistente
def obtener_alumnos(cantidad_compañeros):
    #Creando la lista para los alumnos
    alumnos = []

#Pedir datos de los alumnos
    for a in range(cantidad_compañeros):
        nombre = input("¿Cómo te llamas?: ")
        edad = int(input(f"{nombre} ¿Qué edad tienes?: "))
        alumno = (nombre, edad)
        #Agregando la imformacion a la lista
        alumnos.append(alumno)
    #Ordenando de menos a mayor
    alumnos.sort(key = lambda x:x[1])
    #Alumnos[x] devuelve una tupla  con nombre,edad
    #Definimos al profesor y asistente
    profesor = alumnos[-1][0]
    asistente = alumnos[0][0]
    #Retornamos una tupla
    return profesor,asistente

#Desempaquetamos lo que nos retorna la funcion
profesor,asistente = obtener_alumnos(5)
#Imprimir el resultado
print(f"El profesor es {profesor} y el asistente es {asistente}")

print("---------------------------------------------------")

#Example 2:

#Crear una funcion que verifique si un numero es primo
def es_primo(num):
    #Verificamos que el numero no pueda dividirse entre 2 hasta ese mismo numero
    for i in range(2,num -1):
        #Si es divisible por alguno retornamos False y termina el bucle
        if num % i == 0: return False
    #Si el bucle llega a su fin signidica que no fue divisible, entonces es primo
    return True

#Creando funcion que retorne una lista con todos los numeros primos
def primos_hasta(num):
    #Creamo lista
    primos = []
    for i in range(3,num +1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #Si es primo lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos
resultado = primos_hasta(50)
print(resultado)
    





























