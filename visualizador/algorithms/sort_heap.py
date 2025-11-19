# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

#punteros/estados
items = []
n = 0
i = 0
j = 0
fase = "build"
stack = []

def init(vals):
    global items, n, i, j, fase, stack
    items = list(vals)
    n = len(items)
    i = n//2 - 1
    j = None
    fase = "build"
    stack = []

def step():
    global items, n, i, j, fase, stack

    if fase == "build":
        if i < 0:
            fase = "sort"
            i = n - 1
            j = None
            return {"a":0, "b":0, "swap":False, "done":False}

        if j is None:
            j = i

        left = 2*j + 1
        right = 2*j + 2

        if left >= n:
            a = i
            b = left
            i -= 1
            j = None
            return {"a":a, "b":b, "swap":False, "done":False}

        mayor = left
        if right < n and items[right] > items[left]:
            mayor = right

        if items[mayor] > items[j]:
            a = j
            b = mayor
            items[a], items[b] = items[b], items[a]
            j = mayor
            return {"a":a, "b":b, "swap":True, "done":False}

        a = i
        b = mayor
        i -= 1
        j = None
        return {"a":a, "b":b, "swap":False, "done":False}

    if fase == "sort":
        if i <= 0:
            return {"done":True}

        if j is None:
            a = 0
            b = i
            items[a], items[b] = items[b], items[a]
            i -= 1
            j = 0
            return {"a":a, "b":b, "swap":True, "done":False}

        left = 2*j + 1
        right = 2*j + 2

        if left > i:
            a = j
            b = left
            j = None
            return {"a":a, "b":b, "swap":False, "done":False}

        mayor = left
        if right <= i and items[right] > items[left]:
            mayor = right

        if items[mayor] > items[j]:
            a = j
            b = mayor
            items[a], items[b] = items[b], items[a]
            j = mayor
            return {"a":a, "b":b, "swap":True, "done":False}

        a = j
        b = mayor
        j = None
        return {"a":a, "b":b, "swap":False, "done":False}
