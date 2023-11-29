numeros = [4, 7, 20, 46, 6]
print(numeros)

numero_mas_bajo = min(numeros)
print(f"El numero mas bajo es {numero_mas_bajo}")

numero_mas_alto = max(numeros)
print(f"El numero mas alto es: {numero_mas_alto}")

print("---------------------------")
#Booleano(Bool)
#Retorna False si es :0, vacio, None
#Retorna True si es :distinto a 0 , string, dato no vacio

#False
reslt_bool = bool(0)
print(reslt_bool)
reslt_bool = bool()
print(reslt_bool)
reslt_bool = bool([])
print(reslt_bool)

#True
reslt_bool = bool(5)
print(reslt_bool)
reslt_bool = bool("hola")
print(reslt_bool)
reslt_bool = bool([1,2,3])
print(reslt_bool)

print("---------------------------")
#All
#Retorna True si todos los valores son verdadero(similar al True de bool)

Resultado_all = all([(123, True),[5,4,3]])
print(Resultado_all)
Resultado_all = all([])
print(Resultado_all)

#Retorna False si es 0, vacio, None

Resultado_all = all([0, True,[5,4,3]])
print(Resultado_all)
Resultado_all = all([False, True,[5,4,3]])
print(Resultado_all)
Resultado_all = all([None, True,[5,4,3]])
print(Resultado_all)

print("---------------------------")
#Suma de los valores de un iterable
n = [1,2,3,4]
suma = sum(n)
print(suma)









