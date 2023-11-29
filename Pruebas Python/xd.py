titulo = "Ejercicio aplicando lo aprendido"
d = "======================================"
print(titulo.center(130))
print(d.center(130))
print("Este titulo tiene ", len(titulo), " caracteres.")
print("Este es el titulo: {}".format(titulo))

nombre = input("\n¿Cual es tu nombre?: ")
print(f"Genial {nombre} esto es solo el comienzo.\n")

print("¿Te parece bien si probamos eliminar algunos caracteres finales de tu nombre?")
so = input("Si o NO: ").lower()

if so == "si":
    eliminar = input("Escribe las letras que quieres eliminar: ")
    nombre = nombre.rstrip(f"{eliminar}")
    print(f"\nTu nombre con los caracteres eliminados: {nombre}\n")
    print("Si no se borro debe ser porque te pedí eliminar caracteres final, pero, ¿Es raro no?, ¿Porque acabamos de hacer esto?. Bueno sigamos.\n")
    
elif so == "no":
    print("¿Que estupido no?, ¿Quien quisiera eliminar alguna letra de su nombre?\n")

apellido_p = input("Oye y, ¿Cual es tu apellido paterno?: ")
apellido_m = input("¿Y materno?: ")
apellidos = (f"{apellido_p} {apellido_m}")

print(f"\n{apellidos.title()} me gusta. Te llamare así, {apellido_p.title()}.")

print("\nEsto solo sera una prueba.")
c_l_r = input("\n¿Te gustaria ver tus apellidos al centro, izquierda o derecha?: ").lower()

if c_l_r == "centro":
    print(f"{apellidos.center(130).upper()}")

elif c_l_r == "izquierda":
    print(f"{apellidos.ljust(1).upper()}")

elif c_l_r == "derecha":
    print(f"{apellidos.rjust(255).upper()}")

print("\nUn poquito de relleno nunca viene mal.")
print("De todas formas, si te sientes mal por haber perdido el tiempo con esto, recuerda que el que me creo demoró como un dia en crearme. Asi que parece que hay alguien que pierde más tiempo que tu.")

mama = "mi mama me mima"
con = 0
con = mama.count("m")
print(f"\nPor cierto sabias que la palabra 'mi mama me mima' tiene {con} m's.")
print("Mas relleno para que el creador no se sienta como un perdedor.(Lo es).")
print("\nPor otro lado si algún día necesitas recordar como empieza un acrostico con tus hermosos apellidos aqui te lo dejo.")

for acrostico in apellidos.capitalize():
    print(acrostico)

print("Ahora te toca poner el relleno a ti. ¿No quieres que lo haga todo no?.\n")

print("Mira acabo de aprender a contar.")
print("Voy a contar hasta 10:")
contador = 0
for contador in range(11):
    contador += 1
    if contador == 11:
        break
    print(f"N°: {contador}")

print("\nTambien podemos ver que hay dentro de una lista.")
print("Por ejemplo tengo una lista con el abecedario:")
abcdario = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(abcdario)
print(f"El abecedario tiene: {len(abcdario)} elementos.")
ver = int(input("\n¿Que letra del abecedario deseas ver?(Teniendo en cuenta que se empieza de 0): "))
print(f"La letra de la posicion {ver} es: {abcdario[ver]}")
print("\nSi quieres podemos hacer el abecedario un poco inclusivo colocando la 'ñ' para los hispanos. Pero que no se den cuenta los ingleses porque se molestan.(BUUU)")
abcdario[13] = "ñ"
print(abcdario)
print("Ahora el abecedario tiene: {len(abcdario)} elementos.")
print('La "ch" ya no lo agregamos. Vamos, ¿hay alguien que todavia cree que esa podria ser otra letra del abecedario?.Por Dios')
print("A pesar de ser una maquina me molesta muchisimo. Pido perdon")
print('Me estoy ganando muchos enemigos. El estupido que me creo, los ingleses y ahora la gente que cree que la "ch" es una letra')

print("\nOh no, ahi viene ese tarado que me creo. Me tengo que ir adios, este...")
new_name = input("Me recuerdas tu nombre: ")
print(f"Nos vemos pronto {new_name}.")













