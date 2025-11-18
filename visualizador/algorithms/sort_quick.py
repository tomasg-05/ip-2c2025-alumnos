# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
#Pila para simular la recursion (bajo, alto)
pila= []
bajo= 0 
alto= 0 
i= 0 #Indice menor
j= 0 #Indice actual
pivote_v= 0
pivote_idx= -1 #indice final del pivote
# Fases de la maquina de estados
# 0: Seleccionar un nuevo sub-array de la pila
# 1: Ejecutar el bucle de partición (mover j e intercambiar si items[j] < pivot)
# 2: Colocar el pivote en su posicion final
fase = 0 

def swap(idx1, idx2):
    """Intercambia dos elementos en la lista global."""
    global items
    items[idx1], items[idx2] = items[idx2], items[idx1]
    return {"a": idx1, "b": idx2, "swap": True, "pivot": pivote_idx}

def init(vals):
    global items, n, pila, bajo,alto,i,pivote_v,pivote_indx,fase
    items = list(vals)
    n = len(items)

     # Inicializa la pila con el rango completo
    pila = [(0, n - 1)] # Guardamos (bajo, alto)

    # Reinicializa el estado para el primer paso
    bajo_ptr = 0
    alto_ptr = 0
    i = 0
    j = 0
    pivote_v = 0
    pivote_idx = -1
    fase = 0
    return {"pila": pila}
   

def step():
    