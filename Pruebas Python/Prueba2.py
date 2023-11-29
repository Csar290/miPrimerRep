print(" ")
print("                                                       ======================                    ")
print("                                                       SISTEMA DE OPERACIONES                    ")
print("                                                       ======================                    ")
print(" ")
print(" ")
print("Presiona 1 para sumar: ")
print("Presiona 2 para restar: ")
print("Presiona 3 para multiplicar: ")
print("Presiona 4 para dividir: ")
print(" ")
Operacion = int(input("¿Cual es tu opcion?: "))

if Operacion == 1:
    print("¡Genial!, Vamos a 'sumar'.")
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 + Valor2
    print("El resultado de tu suma es: ", Resultado)

elif Operacion == 2:
    print("¡Genial!, Vamos a 'restar'.")
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 - Valor2
    print("El resultado de tu resta es: ", Resultado)

elif Operacion == 3:
    print("¡Genial!, Vamos a 'multiplicar'.")
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 * Valor2
    print("El resultado de tu multipicacion es: ", Resultado)

elif Operacion == 4:
    print("¡Genial!, Vamos a 'dividir'.")
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 / Valor2
    print("El resultado de tu division es: ", Resultado)

else:
    print("Lo sentimos esa opcion no existe. Puede elegir entre las opciones 1, 2, 3 y 4.")


print(" ")
print(" ")
print("                                                        ===================                    ")
print("                                                        |       FIN       |                    ")
print("                                                        ===================                    ")
    

    
