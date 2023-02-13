"""
202060712 - Dylan Yampuezan
dylan.yampuezan@correounivalle.edu.co
octubre 20 de 2022
"""
import time, voraz
import random
lista = []
listaMaquina = []
turno = ""

def jugador():
    turno = 0
    tamaño = 10  # cantidad de numeros de la lista
    i = 1  # iterador
    numerorandom = random.randint(1, 30)
    time.sleep(1)
    print("BIENVENIDO AL NIVEL 4 DE TOWER BLASTER")
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
        maquina()
    else:
        print("La lista de la maquina esta llena")
        time.sleep(1) 
        print("Ingresa todos los numeros a tu lista")
        if len(lista) < 10:
            jugador() #llamamos la funcion hasta que el jugador ingrese todos los numeros
        else:
            print("Se han llenado las dos listas")

def maquina():
    turno = 1
    tamaño = 10  # cantidad de numeros de la lista
    i = 1  # iterador
    numerorandom = random.randint(1, 30)
    print("MAQUINA JUGANDO")
    print("--------------------------------")
    print("El numero generado fue:")
    print(numerorandom)
    while i <= tamaño and turno == 1 :
        listaMaquina.append(numerorandom)
        time.sleep(1) 
        print("Lista maquina")
        print(listaMaquina)
        i = i+1
        turno = 0
    # print(listaMaquina)
    if len(lista) < 10: #verificamos si la lista del usuario esta vacia
        jugador()

def resultados():
    arreglo = listaMaquina
    print("Lista maquina sin ordenar: ")
    print(arreglo)
    print("//////////////////////////////////")
    voraz.OrdenamientoVoraz(arreglo)
    tiempoMaquina = time.time()
    print("Lista maquina ordenada: ")
    print(arreglo)

    print("------------------------------------")
    print("------------------------------------")

    arreglo = lista
    print("Lista usuario sin ordenar: ")
    print(arreglo)
    print("//////////////////////////////////")
    voraz.OrdenamientoVoraz(arreglo)
    tiempoJugador = time.time()
    print("Lista usuario ordenada: ")
    print(arreglo)

    if tiempoMaquina < tiempoJugador:
        print("//////////////////////////////////")
        print("GANA MAQUINA")
    else:
        print("//////////////////////////////////")
        print("GANASTE")