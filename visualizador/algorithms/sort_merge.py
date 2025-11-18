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
    def mergesort(list):
        if len(list)==1:# TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
            return list     # Recordá:
        middle=len(list)//2# - a, b dentro de [0, n-1]
        left_array=list[:middle]# - si swap=True, primero hacé el intercambio en 'items'
        right_array=list[middle:]# - cuando termines, devolvé {"done": True}
        sorted_left_array=mergesort(left_array)
        sorted_right_array=mergesort(right_array)
        return merge(sorted_left_array,sorted_right_array)
    def merge(left_list,right_list):
        list_resultado=[]
        while len(left_list)>0 and len(right_list)>0:
            if left_list[0] > right_list[0]:
                list_resultado.append(right_list[0])
                right_list.pop(0)
            else:
                 list_resultado.append(left_list[0])
                 left_list.pop(0)
        while len(left_list)>0:
            list_resultado.append(left_list[0])
            left_list.pop(0)
        while len(right_list)>0:
            list_resultado.append(right_list[0])
            right_list.pop(0) 
        return list_resultado   
    return {"done": True}
