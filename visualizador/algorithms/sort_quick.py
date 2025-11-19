items = []
n = 0
pila = []
bajo = 0
alto = 0
i = 0
j = 0
pivot_v = 0
pivote_idx = -1
fase = 0

def swap(idx1, idx2):
    global items
    items[idx1], items[idx2] = items[idx2], items[idx1]
    return {"a": idx1, "b": idx2, "swap": True}

def init(vals):
    global items, n, pila, bajo, alto, i, j, pivot_v, pivote_idx, fase
    items = list(vals)
    n = len(items)
    pila = [(0, n - 1)]
    i = 0
    j = 0
    pivot_v = 0
    pivote_idx = -1
    fase = 0
    return {"pila": pila}

def step():
    global items, n, pila, bajo, alto, i, j, pivot_v, pivote_idx, fase

    if not pila and fase == 0:
        return {"done": True}

    if fase == 0:
        if pila:
            bajo, alto = pila.pop()
            if bajo >= alto:
                return step()

            pivot_v = items[alto]
            pivote_idx = alto
            i = bajo - 1
            j = bajo
            fase = 1
            return {"a": bajo, "b": alto, "swap": False}
        else:
            return {"done": True}

    if fase == 1:
        if j < alto:
            out = {"a": j, "b": pivote_idx, "swap": False}

            if items[j] < pivot_v:
                i += 1
                if i != j:
                    rep = swap(i, j)
                    out["a"] = rep["a"]
                    out["b"] = rep["b"]
                    out["swap"] = True

            j += 1
            return out

        else:
            fase = 2

    if fase == 2:
        final_pos = i + 1
        did_swap = False

        if final_pos != alto:
            rep = swap(final_pos, alto)
            did_swap = True
            a = rep["a"]
            b = rep["b"]
        else:
            a = final_pos
            b = alto

        if bajo < final_pos - 1:
            pila.append((bajo, final_pos - 1))

        if final_pos + 1 < alto:
            pila.append((final_pos + 1, alto))

        fase = 0
        pivote_idx = -1

        return {"a": a, "b": b, "swap": did_swap}

    return {"done": True}
