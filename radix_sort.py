"""
202060712 - Dylan Yampuezan
202056995 -Juan Pablo Rodríguez García
dylan.yampuezan@correounivalle.edu.co
octubre 20 de 2022
"""

"""
Radix sort es un algoritmo de clasificación que clasifica los elementos agrupando
primero los dígitos individuales del mismo valor posicional. Luego, ordena los elementos 
según su orden creciente/decreciente.
"""
# clasificamos los dígitos en cada lugar significativo
def countingSort(arreglo, posicion):
    tamaño = len(arreglo) # tamaño del arreglo 0(1) en esta parte solo definimos las variables, por lo que solo se hara una vez, por lo tanto ese 0(1)
    salida = [0] * tamaño # multiplicamos por 0 todas las posiciones del arreglo 0(1)
    contador = [0] * 10 #0(1)

    # Calculamos el contador de elementos
    for i in range(0, tamaño):  #n+1
        indice = arreglo[i] // posicion #n
        contador[indice % 10] += 1 #n

    # Calcuamos el acumulador de elementos
    for i in range(1, 10): #0(1) como va de 1 a 10, las veces que se repite el for no va a variar, sera constante por lo tanto sera 0(1)
        contador[i] += contador[i - 1] #0(1)

    # Ubicamos los elementos en orden
    i = tamaño - 1 
    while i >= 0: 
        indice = arreglo[i] // posicion
        salida[contador[indice % 10] - 1] = arreglo[i]
        contador[indice % 10] -= 1
        i -= 1

    for i in range(0, tamaño):
        arreglo[i] = salida[i]


# Funcion principal
def radixSort(arreglo):
    # almacenamos el maximo elemento
    maximoElemento = max(arreglo)

    # Aplicamos  clasificación por conteo para clasificar elementos según el valor de posición.
    posicion = 1
    while maximoElemento // posicion > 0:
        countingSort(arreglo, posicion)
        posicion *= 10


# arreglo = [121, 432, 564, 23, 1, 45, 788]
# radixSort(arreglo)
# print(arreglo)