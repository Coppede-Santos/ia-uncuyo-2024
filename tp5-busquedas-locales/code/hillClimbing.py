import random









def h_reinas(table,n):
    # Listas para almacenar si hay más de una reina en filas, columnas, diagonales
    filas = [0] * n
    columnas = [0] * n
    diag_principal = {}
    diag_secundaria = {}
    
    # Encontrar todas las reinas en el tablero
    reinas = [(i, j) for i in range(n) for j in range(n) if table[i][j]]
    
    # Marcar posiciones amenazadas
    amenazadas = set()
    
    for i, j in reinas:
        diag_princ = i - j
        diag_sec = i + j
        
        # Si ya hay una reina en la misma fila, columna o diagonales, las añadimos a las amenazadas
        if filas[i] > 0:
            amenazadas.update((i, k) for k in range(n) if table[i][k])  # Marcar todas las reinas en esa fila
        if columnas[j] > 0:
            amenazadas.update((k, j) for k in range(n) if table[k][j])  # Marcar todas las reinas en esa columna
        if diag_principal.get(diag_princ, 0) > 0:
            amenazadas.update((i+k, j+k) for k in range(-min(i,j), min(n-i, n-j)) if table[i+k][j+k])  # Diagonal principal
        if diag_secundaria.get(diag_sec, 0) > 0:
            amenazadas.update((i+k, j-k) for k in range(-min(i,n-j-1), min(n-i, j+1)) if table[i+k][j-k])  # Diagonal secundaria
        
        # Actualizar las amenazas en filas, columnas y diagonales
        filas[i] += 1
        columnas[j] += 1
        diag_principal[diag_princ] = diag_principal.get(diag_princ, 0) + 1
        diag_secundaria[diag_sec] = diag_secundaria.get(diag_sec, 0) + 1
    
    return len(amenazadas)

# Ejemplo de uso:
#tablero = [
#    [False,True, False,False],
#    [False, False, True,False],
#    [False, True, False,False],
#    [False, False, False,True]
#]
##print(h_reinas_a(tablero,4))  # Salida esperada: 3

###[[True,False,False],[False,False,True],[False,True,False]]
def hillClimbing_reinas(n,states):
    current=make_table(n)
    cont=0

    while True:


        better=make_table(n)
        nmo_better=h_reinas(better,n)
        for i in range(1,n):
            new=make_table(n)
            nmo_new=h_reinas(new,n)
            if nmo_new<nmo_better:
                better=new
                nmo_better=nmo_new
        
        if nmo_better<=h_reinas(current,n):
            current=better
        
            

        if h_reinas(current,n)==0: break

        if cont == states:
            break
        cont+=1
    return [cont,current,h_reinas(current,n)]



def make_table(n):
    # Crear un tablero vacío (n x n) con todas las posiciones en False
    table = [[False for _ in range(n)] for _ in range(n)]
    
    # Colocar reinas en posiciones aleatorias
    posiciones_reinas = random.sample([(i, j) for i in range(n) for j in range(n)], n)
    
    for i, j in posiciones_reinas:
        table[i][j] = True
    
    return table

#tablero = crear_table(4)

#for fila in tablero:
# #   print(fila)

resul=hillClimbing_reinas(8,10000)

print("num de iter: ",resul[0]," +++ h: ", resul[2])
for fila in resul[1]:
   print(fila)