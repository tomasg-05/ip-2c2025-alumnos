# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = [] #nuestra lista que queremos ordenar
n = 0   #cantidad de elementos que tiene nuestra lista "items"
i = 0      # indice del elemento actualque se intenta insertar/acomodar en la porcion ya ordenada (de 0 a i-1)
j = None   # indice del cursor de desplazamiento hacia la izquierda

def init(vals): # inicializa el estado del algoritmo con la lista de valores de entrada.
    global items, n, i, j 
    items = list(vals) 
    n = len(items)
    i = 1      # comun: la primera iteracion (i=1) comienza intentando insertar el segundo elemento (indice 1),asumiendo que el primer elemento (indice 0) ya es una lista ordenada de tamaño 1
    j = None # inicialmente, el cursor "j" no esta activo

def step():
    global items,n,i,j 
    if i>=n: # condicion de terminacion 
    # si "i" excede el tamaño del arreglo, todos los elementos han sido procesados
       return{"done":True}
    if j is None:  # inicio de una nueva Insercion (Nuevo "i") 
        j=i # el primer "paso" de una insercion es una comparacion inicial (sin swap) entre items[j-1] (ultimo elemento ordenado) y items[j] (el nuevo elemento)
        return{"a":j-1, "b":j,"swap":False, "done": False}
    #  Desplazamiento hacia la izquierda
    if j>0 and items[j-1] > items[j]: # Si el elemento a la izquierda es mayor, se realiza el intercambio (swap), esto "burbujea" el elemento 'items[j]' hacia su posicion correcta a la izquierda.
        items[j-1],items[j]= items[j],items[j-1]
        a= j-1
        b=j
        j-=1 # el cursor "j" se mueve una posicion a la izquierda para la siguiente comparacion
        return{"a":j, "b":j+1,"swap":True, "done":False} # se devuelve el estado ANTERIOR al decremento de "j" 
    i+=1    #se pasa al siguiente elemento a insertar
    j=None  # se resetea el cursor 'j' para la proxima insercion
    #se devuelve un paso de "avance" (no-swap) antes de iniciar la proxima insercion
    return{"a":0,"b":0, "swap":False, "done":False} # Los indices a y b no son relevantes en este avance

    