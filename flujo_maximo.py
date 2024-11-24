# Codigo sacado de https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

#Modificado y adaptado por: Daniel Aguilar

from collections import deque

class FlujoMaximo:
    def __init__(self, n, capacidad):
        # Inicializa el problema del flujo máximo.
        # para n: Número de nodos en el grafo.
        # para capacidad: Matriz de capacidades (ancho de banda).
        
        self.n = n
        self.capacidad = capacidad
        self.grafo_residual = [fila[:] for fila in capacidad]  # Inicializa el grafo residual con las capacidades originales

    def bfs(self, fuente, sumidero, padres):
        #Realiza una búsqueda en anchura (BFS) para encontrar un camino desde la fuente al sumidero.
        # para fuente: Nodo inicial.
        # para sumidero: Nodo final.
        # para padres: Arreglo para rastrear el camino.
        # return: True si existe un camino, False en caso contrario.
        
        visitado = [False] * self.n
        cola = deque([fuente])
        visitado[fuente] = True

        while cola:
            nodo = cola.popleft()
            for vecino in range(self.n):
                if not visitado[vecino] and self.grafo_residual[nodo][vecino] > 0:
                    cola.append(vecino)
                    visitado[vecino] = True
                    padres[vecino] = nodo
                    if vecino == sumidero:
                        return True
        return False

    def calcular_flujo_maximo(self, fuente, sumidero):
        #Calcula el flujo máximo desde la fuente hasta el sumidero.
        # para fuente: Nodo fuente (0-indexado).
        # para sumidero: Nodo sumidero (0-indexado).
        # return: El flujo máximo total.

        padres = [-1] * self.n
        flujo_maximo = 0

        while self.bfs(fuente, sumidero, padres):
            # Encuentra el flujo mínimo a lo largo del camino encontrado
            flujo_caminante = float('Inf')
            nodo_actual = sumidero
            while nodo_actual != fuente:
                flujo_caminante = min(flujo_caminante, self.grafo_residual[padres[nodo_actual]][nodo_actual])
                nodo_actual = padres[nodo_actual]

            # Actualiza capacidades en el grafo residual
            nodo_actual = sumidero
            while nodo_actual != fuente:
                anterior = padres[nodo_actual]
                self.grafo_residual[anterior][nodo_actual] -= flujo_caminante
                self.grafo_residual[nodo_actual][anterior] += flujo_caminante
                nodo_actual = anterior

            flujo_maximo += flujo_caminante

        return flujo_maximo
