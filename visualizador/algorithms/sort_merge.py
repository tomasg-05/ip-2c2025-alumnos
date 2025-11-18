# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

from heapq import merge


items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n, task, merge
    items = list(vals)
    n = len(items)
    task=[(0,n)]
    merge=None
    # TODO: inicializar punteros/estado

def step():
    global items,task,merge
    if merge is not None:
        L, R = merge["L"], merge["R"]
        i, j, w = merge["i"], merge["j"], merge["w"]
        ls, rs = merge["ls"], merge["rs"]
        if i < len(L) and j < len(R):
            a=ls + i
            b=rs + j
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
    l, r = task.pop()
    if r - l <= 1:
        return {"a": l, "b": l, "swap": False, "done": False}
    m = (l + r) // 2
    if task and task[-1] == (l, r):
        task.pop()
        merge = {
            "L": items[l:m],
            "R": items[m:r],
            "i": 0,
            "j": 0,
            "w": l,
            "ls": l,
            "rs": m
        }
        return {"a": l, "b": m, "swap": False, "done": False}
    task.append((l, r))
    task.append((m, r))
    task.append((l, m))
    
    return {"a": l, "b": r - 1, "swap": False, "done": False}

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
