dato = float(input("Dame un valor: "))

if dato == int(dato):
    print("El número es entero.")

elif dato == float(dato):
    print(round(dato // 1))

print("------------------------------------------")

dato = float(input("Dame un valor: "))

if dato == int(dato):
    print("El número es entero.")

else:
    print("El numero no es entero.")


print("------------------------------------------")

dulce = 2
print("El dulce cuesta 2 Dolares.")
money = int(input("¿Cuánto dinero tiene?: "))

if money > dulce:
    c = money - dulce
    print(f"Ahí tiene su dulce.\nSu vuelto es {c}")

if money < dulce:
    print("No le alcanza.")
