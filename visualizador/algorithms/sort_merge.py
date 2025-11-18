# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

from heapq import merge


items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    # TODO: inicializar punteros/estado

def step():
    def mergesort(n):
        if len(n)==1:# TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
            return n     # Recordá:
        middle=len(n)//2# - a, b dentro de [0, n-1]
        left_array=n[:middle]# - si swap=True, primero hacé el intercambio en 'items'
        right_array=n[middle:]# - cuando termines, devolvé {"done": True}
        sorted_left_array=mergesort(left_array)
        sorted_right_array=mergesort(right_array)
        return merge(sorted_left_array,sorted_right_array)
    def merge(left_n,right_n):
        list_resultado=[]
        while len(left_n)>0 and len(right_n)>0:
            if left_n[0] > right_n[0]:
                list_resultado.append(right_n[0])
                right_n.pop(0)
            else:
                 list_resultado.append(left_n[0])
                 left_n.pop(0)
        while len(left_n)>0:
            list_resultado.append(left_n[0])
            left_n.pop(0)
        while len(right_n)>0:
            list_resultado.append(right_n[0])
            right_n.pop(0) 
        return list_resultado   
    return {"done": True}
