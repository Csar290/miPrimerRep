#Importamos un modulo y le asignamos un nombre
#import modulo_saludar as m_saludar

#1.-Desde ese modulo importamos funciones
#2.-Creamos las variables
#3.-Mostramos los resultados

#1
#import modulo_saludar as m_saludar
#2
#saludo = m_saludar.saludar("Cesar")
#3
#print(saludo)

#1
#import modulo_saludar 
#2
#saludo = modulo_saludar.saludar("Cesar")
#3
#print(saludo)

#1   #Llamar cuando el modulo esta en una carpeta en este caso Pruebas
from Pruebas.modulo_saludar import saludar
#2
saludo = saludar("Cesar")
#3
print(saludo)

#1
from Pruebas.modulo_saludar import saludar, saludare
#2
saludo = saludar("Cesar")
saludo1 = saludare("Adriano")
#3
print(saludo)
print(saludo1)

#1 #Importar todo #Forma no recomendable(muy pesado)
from Pruebas.modulo_saludar import *
#2
saludo = saludar("Cesar")
saludo1 = saludare("Adriano")
#3
print(saludo)
print(saludo1)


