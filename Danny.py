import numpy as np
from itertools import permutations

# --------------------------------------------------------
# Funciones para Recolección de Datos de Entrada
# --------------------------------------------------------

def obtener_entrada_numero(mensaje, rango=None):
    
    #Función para obtener un número con validación. Si se proporciona un rango,
    #verifica que el número esté dentro de ese rango.

    while True:
        try:
            valor = int(input(mensaje))
            if rango and (valor < rango[0] or valor > rango[1]):
                print(f"Por favor ingrese un valor entre {rango[0]} y {rango[1]}")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

def obtener_entrada_matriz(mensaje, tamaño):

    #Función para obtener una matriz cuadrada con validación.

    matriz = []
    print(mensaje)
    for i in range(tamaño):
        while True:
            try:
                fila = list(map(int, input(f"Ingrese la fila {i+1} de la matriz: ").split()))
                if len(fila) != tamaño:
                    print(f"La fila debe tener {tamaño} elementos.")
                    continue
                matriz.append(fila)
                break
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números enteros.")
    return matriz

def obtener_entrada_coordenadas(tamaño):
    
    #Función para obtener las coordenadas de las centrales con validación.

    coordenadas = []
    for i in range(tamaño):
        while True:
            try:
                x, y = map(int, input(f"Ingrese las coordenadas de la central {i+1} (x,y): ").split(','))
                coordenadas.append((x, y))
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese las coordenadas en formato x,y.")
    return coordenadas

# --------------------------------------------------------
# Función Principal
# --------------------------------------------------------

def main():
    """
    Función principal que integra todas las funcionalidades:
    1. Lectura de datos con validación.
    2. Mostrar los datos ingresados.
    """
    # Leer entrada
    num_colonias = obtener_entrada_numero("Número de colonias (ej. 4): ", rango=(1, 100))
    
    # Matriz de distancias entre colonias
    matriz_distancias = obtener_entrada_matriz("Ingrese las distancias entre colonias (grafo ponderado): ", num_colonias)
    
    # Coordenadas de las centrales
    coordenadas_centrales = obtener_entrada_coordenadas(num_colonias)
    
    # Mostrar los datos recolectados
    print("\nDatos recolectados:")
    print(f"Número de colonias: {num_colonias}")
    
    print("\nMatriz de distancias entre colonias:")
    for fila in matriz_distancias:
        print(fila)
    
    print("\nCoordenadas de las centrales:")
    for i, coord in enumerate(coordenadas_centrales):
        print(f"Central {i+1}: {coord}")

# Ejecutamos el programa
main()
