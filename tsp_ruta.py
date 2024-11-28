from itertools import permutations

def tsp(graph):
    """
    Algoritmo para encontrar la ruta más corta en un grafo completo (TSP).
    """
    N = len(graph)
    min_dist = float('inf')
    best_route = []

    for perm in permutations(range(N)):
        current_dist = 0
        for i in range(N - 1):
            current_dist += graph[perm[i]][perm[i + 1]]
        current_dist += graph[perm[-1]][perm[0]]  # Regresar al inicio

        if current_dist < min_dist:
            min_dist = current_dist
            best_route = perm

    # Convertir a formato de letras
    best_route_letters = [chr(65 + node) for node in best_route]
    return min_dist, best_route_letters


