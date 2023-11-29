#BUCLE FOR
animales = ["Perro", "Gato", "Conejo", "Sapo"]
numeros = [10, 20, 30, 40]

#Recorriendo la lista animales
for animal in animales:
    print(animal)

print("------------------------------------------")

#Recorriendo dos lisas del mismo tamaño
for animal,numero in zip(animales,numeros):
    print(f"Lista 1: {animal}")
    print(f"Lista 2: {numero}")

print("------------------------------------------")

#Forma no optima de recorrer una lista. No funca en conjuntos
for num in range(len(numeros)):
    print(numeros[num])

print("------------------------------------------")

#Forma correcta de recorrer una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

print("------------------------------------------")
for num in enumerate(numeros):
    print(num)

else:
    print("El bucle finalizó")

print("------------------------------------------")

#Recorrer diccionario para obtener clave
diccionario = {"Nombre": "Cesar",
               "Apellido": "Suarez",
               "Edad": 18
               }

for datos in diccionario:
    key = datos
    print(f"La clave es: {key} ")

print("------------------------------------------")

#Recorrer diccionario con items() para obtener clave y valor
diccionario = {"Nombre": "Cesar",
               "Apellido": "Suarez",
               "Edad": 18
               }

for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"La clave es: {key} y el valor es: {valor}")

print("-----------------------------------------")

#Continue en bucle for

frutas = ["Platano", "Manzana", "Pera", "Naranja", "Mandarina"]

for fruta in frutas:
    if fruta == "Pera":
        continue
    print(f"Quiero comer {fruta}")

print("------------------------------------------")

#Break en el bucle for

frutas = ["Platano", "Manzana", "Pera", "Naranja", "Mandarina"]

for fruta in frutas:
    print(f"Quiero comer {fruta}")
    if fruta == "Naranja":
        break
print(f"Si sigues comiendo te puede hacer mal")

print("------------------------------------------")

#For en una sola linea de codigo
numeros = [2,4,6,8]
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

print()
print("============================================")
print()

#BUCLE WHILE

contador = 0

while contador < 11:
    print(contador)
    contador += 1
















