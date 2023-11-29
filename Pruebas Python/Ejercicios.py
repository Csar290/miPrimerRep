#Bank
saldo = int(input("Cuento saldo tiene en la cuenta: "))

if saldo > 10000:
    saldo = int(saldo * 0.04)
    print(f"Usted recibira: {saldo} de interes anualmente.")

else:
    saldo = int(saldo * 0.03)
    print(f"Usted recibira: {saldo} de interes anualmente.")

#Ecuacion
print("\n x = -b/a")
a = float(input("\nDame el valor de a: "))
b = float(input("Dame el valor de b: "))

if a != 0:
      x = b/a
      print(f"B entre a es: {x}")

if b == 0:
      print("a = 0 y b = 0")
      print("No hay solucion")

#Calificaciones

cal = int(input("\n¿Que calificacion tienes?: "))

if cal <= 20 and cal >= 16:
    print("Tu calificacion es A.")

elif cal < 16 and cal >= 11:
    print("Tu calificacion es B.")

else:
    print("Tu calificacion es reprobatoria.")











    

      
