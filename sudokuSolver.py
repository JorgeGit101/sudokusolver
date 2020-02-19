from numpy import *
from time import sleep


# grilla de sudoku
f1 = array([8,1,7,0,0,0,0,4,5])
f2 = array([0,0,0,0,5,1,7,0,6])
f3 = array([2,6,5,0,0,3,0,0,1])
f4 = array([4,7,0,5,6,8,0,0,0])
f5 = array([9,5,1,0,0,0,0,8,0])
f6 = array([0,3,0,0,9,0,2,0,0])
f7 = array([0,4,0,2,0,0,0,0,0])
f8 = array([0,0,0,0,0,5,0,7,9])
f9 = array([5,8,9,7,3,0,1,6,0])

# creando la matriz
matriz = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
matriz = matrix(matriz)

print(matriz)
print('\n\n')
delay = input('Presiona Enter para resolver')
print('Procesando...\n\n')
sleep(1.5)

def vacio(i,j):
    if matriz[i,j] != 0:
        v = False
    else:
        v = True
    return v


def posibles(i, j):
    # empieza a analizar solo si la casilla está vacía
    numeros = False
    if vacio(i, j) is True:
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        columna = []
        listado = matriz[i].tolist()
        selecto = listado[0]
        # posibles en renglon
        for numero in range(1, 10):
            if numero in selecto:
                numeros.remove(numero)
        # posibles en columna
        for valor in range(9):
            if matriz[valor, j] != 0:
                columna.append(matriz[valor, j])
        for numero in numeros:
            if numero in columna:
                numeros.remove(numero)
        # posibles en cuadrado
        y0 = (i // 3) * 3
        x0 = (j // 3) * 3
        for x in range(0, 3):
            for y in range(0, 3):
                if matriz[y0 + x, x0 + y] in numeros:
                    numero = matriz[y0 + x, x0 + y]
                    numeros.remove(numero)
    return numeros


def rellenado(i,j):
    posible = posibles(i,j)
    if posible is False:
        pass
    else:
        if len(posible) == 1:
            matriz[i, j] = posible[0]
    return None


# con realizar la operacion de rellenado 6 o 7 veces es suficiente
z = 0
while z < 6:
    for x in range(9):
        for y in range(9):
            rellenado(y,x)
    z += 1

print(matriz)
