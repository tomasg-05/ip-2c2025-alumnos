# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

from heapq import merge

items = []
n = 0
task = []
merge = None

def init(vals):
    global items, n, task, merge
    items = list(vals)
    n = len(items)
    task = [("split", 0, n)]
    merge = None

def step():
    global items,task,merge
    if merge is not None:
        L, R = merge["L"], merge["R"]
        i, j, w = merge["i"], merge["j"], merge["w"]
        ls, rs = merge["ls"], merge["rs"]
        if i < len(L) and j < len(R):
            a, b = ls + i, rs + j
            if L[i] <= R[j]:
                items[w] = L[i]
                i+=1
            else:
                items[w] = R[j]
                j += 1
            merge["i"], merge["j"], merge["w"] = i, j, w + 1
            return {"a": a, "b": b, "swap": False, "done": False}
        if i < len(L):
            items[w] = L[i]
            merge["i"], merge["w"] = i + 1, w + 1
            return {"a": w, "b": w, "swap": False, "done": False}
        if j < len(R):
            items[w] = R[j]
            merge["j"], merge["w"] = j + 1, w + 1
            return {"a": w, "b": w, "swap": False, "done": False}
        merge = None
        return {"a": 0, "b": 0, "swap": False, "done": False}
    if not task:
        return {"done": True}
    tipo,l, r = task.pop()
    if tipo == "split":
        if r - l <= 1:
            return {"a": l, "b": l, "swap": False, "done": False}
        m = (l + r) // 2
        task.append(("merge",l, r))
        task.append(("split",m, r))
        task.append(("split",l, m))    
        return {"a": l, "b": r-1, "swap": False, "done": False}
    elif tipo == "merge":       
        m = (l + r) // 2
        L= items[l:r].copy()
        R = items[m:r].copy()
        merge = {"L": L, "R": R, "i": 0, "j": 0, "w": l, "ls": l, "rs": m}
        return {"a": l, "b": m-1, "swap": False, "done": False}