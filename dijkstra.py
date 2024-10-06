import tkinter as tk
from tkinter import messagebox
import heapq
print("Hola mundo esto es un algoritmo dijkstra")
print("esto es un prueba 1 de creador")

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def calculate_shortest_path():
    try:
        start_node = entry_start.get()
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

        shortest_distances = dijkstra(graph, start_node)
        result = "\n".join([f"Distancia a {node}: {distance}" for node, distance in shortest_distances.items()])
        messagebox.showinfo("Resultados", result)

    except KeyError:
        messagebox.showerror("Error", "Nodo de inicio no válido. Usa A, B, C o D.")



# Inicia la aplicación
root.mainloop()
