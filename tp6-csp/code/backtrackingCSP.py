def crear_matriz(n):
    # Crear una matriz vacía de tamaño n x n
    matriz = [[0] * n for _ in range(n)]

    # Llenar la matriz con valores de 0 a n-1 en cada columna
    for columna in range(n):
        for fila in range(n):
            matriz[fila][columna] = fila  # Asignar valores incrementales en cada columna
    return matriz

def estan_en_diagonal(vector,n):
    # Recorrer cada par de elementos del vector para verificar las diagonales
    for fila1 in range(n):
        if vector[fila1] is None:
            continue  # Ignorar si el valor de la columna es None
        for fila2 in range(fila1 + 1, n):
            if vector[fila2] is None:
                continue  # Ignorar si el valor de la columna es None
            # Si están en la misma diagonal
            if abs(fila1 - fila2) == abs(vector[fila1] - vector[fila2]):
                return True  # Hay al menos una diagonal conflictiva
    return False  # No hay elementos en diagonal

def posiciones_sin_multiples_valores(vector):
    # Verificar que cada posición tenga un único valor o esté vacía (None)
    for valor in vector:
        # Si el valor es una colección (lista, conjunto o tupla) y tiene más de un elemento
        if isinstance(valor, (list, set, tuple)) and len(valor) > 1:
            return valor
    return None

def vuelta_atras_recursiva(asignacion,n):
    index = posiciones_sin_multiples_valores(asignacion)
    if index is None: return asignacion

    #todos_los_valores = set(range(n))
    #valores_en_vector = set(asignacion)
    #valores_faltantes = todos_los_valores - valores_en_vector
    valores=asignacion[index]
    for valor in valores:
        asignacion[index] = valor
        #print(valores_faltantes,f"analizando el index {index}, asignacion {asignacion}, hay valores en la diagonal {estan_en_diagonal(asignacion,n)}")

        if not estan_en_diagonal(asignacion,n):
            #print(f"entra {asignacion}")
            comprobar=vuelta_atras_recursiva(asignacion,n)
            #print(f"sale {comprobar}")

            if comprobar is not None:
                return asignacion
        asignacion[index] = None
    return None


def busqueda_vuelta_atras(n):

    return vuelta_atras_recursiva(crear_matriz(n),n)
#vec=[0,4,5]
#print(estan_en_diagonal(vec,3))
print(busqueda_vuelta_atras(12))