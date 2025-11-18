# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    if i >= n - 1:
        return {"done": True}
    if fase == "buscar":
        # Si j llegó al final pasa a fase de swap
        if j >= n:
            fase = "swap"
            return {"a": i, "b": min_idx, "swap": False, "done": False}
        comparacion_j = j
        # Buscar el minimo(orden acendente)
        if items[j] < items[min_idx]:
            min_idx = j
        j += 1
        return {"a": min_idx, "b": comparacion_j, "swap": False, "done": False}
    elif fase == "swap":
        swap_hecho = False
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap_hecho = True
        antiguo_i = i
        antiguo_min = min_idx
        # Avanzar a la siguiente pasada
        i += 1
        min_idx = i
        j = i + 1
        fase = "buscar"
        #devuelve los indices reales del swap
        return {"a": antiguo_i, "b": antiguo_min, "swap": swap_hecho, "done": False}