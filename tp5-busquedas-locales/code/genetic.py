import random
import matplotlib.pyplot as plt


def h_reinas(board, n):
    amenazas = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                amenazas += 1
    return amenazas


def initializer(n, population_size=100):
    return [[random.randint(0, n - 1) for _ in range(n)] for _ in range(population_size)]


def fitCalculator(population):
    return [h_reinas(board, len(board)) for board in population]


def selector(population, fitness, selection_size=50):
    selected = sorted(zip(population, fitness), key=lambda x: x[1])[:selection_size]
    return [individual for individual, _ in selected]


def crossOver(selected_population, n):
    new_population = []
    num_individuals = len(selected_population)
    for _ in range(num_individuals // 2):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        crossover_point = random.randint(1, n - 2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        new_population.extend([child1, child2])
    new_population = new_population[:num_individuals // 2]
    combined_population = selected_population[:num_individuals // 2] + new_population
    return combined_population


def mutation(population, mutation_rate=0.1):
    for individual in population:
        if random.uniform(0, 1) < mutation_rate:
            col = random.randint(0, len(individual) - 1)
            individual[col] = random.randint(0, len(individual) - 1)


def genetic(n, time):
    t = 0
    population = initializer(n)
    fitness = fitCalculator(population)
    min_H_values = []  # Lista para almacenar el mínimo H en cada iteración

    while t < time:
        best_population = selector(population, fitness)
        population = crossOver(best_population, n)
        mutation(population)
        fitness = fitCalculator(population)

        min_H = min(fitness)
        min_H_values.append(min_H)  # Guardar el valor mínimo de H en esta iteración

        if min_H == 0:
            break

        t += 1

    # Retornar la lista de valores mínimos de H para cada iteración
    return min_H_values


def plot_h_variation(min_H_values, filename="variacion_h.png"):
    plt.plot(min_H_values, label="H(min) por iteración")
    plt.xlabel("Iteración")
    plt.ylabel("Valor de H (amenazas)")
    plt.title("Variación de H a lo largo de las iteraciones (Genetic)")
    plt.legend()
    plt.savefig(filename)  # Guardar el gráfico como un archivo
    plt.close()  # Cerrar el gráfico para liberar memoria


# Ejecutar el algoritmo para n=10 y tiempo límite de 1000 iteraciones
n = 10
time_limit = 1000
min_H_values = genetic(n, time_limit)

# Guardar el gráfico de los resultados
plot_h_variation(min_H_values, filename="../images/variacion_h_n10.png")
