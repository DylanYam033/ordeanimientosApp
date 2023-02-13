# 1. Menu de usuario preguntando que nivel quiere jugar LISTO
# 2. Por cada nivel implementar un rango de numeros al azar diferentes LISTO
# 3. Preguntar al usuario que numeros desea almacenar en una lista de los numeros generados al azar LISTO
# 4. Si el numero escogido es sucesor del que ya esta almacenado suma puntos PENDIENTE...
# 5. Una vez esten escogidos los numeros de la lista se la pasamos al algoritmo quicksort LISTO
# 6. COMENTARIO_CABECERA
# 7. PRUEBA DE ESCRITORIO
# 8. DIAGRAMA DE CLASES
# 9. DOCUMENTO ESCRITO
# 10. ANALIZAR LOS ALGORITMOS Y COMENTARLOS LISTO

"""
202060712 - Dylan Yampuezan
dylan.yampuezan@correounivalle.edu.co 
octubre 20 de 2022
"""
import nivel1, nivel2, nivel3, nivel4

def bienvenida(name):
    name = input("INGRESE SU NOMBRE DE JUGADOR PARA EMPEZAR: ")
    assert len(name) > 0, "Error" #Afirmo que el input no va a estar vacio
    print("---------------------------------------------------------------")
    print("BIENVENIDO "+name.upper()+" A TOWER BLASTER") 

def menu():
    menu = """
    SELECCIONE UN NIVEL PARA EMPEZAR:
        1. Nivel 1
        2. Nivel 2
        3. Nivel 3
        4. Nivel 4 
        5. Para salir del juego

    INGRESA EL NIVEL QUE QUIERAS JUGAR  
    """
    opcion = str(input(menu))
    if opcion == "1":
        nivel1.jugador() #Ejecutamos el nivel 1
        nivel1.resultados() #ejecutamos la funcion resultados

    elif opcion == "2":
      nivel2.jugador()
      nivel2.resultados()

    elif opcion == "3":
        nivel3.jugador()
        nivel3.resultados()

    elif opcion == "4":
        nivel4.jugador()
        nivel4.resultados()
    elif opcion == "5":
        print("Gracias por jugar")
    else:
        print('Seleccione una opcion valida')

#Se llaman las funciones a usar
if __name__ == '__main__':
    bienvenida("")
    menu()