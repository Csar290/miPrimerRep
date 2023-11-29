palabra = input("Dame una palabra: ")
eliminar = input("Que quieres eliminar: ")
subcadena = ""
find = palabra.find(eliminar)
subcadena = palabra[0 : find] + palabra[find + len(eliminar) + 1 : ]
print(f"la oracion con la eliminacion: {subcadena}")
