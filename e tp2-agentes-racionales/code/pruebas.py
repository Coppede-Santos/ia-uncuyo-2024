
from environment import *
from agenteAleatorio import*
import csv

def run_simulation(sizeX, sizeY, dirt_rate, num_iterations=1000):
    env = Environment(sizeX, sizeY, random.randint(0, sizeX-1), random.randint(0, sizeY-1), dirt_rate)
    agent = AgentAle(env)
    #env.print_enviroment()
    for _ in range(num_iterations):
        agent.think()
    
    # Medir el desempeño
    cleaned = env.get_performance()  # Celdas limpias
    print("--------------------------------",cleaned)
    return cleaned

# Parámetros de simulación
sizes = [2, 4, 8, 16, 32, 64, 128]
#sizes= [2]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
num_repeats = 10
num_iterations = 1000

# Guardar resultados en un archivo CSV
with open("resultados_simulacion.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tamaño", "Porcentaje de Suciedad", "Promedio Celdas Limpias", "Porcentaje Celdas Limpias"])

    # Realizar simulaciones y guardar los resultados en el archivo
    for size in sizes:
        for dirt_rate in dirt_rates:
            total_cleaned = 0  # Para acumular el total de celdas limpias en las repeticiones
            total_cells = size * size  # Número total de celdas en el entorno
            print(f"Tamaño: {size}x{size}, Porcentaje de Suciedad: {dirt_rate}")
            
            for repeat in range(num_repeats):
                cleaned = run_simulation(size, size, dirt_rate, num_iterations)
                total_cleaned += cleaned
                print(f"  Repetición {repeat + 1}: Celdas Limpias = {cleaned}")
            
            # Calcular promedio y porcentaje
            average_cleaned = total_cleaned / num_repeats
            percentage_cleaned = (average_cleaned / total_cells) * 100
            
            print(f"Promedio de Celdas Limpias: {average_cleaned}")
            print(f"Porcentaje de Celdas Limpias: {percentage_cleaned:.2f}%\n")
            
            # Guardar en el archivo CSV
            writer.writerow([f"{size}x{size}", dirt_rate, average_cleaned, percentage_cleaned])