#Saber nombre e IP del ordenador:

import socket

hostname = socket.gethostname()#Nombre del ordenador
ip = socket.gethostbyname (hostname)#IP del ordenador
print("El nombre de tu ordenador es: " + hostname)
print("Tu dirección IP es: " + ip)


#Pasar de decimal a binario:

def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
       binario = str(decimal % 2) + binario
       decimal = decimal // 2
    return str (decimal) + binario

numero = int(input("Introduce el número que quieres convertir a binario: "))
print(binario(numero))


#Crackeador de contraseñas:


import hashlib

encontrada = 0
input_hash = input("Inserte la contraseña hasheada: ")
pass_doc = input("Inserte el diccionario: ")

try:
    pass_file = open(pass_doc, 'r')
except:
    print("Error: " + pass_doc + " no ha sido encontrada.")

for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()

    if digest == input_hash:
        print("¡Contraseña encontrada!")
        print("La contraseña es: " + palabra)
        encontrada = 1
        break
if not encontrada:
    print("Contraseña no encontrada en el archivo " + pass_doc)


#Escaner de puertos:
import sys
import socket
objetivo = socket.gethostbyname(input("Inserte la dirección IP: "))
print("Escaneando objetivo: " + objetivo)
try:
    for port in range(1,150):
         s = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         resultado = s.connect_ex((objetivo, port))
         if resultado == 0:
            print("El puerto {} está abierto".format(port))
         s.close()
except:
    print("\nSaliendo...")
    sys.exit(0)
















