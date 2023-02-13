"""
202060712 - Dylan Yampuezan
dylan.yampuezan@correounivalle.edu.co
octubre 20 de 2022
"""

"""
Utilizando la técnica Divide y venceras , dividimos un problema en subproblemas. 
Cuando la solución a cada subproblema está lista, 'combinamos' 
los resultados de los subproblemas para resolver el problema principal.
"""
def OrdenamientoDinamico(arreglo):
    if len(arreglo) > 1: # verificamos que el arreglo tengas mas de un elemento

        # dividimos la longitud del arreglo 
        division = len(arreglo)//2
        arreglo1 = arreglo[:division] # tomamos la primera parte del arreglo
        arreglo2 = arreglo[division:] # tomamos la segunda parte del arreglo

        # ordenamos las dos mitades
        OrdenamientoDinamico(arreglo1)
        OrdenamientoDinamico(arreglo2)

        i = j = k = 0 # inicializamos contadores para hacer los recorridos

        # ordenamos los elementos hasta llegar a cualquiera de los dos extremos de los arreglos
        while i < len(arreglo1) and j < len(arreglo2):
            if arreglo1[i] < arreglo2[j]:
                arreglo[k] = arreglo1[i]
                i += 1
            else:
                arreglo[k] = arreglo2[j]
                j += 1
            k += 1

        # cuando los elementos ya han sido ordenados, se toman los restantes para ambos arreglos
        while i < len(arreglo1):
            arreglo[k] = arreglo1[i]
            i += 1
            k += 1

        while j < len(arreglo2):
            arreglo[k] = arreglo2[j]
            j += 1
            k += 1

# arreglo = [6, 5, 12, 10, 9, 1]
# OrdenamientoDinamico(arreglo)
# print("Sorted arreglo is: ")
# print(arreglo)