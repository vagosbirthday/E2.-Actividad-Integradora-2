from collections import deque

def bfs(capacity, source, sink, parent):
    """
    BFS para encontrar el camino aumentante.
    """
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, cap in enumerate(capacity[u]):
            if not visited[v] and cap > 0:
                parent[v] = u
                visited[v] = True
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmonds_karp(capacity, source, sink):
    """
    Algoritmo de Edmonds-Karp para encontrar el flujo máximo.
    """
    parent = [-1] * len(capacity)
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

