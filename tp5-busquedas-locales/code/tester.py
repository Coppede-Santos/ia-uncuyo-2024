# Importar bibliotecas necesarias
from genetic import *
from hillClimbing import *
from simulatedAnnealing import *
import time
import csv
import numpy as np
import matplotlib.pyplot as plt


# Supón que los métodos `simulatedAnnealing_reinas`, `hillClimbing_reinas` y `genetic` ya están implementados.

def ejecutar_algoritmos(n_reinas, iteraciones, max_iterations):
    resultados = {
        'Simulated Annealing': [],
        'Hill Climbing': [],
        'Genetic Algorithm': []
    }

    for _ in range(iteraciones):
        # Simulated Annealing
        start_time = time.time()
        solucion_sa, estados_visitados_sa = simulatedAnnealing_reinas(n_reinas, max_iterations)
        tiempo_sa = time.time() - start_time
        resultados['Simulated Annealing'].append((estados_visitados_sa, tiempo_sa, solucion_sa[2] == 0))

        # Hill Climbing
        start_time = time.time()
        solucion_hc, estados_visitados_hc = hillClimbing_reinas(n_reinas, max_iterations)
        tiempo_hc = time.time() - start_time
        resultados['Hill Climbing'].append((estados_visitados_hc, tiempo_hc, solucion_hc[2] == 0))

        # Genetic Algorithm
        start_time = time.time()
        solucion_ga, estados_visitados_ga = genetic(n_reinas, max_iterations)
        tiempo_ga = time.time() - start_time
        es_optimo = h_reinas(solucion_ga, n_reinas) == 0
        resultados['Genetic Algorithm'].append((estados_visitados_ga, tiempo_ga, es_optimo))

    return resultados


# Guardar resultados en CSV
def guardar_resultados_csv(resultados, n_reinas):
    with open(f'resultados_{n_reinas}_reinas.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Algoritmo", "Iteración", "Estados Visitados", "Tiempos", "Solución Óptima"])

        for alg, data in resultados.items():
            for i, (estados, tiempo, es_optimo) in enumerate(data):
                writer.writerow([alg, i + 1, estados, tiempo, es_optimo])


# Calcular estadísticas y graficar una única gráfica de caja y bigotes para estados visitados
def graficar_boxplot_estados(resultados, n_reinas):
    estados_por_algoritmo = [[dato[0] for dato in resultados[alg]] for alg in resultados]
    nombres_algoritmos = list(resultados.keys())

    plt.figure(figsize=(10, 6))
    plt.boxplot(estados_por_algoritmo, tick_labels=nombres_algoritmos)
    plt.title(f"Distribución de Estados Visitados para {n_reinas} Reinas")
    plt.ylabel("Cantidad de Estados Visitados")
    plt.xlabel("Algoritmo")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(f"boxplot_estados_{n_reinas}_reinas.png")
    plt.close()


# Calcular estadísticas y graficar una única gráfica de caja y bigotes para tiempos de ejecución
def graficar_boxplot_tiempos(resultados, n_reinas):
    tiempos_por_algoritmo = [[dato[1] for dato in resultados[alg]] for alg in resultados]
    nombres_algoritmos = list(resultados.keys())

    plt.figure(figsize=(10, 6))
    plt.boxplot(tiempos_por_algoritmo, tick_labels=nombres_algoritmos)
    plt.title(f"Distribución de Tiempos de Ejecución para {n_reinas} Reinas")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.xlabel("Algoritmo")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(f"boxplot_tiempos_{n_reinas}_reinas.png")
    plt.close()


# Graficar promedios de soluciones óptimas
def graficar_promedio_soluciones_optimas(tamanos, promedios):
    plt.figure(figsize=(10, 6))

    # Graficar cada algoritmo
    for alg, promedios_alg in promedios.items():
        plt.plot(tamanos, promedios_alg, marker='o', linestyle='-', label=alg)

    plt.title("Promedio de Soluciones Óptimas por Tamaño de N Reinas")
    plt.xlabel("Número de Reinas")
    plt.ylabel("Promedio de Soluciones Óptimas")
    plt.xticks(tamanos)
    plt.grid(True)
    plt.legend()
    plt.savefig("promedio_soluciones_optimas.png")
    plt.close()


# Ejecución para 4, 8 y 10 reinas
tamanos_reinas = [4, 8, 10]
promedios_soluciones_optimas = {alg: [] for alg in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm']}

for n in tamanos_reinas:
    resultados = ejecutar_algoritmos(n, 30, 1000)
    guardar_resultados_csv(resultados, n)
    graficar_boxplot_estados(resultados, n)
    graficar_boxplot_tiempos(resultados, n)

    # Calcular promedio de soluciones óptimas
    for alg in promedios_soluciones_optimas.keys():
        conteo_optimos = sum(1 for _, _, es_optimo in resultados[alg] if es_optimo)
        promedio_optimos = conteo_optimos / 30
        promedios_soluciones_optimas[alg].append(promedio_optimos)

# Graficar promedios de soluciones óptimas
graficar_promedio_soluciones_optimas(tamanos_reinas, promedios_soluciones_optimas)
