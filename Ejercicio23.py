# Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

lab = [[1, 1, 1, 0, 1],
       [1, 0, 1, 1, 1],
       [1, 1, 0, 0, 1],
       [0, 1, 1, 0, 1],
       [0, 0, 1, 1, 2]]

def laberinto (matriz,x,y,caminos = []):
    if ( x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if (matriz [x][y] == 2):
            caminos.append([x, y]) 
            print ('Saliste del laberinto')
            print (caminos) 
            caminos.pop() #Elimina y retorna el ultimo elemento de la lista
        else:
            if (matriz [x][y] == 1):
                matriz[x][y] = 3 
                caminos.append([x, y]) 
                laberinto(matriz, x, y+1, caminos) #mover derecha
                laberinto(matriz, x, y-1, caminos) #mover izquierda
                laberinto(matriz, x-1, y, caminos) #mover arriba
                laberinto(matriz, x+1, y, caminos) #mover abajo
                caminos.pop()
                matriz[x][y] = 1
                
laberinto(lab,0,0)