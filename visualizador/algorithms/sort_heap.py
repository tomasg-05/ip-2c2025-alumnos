# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

#Lista que se va a ordenar
items = []
#Cantidad de elementos
n = 0
#Indices utilizados para recorrer y ajustar el heap
i = 0
j = 0
#Indica en que etapa del algoritmo estamos: construcción o ordenamiento
fase = "build"
#Variable reservada por si fuera necesario almacenar estados
stack = []

def init(vals):
    global items, n, i, j, fase, stack
    #Se copia la lista de entrada para trabajar sobre ella
    items = list(vals)
    #se almacena el tamaño de la lista
    n = len(items)
    #Se establece el indice inicial desde el cual se comienza a construir el heap
    i = n//2 - 1
    #j queda sin asignacion específica hasta ser utilizado
    j = None
    #La primera fase consiste en construir el heap
    fase = "build"
    #Se reinicia el stack
    stack = []

def step():
    global items, n, i, j, fase, stack
#Si ya se procesaron todos los nodos, se pasa a la fase de ordenamiento
    if fase == "build":
        if i < 0:
            fase = "sort"
            i = n - 1
            j = None
            return {"a":0, "b":0, "swap":False, "done":False}
#Si j aUn no fue asignado, se iguala a i
        if j is None:
            j = i
#Se calculan los indices de los hijos
        left = 2*j + 1
        right = 2*j + 2

#Si no existen hijos dentro del rango, se continua con el siguiente nodo
        if left >= n:
            a = i
            b = left
            i -= 1
            j = None
            return {"a":a, "b":b, "swap":False, "done":False}
#se toma inicialmente el hijo izquierdo como el mayor
        mayor = left
#Si el hijo derecho existe y es mayor, se actualiza
        if right < n and items[right] > items[left]:
            mayor = right

#Si el hijo es mayor que el padre, se intercambian
        if items[mayor] > items[j]:
            a = j
            b = mayor
            items[a], items[b] = items[b], items[a]
            #Se continua evaluando hacia abajo
            j = mayor
            return {"a":a, "b":b, "swap":True, "done":False}

#Si no hay intercambio, se pasa al siguiente nodo superior
        a = i
        b = mayor
        i -= 1
        j = None
        return {"a":a, "b":b, "swap":False, "done":False}

    if fase == "sort":
        # Si i llega a 0, el proceso finaliza
        if i <= 0:
            return {"done":True}

#Si se inicia un nuevo ciclo de bajada
        if j is None:
            #Se intercambia la raiz con el ultimo elemento valido
            a = 0
            b = i
            items[a], items[b] = items[b], items[a]
            #Se reduce el area activa del heap
            i -= 1
            #Se comienza nuevamente desde la raiz
            j = 0
            return {"a":a, "b":b, "swap":True, "done":False}

#Se calculan los hijos del nodo actual
        left = 2*j + 1
        right = 2*j + 2

#Si el hijo izquierdo esta fuera del rango, se detiene la bajada
        if left > i:
            a = j
            b = left
            j = None
            return {"a":a, "b":b, "swap":False, "done":False}

#Se toma inicialmente el hijo izquierdo como el mayor
        mayor = left
        #si el hijo derecho esta dentro del rango y es mayor, se actualiza
        if right <= i and items[right] > items[left]:
            mayor = right

#Si el hijo es mayor que el nodo actual, se realiza el intercambio
        if items[mayor] > items[j]:
            a = j
            b = mayor
            items[a], items[b] = items[b], items[a]
            #Se continua la bajada desde la nueva posicion
            j = mayor
            return {"a":a, "b":b, "swap":True, "done":False}

#Si no hay necesidad de ajustar, termina esta bajada
        a = j
        b = mayor
        j = None
        return {"a":a, "b":b, "swap":False, "done":False}
