#Existe 2 manera de importar
import modulo_saludar as mSalud
#from modulo_saludar import saludar
import math
#from modulo_saludar import * # no es una buena practica
import modulo_fuera.calcular_edad as calEdad
# CREACIÓN DE LA VARIABLE
variable_saludar = mSalud.saludar("Juan")
variable_edad = calEdad.calcularEdad(1997,2024)

print(variable_saludar)
print(variable_edad)
print("El PI es: ", math.pi)


