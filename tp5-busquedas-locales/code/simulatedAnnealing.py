import random
import math
import matplotlib.pyplot as plt

def h_reinas(board, n):
    amenazas = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                amenazas += 1
    return amenazas

def make_table(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def simulatedAnnealing_reinas(n, max_iterations):
    current = make_table(n)
    cont = 0
    T = 1.0
    cooling_rate = 0.99
    h_values = []  # Lista para almacenar el valor de H en cada iteración

    while cont < max_iterations:
        next_state = current[:]
        col = random.randint(0, n - 1)
        new_row = random.randint(0, n - 1)
        next_state[col] = new_row

        nmo_current = h_reinas(current, n)
        nmo_next = h_reinas(next_state, n)

        # Guardar el valor actual de H antes de cualquier cambio de estado
        h_values.append(nmo_current)

        # Condición de aceptación para el cambio de estado
        if nmo_next < nmo_current or random.uniform(0, 1) < math.exp((nmo_current - nmo_next) / T):
            current = next_state

        # Reducir la temperatura
        T *= cooling_rate

        if nmo_next == 0:
            h_values.append(0)  # Añadir 0 cuando se encuentra una solución óptima
            break

        cont += 1

    return current, cont, h_values

def plot_h_variation(h_values, filename="variacion_h_simulatedannealing.png"):
    plt.plot(h_values, label="H por iteración")
    plt.xlabel("Iteración")
    plt.ylabel("Valor de H (amenazas)")
    plt.title("Variación de H a lo largo de las iteraciones (Simulated Annealing)")
    plt.legend()
    plt.savefig(filename)  # Guardar el gráfico como archivo
    plt.close()

# Ejecutar el algoritmo con n=10 y límite de 1000 iteraciones
n = 10
max_iterations = 1000
_, _, h_values = simulatedAnnealing_reinas(n, max_iterations)

# Guardar el gráfico de la variación de H
plot_h_variation(h_values, filename="../images/variacion_h_simulatedannealing_n10.png")


