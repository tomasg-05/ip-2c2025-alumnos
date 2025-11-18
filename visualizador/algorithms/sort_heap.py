# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
#punteros/estado
n = 0
i=0
j=0
fase= "build" 
stack= [] 

def init(vals):
    global items, n, i, j, fase, stack
    items = list(vals)
    n = len(items)
    i= n//2-1
    j=None
    fase= "build"
    stack=[]

def step():
    global items, n, i, j, fase, stack
    if fase == "build":
        fase= "sort"
        i= n-1
        j= 0
        return {"a":0,"b":0,"swap":False,"done":False}
    if j is None:
        j= i
        stack=[]
    left= 2*j + 1
    right= 2*j + 2
    if left >= n:
        i-=1
        j=None
        return{"a":0, "b":0, "swap":False, "done":False}
    mayor = left
    if right < n and items[right] > items[left]:
        mayor= right
    if items[mayor] > items[j]:
        a, b= j, mayor
        items[a], items[b] =items[b], items[a]
        j= mayor
        return{"a":0, "b":0, "swap":True, "done":False}
    else:
        i-=1
        j=None
        return{"a":0, "b":0, "swap":False, "done":False}

    if fase == "sort":
        if i <= 0:
            return{"done":True}
    if j == 0:
        a, b = 0, i
        items[a], items[b] = items[b], items[a]
        i-= 1
        j= 0
        return{"a":a, "b":b, "swap":True, "done":False}
    
    left= 2*j + 1
    right= 2*j + 2
    
    if left > i:
        j = 0
        return{"a": 0, "b": 0, "swap": False, "done": False}
   
    mayor = left
    
    if right <= i and items[right] > items[left]:
        mayor = right


    
    

    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    
