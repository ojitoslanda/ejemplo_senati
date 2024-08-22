#Lista (array) unidimensional - números enteros
listaNumeros = [1,2,3,4,5,6,7,8,9,10]
#creacion de variables
suma = 0
mayorNumero = listaNumeros[0]

#Bucle FOR - Para encontrar el mayor número
for varNumero in listaNumeros:
        suma += varNumero
        if varNumero > mayorNumero:
            mayorNumero = varNumero

print("El número mayor es: ", mayorNumero)
print("La suma de lista es:", suma)

