deco = "========================"
titulo = "Fiesta de cumpleaños"
racion = "========================"

print(deco.center(132))
print(titulo.center(132))
print(racion.center(132))

lista_de_invitados = []
lista_de_invitados.insert(0, "Carlos")
lista_de_invitados.insert(1, "Adriano")
lista_de_invitados.insert(2, "Cesar")
lista_de_invitados.insert(3, "Karen")
lista_de_invitados.insert(4, "Karol")
lista_de_invitados.insert(5, "Kevin")
lista_de_invitados.insert(6, "Martha")
lista_de_invitados.insert(7, "Milagros")

print("Hola, para ingresar a la fiesta tenemos una lista de invitados.")
nombre = input("Me permite su nombre por favor: ")
nombre = nombre.capitalize()

numeros = lista_de_invitados.index(nombre)

if numeros == 0:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 1:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 2:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 3:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 4:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 5:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 6:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

if numeros == 7:
    print(f"\nBienvenido {nombre}, usted está en la lista. Disfrute de la fiesta.")

