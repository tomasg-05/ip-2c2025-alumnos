# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
gap = 0
i = 0
j = None

def init(vals):
    global items, n, gap, i, j
    items = list(vals)
    n = len(items)
    gap = n // 2        # primer gap
    i = gap            # primer indice valido para comparacion
    j = None           # j desactivado al inicio

def step():
    global items, n, gap, i, j

    # si gap llego a 0, termino
    if gap == 0:
        return {"done": True}

    # si j no esta activo, comenzamos nueva insercion con gap
    if j is None:
        if i >= n:
            # reducir gap
            gap //= 2
            if gap == 0:
                return {"done": True}
            i = gap
            j = None
            return {"a": 0, "b": 0, "swap": False, "done": False}
        j = i
        return {"a": j - gap, "b": j, "swap": False, "done": False}

    # comparar con separacion gap
    if j - gap >= 0 and items[j] < items[j - gap]:
        a = j
        b = j - gap
        items[a], items[b] = items[b], items[a]
        j -= gap
        return {"a": a, "b": b, "swap": True, "done": False}

    # si no hay swap, avanzar
    i += 1
    j = None
    return {"a": 0, "b": 0, "swap": False, "done": False}
    