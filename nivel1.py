"""
202060712 - Dylan Yampuezan  
dylan.yampuezan@correounivalle.edu.co
octubre 20 de 2022
"""
import time, quick_sort #importamos quicksort para ser usado en la funcion resultados
import random
lista = []
listaMaquina = []
turno = ""
"""
La funcion jugador() tiene la logica de juego del usuario, en esta se generan los numeros y se pregunta al usuario
si desea agregarlos o no, ademas de esto se van agregando los numeros elegidos a la lista del jugador y tambien
hacemos las respectivas validaciones, tales como si la lista ya se lleno o no y en caso de no estarlo, ejecutar
la funcion respectiva, en caso de que la lista sin llenar sea del jugador o la maquina
"""
def jugador():
    turno = 0 #inicializamos la variable turno para alternar el juego entre la maquina y el usuario
    tamaño = 10  # cantidad de numeros de la lista
    i = 1  # iterador
    numerorandom = random.randint(1, 50)
    time.sleep(1)
    print("BIENVENIDO AL NIVEL 1 DE TOWER BLAST")
    print("-------------------------------------")
    time.sleep(1)
    print("El numero generado fue:")
    print(numerorandom)
    decision = input("¿Desea agregar este numero? ")
    while decision == "si" and i <= tamaño and turno == 0:
        lista.append(numerorandom)
        print("Lista usuario")
        print(lista)
        turno = 1
        i = i+1
    
    if len(listaMaquina) < 10: # verificamos si la lista de la maquina esta vacia
        maquina() # si esta vacia ejecutamos maquina() 
    else:
        print("La lista de la maquina esta llena...")
        time.sleep(1) 
        print("Ingresa todos los numeros a tu lista")
        if len(lista) < 10: # verificamos si la lista del jugador esta vacia o si le faltan numeros por agregar
            jugador() #llamamos la funcion hasta que el jugador ingrese todos los numeros
        else:
            time.sleep(1) 
            print("Se han llenado las dos listas")
"""
La funcion maquina(), tiene la logica de juego de la maquina, en esta implementamos la misma logica del jugador()
con la diferencia de que la maquina escoge sus numeros.
"""
def maquina():
    turno = 1
    tamaño = 10  # cantidad de numeros de la lista
    i = 1  # iterador
    numerorandom = random.randint(1, 50)
    print("MAQUINA JUGANDO")
    time.sleep(1)
    print("--------------------------------")
    print("El numero generado fue:")
    print(numerorandom)
    while i <= tamaño and turno == 1 :
        listaMaquina.append(numerorandom)
        time.sleep(1)  # espera 1 segundos entre cada print()
        print("Lista maquina")
        print(listaMaquina)
        i = i+1
        turno = 0
    if len(lista) < 10: #verificamos si la lista del usuario esta vacia
        jugador()
"""
La funcion resultados(), nos muestra ambas listas, la del jugador y la maquina, luego usamos la funcion quicksort
ubicada en nuestro archivo, previamente importado y esta funcion recibe como parametro las dos listas para ser 
ordenadas, posterior a esto usamos una funcion de python para calcular el tiempo que tardo ejecutando la funcion
con cada lista, ya con ambos tiempos de ejecucion almacenados, evaluamos cual tuvo el menor tiempo y en base a esto
elegimos el ganador.
"""
def resultados():
    arreglo = listaMaquina
    print("Lista maquina sin ordenar: ")
    print(arreglo)
    print("//////////////////////////////////")
    quick_sort.quicksort(arreglo, 0, len(arreglo) - 1) #le pasamos a nuestra funcion la lista de la maquina para partirla
    tiempoMaquina = time.time()                        #y posterior a esto hacer el ordenamiento tomando un pivote
    print("Lista maquina ordenada: ")
    print(arreglo)

    print("------------------------------------")
    print("------------------------------------")

    arreglo = lista
    print("Lista usuario sin ordenar: ")
    print(arreglo)
    print("//////////////////////////////////")
    quick_sort.quicksort(arreglo, 0, len(arreglo) - 1)
    tiempoJugador = time.time() #capturamos el tiempo que se demora en ordenar la lista del jugador
    print("Lista usuario ordenada: ")
    print(arreglo)

    if tiempoMaquina < tiempoJugador:
        print("//////////////////////////////////")
        print("GANA MAQUINA")
    else:
        print("//////////////////////////////////")
        print("GANASTE")
        

    