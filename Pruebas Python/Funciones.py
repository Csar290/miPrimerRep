#Creando funciones:
#Funcion simple
def saludar():
    print("Hola cesar ¿Cómo estas?.")

#Print(imprimir en pantalla)
saludar()

print("----------------------------------")

#Funcion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "Mujer":
        adjetivo = "Sra"
    elif sexo == "Hombre":
        adjetivo = "Sr"
    
    print(f"Hola {adjetivo} {nombre} ¿Cómo estas?.")

#Print(imprimir en pantalla)
saludar("Camila", "Mujer")
saludar("Cesar", "Hombre")

print("----------------------------------")

#Funcion que retorna valores
def creando_contraseña(num):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 5
    c2 = num
    c3 = num - 1
    c4 = num - 3
    contraseña = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{caracteres[c4]}{num*2}"
    return contraseña, num

#Desempaquetando la funcion
password, primer_numero = creando_contraseña(777)

#Mostrando los resultados obtenidos y los datos utilizando para obtenerlo
print(f"Tu contraseña es: {password}")
print(f"El número utilizado para crearla fue {primer_numero}")
    
print("----------------------------------")

#Funcion no optima para sumar
def suma(lista):
    numero_sumados = 0

    for numero in lista:
        numero_sumados += numero
    return numero_sumados

resultado = suma([1,2,3,4,5,6,7,8,9,10])
print(resultado)

print("----------------------------------")

#Utilizando el operador * como argumento (args)
def sumar(nombre,*numeros):
    return f"{nombre} el resultado de tus suma es {sum(numeros)}"

resultado =  sumar("Csar",1,2,3,4)
print(resultado)
    
print("----------------------------------")

#Funciones con datos extras
def frase(nombre,apellido,adjetivo = "inteligente"): #Forma 3
    return f"Hola {nombre} {apellido} eres muy {adjetivo}"

frase_r = frase("Csar", "Suarez") #Forma 1
print(frase_r)
frase_r = frase(adjetivo = "bueno", nombre = "Csar", apellido = "Suarez") #Forma 2
print(frase_r)

print("----------------------------------")

#Funcion LAMBDA
#Funcion lambda para multiplicar
multiplicador = lambda x : x*5

print(multiplicador(2))

#Usando filter

numeros = [1,2,3,4,5,6,7,8,9,10]

#Creando una funcion comun que diga si es par o no
def es_par(num):
    if (num%2 == 0):
        return True

#Filter
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))
        
#Lo mismo pero con lambda e impares

numeros = [1,2,3,4,5,6,7,8,9,10]


numeros_impares = filter(lambda numeros: numeros%2 == 1, numeros)
print(list(numeros_impares))













