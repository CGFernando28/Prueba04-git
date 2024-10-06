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

<<<<<<< HEAD
=======
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

a, b = 0, 1

while a < 100:
    print(a, end=' ')
    a, b = b, a+b
>>>>>>> quinto
