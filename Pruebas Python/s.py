#Suma de los primeros enteros

suma = 0
s = 1

a = int(input("¿Hasta que entero deseas sumar?: "))

while s <= a:
    suma += s
    s += 1
    print(suma)
