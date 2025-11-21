# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
items = []
n = 0
gap = 0
i = 0
j = 0

def init(vals):
    global items, n, gap, i, j
    items = list(vals)
    n = len(items)
    gap = n // 2
    i = gap
    j = 0

def step():
    global items, n, gap, i, j

    if gap == 0:
        return {"done": True}

    if i < n:
        if j >= gap and items[j] > items[j-gap]:
            a = j
            b = j-gap
            items[a], items[b] = items[b], items[a]
            j -= gap
            return {"a": a, "b": b, "swap": True, "done": False}
        else:
            i += 1
            j = i
            return {"a": i-1 if i-1 < n else n-1, "b": j-gap if j-gap >= 0 else 0, "swap": False, "done": False}
    else:
        gap //= 2
        i = gap
        j = i
        return {"a": 0, "b": 0, "swap": False, "done": False}
    