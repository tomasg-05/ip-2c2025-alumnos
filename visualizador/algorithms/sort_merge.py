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
    global items, task, merge

    if merge is not None:
        L = merge["L"]
        R = merge["R"]
        i = merge["i"]
        j = merge["j"]
        w = merge["w"]

        if i < len(L) and j < len(R):
            a = merge["l"] + i
            b = merge["m"] + j
            if L[i] <= R[j]:
                items[w] = L[i]
                merge["i"] += 1
            else:
                items[w] = R[j]
                merge["j"] += 1
            merge["w"] += 1
            return {"a": a, "b": b, "swap": True, "done": False}

        if i < len(L):
            a = merge["l"] + i
            b = w
            items[w] = L[i]
            merge["i"] += 1
            merge["w"] += 1
            return {"a": a, "b": b, "swap": True, "done": False}

        if j < len(R):
            a = merge["m"] + j
            b = w
            items[w] = R[j]
            merge["j"] += 1
            merge["w"] += 1
            return {"a": a, "b": b, "swap": True, "done": False}

        merge = None
        return {"a": 0, "b": 0, "swap": False, "done": False}

    if not task:
        return {"done": True}

    tipo, l, r = task.pop()

    if tipo == "split":
        if r - l <= 1:
            return {"a": l, "b": l, "swap": False, "done": False}
        m = (l + r) // 2
        task.append(("merge", l, r))
        task.append(("split", m, r))
        task.append(("split", l, m))
        return {"a": l, "b": r - 1, "swap": False, "done": False}

    if tipo == "merge":
        m = (l + r) // 2
        L = items[l:m].copy()
        R = items[m:r].copy()
        merge = {
            "L": L,
            "R": R,
            "i": 0,
            "j": 0,
            "w": l,
            "l": l,
            "m": m
        }
        return {"a": l, "b": m - 1, "swap": False, "done": False}




#    def mergesort(n):
 #       if len(n)==1:# TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
  #          return n     # Recordá:
   #     middle=len(n)//2# - a, b dentro de [0, n-1]
    #    left_array=n[:middle]# - si swap=True, primero hacé el intercambio en 'items'
     #   right_array=n[middle:]# - cuando termines, devolvé {"done": True}
      #  sorted_left_array=mergesort(left_array)
       # sorted_right_array=mergesort(right_array)
        #return merge(sorted_left_array,sorted_right_array)
    #def merge(left_n,right_n):
     #   list_resultado=[]
      #  while len(left_n)>0 and len(right_n)>0:
       #     if left_n[0] <= right_n[0]:
        #        list_resultado.append(right_n[0])
         #       right_n.pop(0)
          #  else:
           #      list_resultado.append(left_n[0])
            #     left_n.pop(0)
    #    while len(left_n)>0:
     #       list_resultado.append(left_n[0])
      #      left_n.pop(0)
       # while len(right_n)>0:
        #    list_resultado.append(right_n[0])
         #   right_n.pop(0) 
        #return list_resultado   
    #return {"done": True}
