def prim_mst(graph):
    """
    Algoritmo de Prim para encontrar el Árbol de Expansión Mínima.
    """
    N = len(graph)
    selected = [False] * N
    mst_edges = []
    selected[0] = True

    for _ in range(N - 1):
        min_weight = float('inf')
        edge = (-1, -1)

        for i in range(N):
            if selected[i]:
                for j in range(N):
                    if not selected[j] and 0 < graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        edge = (i, j)

        if edge != (-1, -1):
            mst_edges.append(edge)
            selected[edge[1]] = True

    return [(chr(65 + u), chr(65 + v)) for u, v in mst_edges]
