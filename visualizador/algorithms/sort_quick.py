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
  global items, pivote_idx # <--- ¡CORRECCIÓN! Ahora es global
  items[idx1], items[idx2] = items[idx2], items[idx1]
  return {"a": idx1, "b": idx2, "swap": True, "pivot": pivote_idx}

def init(vals):
    global items, n, pila, bajo,alto,i,pivote_v,pivote_idx,fase,j
    items = list(vals)
    n = len(items)

     # Inicializa la pila con el rango completo
    pila = [(0, n - 1)] # Guardamos (bajo, alto)

    # Reinicializa el estado para el primer paso
    i = 0
    j = 0
    pivote_v = 0
    pivote_idx = -1
    fase = 0
    return {"pila": pila}
   

def step():
    global items, n, pila, bajo, alto, i, j, pivote_v, pivote_idx, fase
    if not pila and fase == 0:
        return {"done": True}
    if fase == 0:
        if pila:
            # Sacamos el rango (bajo, alto) de la pila
            bajo, alto= pila.pop()
            if bajo >= alto:
                # Si el rango es trivial (0 o 1 elemento), salta al siguiente
                return step()
            
             # Inicializa punteros y pivote
            pivot_v = items[alto]  # Elegimos el ultimo como pivote
            pivote_idx = alto        # El indice del pivote actual
            i = bajo - 1
            j = bajo
            fase = 1 # Pasa a la fase de particion (bucle principal)
              # Devuelve un paso de "preparacion" (destacar el pivote)
            return {"a": bajo, "b": alto, "swap": False, "pivot": pivote_idx}
        else:
            return {"done": True}
        #Bucle de particion (j itera de bajo a alto - 1)

    if fase == 1:
        # El bucle va hasta alto - 1 (el pivote)
        if j < alto:
            # Reporta la comparacion del elemento actual (j) con el pivote
            dict_out = {"a": j, "b": pivote_idx, "swap": False, "pivot": pivote_idx}
            if items[j] < pivote_v:
                i += 1
                if i != j:
# Ejecuta el swap y obtiene el reporte
                    swap_reporte = swap(i, j)
                   #Agrega las claves del swap al dict_out 
                dict_out["a"] = swap_reporte["a"]
                dict_out["b"] = swap_reporte["b"]
                dict_out["swap"] = swap_reporte["swap"]
                # Tambien si el visualizador necesita items:
                # dict_out["items"] = swap_reporte["items"]
            j += 1 # Avanza el puntero j
            return dict_out
        else:
            # El bucle de particion (j) ha terminado
            fase = 2 # Pasa a la fase de colocacion del pivote
             #Colocamos el pivote en su posicion final
    if fase == 2:
        # Coloca el pivote (items[alto]) en su posicion final (i + 1)
        final_pivote_pos = i + 1
        # Si el pivote ya esta en la posición correcta, no swapear con si mismo
        if final_pivote_pos != alto:
            swap(final_pivote_pos, alto) 
        # Agrega los nuevos sub problemas a la pila para la proxima iteracion
        # Sub array izquierdo
        if bajo< final_pivote_pos - 1:
            pila.append((bajo, final_pivote_pos - 1))

        # Sub array derecho
        if final_pivote_pos + 1 < alto:
            pila.append((final_pivote_pos + 1, alto))
        fase = 0 # Vuelve a la fase de seleccion para el siguiente sub array
        pivote_idx = -1 # Limpia el pivote
        # Devuelve el paso final de la particion
        return {"a": final_pivote_pos, "b": alto, "swap": True, "pivot": final_pivote_pos}
    return {"done": True}