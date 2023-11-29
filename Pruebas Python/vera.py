t = 0
for i in [5, 4, 3, 2, 1]:
    t = t +1
    print(t)

lo = -1
for numero in [9, 12, 3, 9, 17, 23]:
    if numero > lo:
        lo = numero
print(lo)

n = 0
while n > 0:
    print(n)
    n += 1

print("Terminado")

#1
for num in range(0, 20, 2):
    print(num)

n = 0
while n == 0 or n > 0:
    print(n)
    n += 2
    if n > 18:
        break

#2

a = int(input("Dame un valor: "))
b = int(input("Dame otro valor: "))
res = 0

if b < a:
    print(f"{b} es menor que {a}.")

elif b > a:
    for suma in range(a, b):
        res += suma
        print(res)



