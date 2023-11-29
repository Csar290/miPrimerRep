diccionario = {"nombre": "Cesar",
               "apellido": "Suarez",
               "edad": 18
               }

#Devuelve las claves
claves = diccionario.keys()
print(claves)

#Devuelve el valor de una clave
clave = diccionario.get("nombre")
print(clave)

#Obtiene un elemento iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#Eliminando un elemento del diccionario
diccionario.pop("apellido")
print(diccionario)

#Elimina todo del diccionario
diccionario.clear()
print(diccionario)
