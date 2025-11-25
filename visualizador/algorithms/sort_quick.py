items = []       # Lista a ordenar
n = 0            # Cantidad de elementos
pila = []        # Pila para simular la recursion
bajo = 0         # Limite inferior del segmento actual 
alto = 0         # Limite superior del segmento actual 
i = 0            # Indice que separa menores que el pivote 
j = 0            # Cursor que recorre el segmento
pivot_v = 0      # Valor del pivote
pivote_idx = -1  # Indice del pivote 
fase = 0         # 0 = elegir pivote, 1 = particionar, 2 = colocar pivote

# Intercambio simple entre dos posiciones
def swap(idx1, idx2):
    global items
    items[idx1], items[idx2] = items[idx2], items[idx1]
    return {"a": idx1, "b": idx2, "swap": True}

# Inicializacion del algoritmo 
def init(vals):
    global items, n, pila, bajo, alto, i, j, pivot_v, pivote_idx, fase
    items = list(vals)        # Copiamos la lista original
    n = len(items)
    pila = [(0, n - 1)]       # Primer segmento completo en la pila
    i = 0
    j = 0
    pivot_v = 0
    pivote_idx = -1
    fase = 0                  # Comenzamos en fase de seleccion de pivote 
    return {"pila": pila}

def step():
    global items, n, pila, bajo, alto, i, j, pivot_v, pivote_idx, fase

    # Si no quedan segmentos por procesar, finalizado 
    if not pila and fase == 0:
        return {"done": True}


    if fase == 0:
        if pila:
            bajo, alto = pila.pop()     # Extraemos un rango pendiente

            # Si el segmento es invalido o de un solo elemento → saltamos 
            if bajo >= alto:
                return step()

            # Elegimos el pivote: el ultimo elemento del segmento 
            pivot_v = items[alto]
            pivote_idx = alto

            # i empieza antes de bajo, j empieza en bajo
            i = bajo - 1
            j = bajo

            fase = 1   # Pasamos a la fase de particion 
            return {"a": bajo, "b": alto, "swap": False}
        else:
            return {"done": True}

   
    if fase == 1:
        # Mientras j aun no llego al pivote 
        if j < alto:
            out = {"a": j, "b": pivote_idx, "swap": False}

            # Si el elemento es menor que el pivote, mover al sector izquierdo 
            if items[j] < pivot_v:
                i += 1
                if i != j:
                    rep = swap(i, j)    # Hacemos el swap y lo devolvemos
                    out["a"] = rep["a"]
                    out["b"] = rep["b"]
                    out["swap"] = True

            j += 1                      # Avanzamos j
            return out

        else:
            # Particion terminada,  pasamos a colocar el pivote en su lugar 
            fase = 2


    if fase == 2:
        final_pos = i + 1        # Lugar correcto del pivote
        did_swap = False

        # Si el pivote no esta en su lugar, intercambiarlo 
        if final_pos != alto:
            rep = swap(final_pos, alto)
            did_swap = True
            a = rep["a"]
            b = rep["b"]
        else:
            a = final_pos
            b = alto

        # Agregar a la pila el segmento izquierdo del pivote
        if bajo < final_pos - 1:
            pila.append((bajo, final_pos - 1))

        # Agregar el segmento derecho del pivote
        if final_pos + 1 < alto:
            pila.append((final_pos + 1, alto))

        fase = 0            # Volver a la fase inicial para el siguiente segmento
        pivote_idx = -1

        return {"a": a, "b": b, "swap": did_swap}

    return {"done": True}
