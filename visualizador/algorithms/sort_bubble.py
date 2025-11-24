# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = [] #Lista de enteros sobre la que vamos a trabajar.
n = 0 #Longitud de la lista.
i = 0 #Puntero exterior.
j = 0 #Puntero interior 

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    #Realiza UN solo micro paso (comparacion o swap) del bubble sort.
    #La UI llama a esta funcion repetidamente para crear la animacion.
    global items, n,i,j
    # Chequeo de finalizacion
    # Si "i" ha avanzado n-1 veces, todos los elementos estan en su lugar.
    if i >= n - 1:
        return {"done": True}
     # Fin de pasada
    # Si "j" llego al final de la pasada actual (n - 1 - i), significa que 
    # el elemento mas grande ha bubujeo a su posicion final (indice n-1-i).
    if j >= n - 1 - i:
        # Avanzamos la pasada exterior "i" y reseteamos "j" para la proxima pasada.
        i += 1
        j = 0
        # Devolvemos un paso de transicion (sin accion) para que el visualizador 
        # limpie el resaltado y se prepare.
        return {"a": 0, "b": 0, "swap": False, "done": False}
    
    # Micro paso de comparacion y swap
    #Definimos los indices adyacentes a comparar en este micro paso.
    a=j
    b=j+1
    swap=False

    #Si el elemento de la izquierda "a" es mayor que el de la derecha "b".
    if items[a]>items[b]:
        items[a],items[b]= items[b],items[a]
        swap=True
    #El visualizador hace el swap en pantalla porque devolvemos swap=True.

    #Movemos el cursor "j" al siguiente par para el proximo step()
    j= j + 1
    # Retorna el estado del micro paso  
    return {"a": a, "b": b, "swap": swap, "done": False}