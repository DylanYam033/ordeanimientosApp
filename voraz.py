"""
202060712 - Dylan Yampuezan
dylan.yampuezan@correounivalle.edu.co
octubre 20 de 2022
"""
"""
Este algoritmo se considera voraz, ya que toma como elemento menor el primero y puede que este sea el mejor elemento
o no para empezar a ordenar de una sola manera, la cual es comparando cada elemento con el supuesto "menor"
y de esta manera ir intercambiando lugares y dejando de ultimo al mayor de los elementos es por eso que se hace
con la longitud del arreglo menos 1, porque no sera necesario hacer el recorrido con el ultimo elemento, debido
a que ya estaran todos los anteriores ordenados y este estara en la ultima posicion por default.
"""

def OrdenamientoVoraz(arreglo):
    for i in range(len(arreglo) - 1): #n+1 
        menor = i # primer elemento por default será el mínimo para ordenar a partir de alli #n
        """
        con el bucle j recorremos los elementos hallando el verdadero menor y comparando entre si,
        una vez se encuentra se intercambia con la posicion i=0, que es la posicion de nuestro
        supuesto menor.
        """
        for j in range(i + 1, len(arreglo)): # se toma i a partir del elemento ordenado, pero no se toma porque ya esta ordenado 
            if arreglo[j] < arreglo[menor]: # comparamos si el elemento en posicion j es menor al primer elemento 
                menor = j # si lo es, pasa a ser el nuevo menor 

        if menor != i: #n
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor] #peor caso: n mejor caso:0 

"""
Ya estando ordenado el primero elemento, arranca de nuevo el ciclo pero con i=1, porque ya i=0 fue ubicado y asi 
hasta ordenar la ultima posicion.
"""

# a = [22, 25, 12, 64, 11]
# OrdenamientoVoraz(a)

# print(a)