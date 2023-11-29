#DESEMPAQUETADO
#Tupla
datos = ["Cesar", "Suarez", 18]
#Lista
datos = ("Cesar", "Suarez", 18)
#Desempaqueamiento
nombre, apellido, edad = datos
#Resultado 
print(nombre)
print(apellido)
print(edad)
print()

print("-----------------------\n")

#TUPLAS
#Creando tuplas con Tuple()
tupla = tuple([1, 3, 2004])
print(tupla)
#Creando tupla sin parentesis de multiples datos
tupla = 1, 3, 2004
print(tupla)
#Creando tupla sin parentesis de un dato
tupla = 1,
print(tupla)
print(type(tupla))
print()

print("-----------------------\n")

#CONJUNTOS
#Creando conjutnso con set()
conjunto = set(["Cesar", "Manuel"])
print(conjunto)
#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Cesar", "Manuel"])
conjunto2 = {conjunto1, "Suarez"}
print(conjunto2)
print()

#TEORIA DE CONJUNTOS
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
print("Subconjunto")
print(f"{conjunto2} es subconjunto de {conjunto1}:")
resultado = conjunto2.issubset(conjunto1)
print(f"{resultado}\n")
print(f"{conjunto1} es subconjunto de {conjunto2}:")
resultado = conjunto1.issubset(conjunto2)
print(f"{resultado}\n")

print("Superconjunto")
print(f"{conjunto2} es superconjunto de {conjunto1}:")
resultado = conjunto2.issuperset(conjunto1)
print(f"{resultado}\n")
print(f"{conjunto1} es superconjunto de {conjunto2}:")
resultado = conjunto1.issuperset(conjunto2)
print(f"{resultado}\n")

print("Subconjuntos con >=")
print(f"{conjunto2} es subconjunto de {conjunto1}:")
resultado = conjunto2 >= (conjunto1)
print(f"{resultado}\n")
print(f"{conjunto1} es subconjunto de {conjunto2}:")
resultado = conjunto1 >= (conjunto2)
print(f"{resultado}\n")

print("Superconjunto con <=")
print(f"{conjunto2} es superconjunto de {conjunto1}:")
resultado = conjunto2 <= (conjunto1)
print(f"{resultado}\n")
print(f"{conjunto1} es superconjunto de {conjunto2}:")
resultado = conjunto1 <= (conjunto2)
print(f"{resultado}\n")

#Verificar si no hay algun numero en comun
print(f"{conjunto1} tiene algo en comun con {conjunto2}:")
resultado = conjunto1.isdisjoint(conjunto2)
print(f"{resultado}\n")

#DICCIONARIOS
#Creando diccionarios
diccionario = dict(nombre = "Cesitar",
                    apellido = "Suarez",
                    edad = 18
                    )

print(f"{diccionario}\n")

#NO SE PUEDE CREAR NADA VACIO SIN METODOS COMO DICT(), TUPLE(), ETC

#Las tuplas pueden ser claves

diccionario = {("Cesar", "Suarez"): "Nombre completo"}
print(f"{diccionario}\n")

#Mientras que las lista no, a menos que usemos frozenset() 

diccionario = {frozenset(["Cesar", "Suarez"]): "Nombre completo"}
print(f"{diccionario}\n")

#Creando diccionarios con fromkeys
diccionario = dict.fromkeys("abcd", "Cesar")
print(f"{diccionario}\n")
#Valor por defecto none
diccionario = dict.fromkeys(["abcd", "Cesar"])
print(f"{diccionario}\n")
#Cambiando valor por defecto none por "No se"
diccionario = dict.fromkeys(["abcd", "Cesar"], "No se")
print(f"{diccionario}\n")












































