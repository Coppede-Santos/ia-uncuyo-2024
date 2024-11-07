import random
import matplotlib.pyplot as plt


def h_reinas(table, n):
    filas = [0] * n
    columnas = [0] * n
    diag_principal = {}
    diag_secundaria = {}
    reinas = [(i, j) for i in range(n) for j in range(n) if table[i][j]]
    amenazadas = set()

    for i, j in reinas:
        diag_princ = i - j
        diag_sec = i + j

        if filas[i] > 0:
            amenazadas.update((i, k) for k in range(n) if table[i][k])
        if columnas[j] > 0:
            amenazadas.update((k, j) for k in range(n) if table[k][j])
        if diag_principal.get(diag_princ, 0) > 0:
            amenazadas.update((i + k, j + k) for k in range(-min(i, j), min(n - i, n - j)) if table[i + k][j + k])
        if diag_secundaria.get(diag_sec, 0) > 0:
            amenazadas.update(
                (i + k, j - k) for k in range(-min(i, n - j - 1), min(n - i, j + 1)) if table[i + k][j - k])

        filas[i] += 1
        columnas[j] += 1
        diag_principal[diag_princ] = diag_principal.get(diag_princ, 0) + 1
        diag_secundaria[diag_sec] = diag_secundaria.get(diag_sec, 0) + 1

    return len(amenazadas)


def mmake_table(n):
    table = [[False for _ in range(n)] for _ in range(n)]
    posiciones_reinas = random.sample([(i, j) for i in range(n) for j in range(n)], n)
    for i, j in posiciones_reinas:
        table[i][j] = True
    return table


def hillClimbing_reinas(n, states):
    current = mmake_table(n)
    cont = 0
    h_values = []  # Lista para almacenar H en cada iteración

    while cont < states:
        better = mmake_table(n)
        nmo_better = h_reinas(better, n)

        for i in range(1, n):
            new = mmake_table(n)
            nmo_new = h_reinas(new, n)
            if nmo_new < nmo_better:
                better = new
                nmo_better = nmo_new

        if nmo_better <= h_reinas(current, n):
            current = better

        h_current = h_reinas(current, n)
        h_values.append(h_current)  # Guardar el valor de H de la iteración actual

        if h_current == 0:
            break

        cont += 1

    return current, cont, h_values


def plot_h_variation(h_values, filename="variacion_h_hillclimbing.png"):
    plt.plot(h_values, label="H(min) por iteración")
    plt.xlabel("Iteración")
    plt.ylabel("Valor de H (amenazas)")
    plt.title("Variación de H a lo largo de las iteraciones (Hill Climbing)")
    plt.legend()
    plt.savefig(filename)  # Guardar el gráfico como archivo
    plt.close()


# Ejecutar el algoritmo con n=10 y límite de 1000 iteraciones
n = 10
states = 1000
_, _, h_values = hillClimbing_reinas(n, states)

# Guardar el gráfico de la variación de H
plot_h_variation(h_values, filename="../images/variacion_h_hillclimbing_n10.png")
