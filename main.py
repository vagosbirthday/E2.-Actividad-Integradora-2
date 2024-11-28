import prim_cableado
import tsp_ruta
import flujo_maximo
import cercania_central

def validate_input(prompt, validator):
    """
    Corutina para validar entradas de datos.
    """
    while True:
        value = input(prompt).strip()
        try:
            if validator(value):
                yield value
                return
        except Exception as e:
            print(f"Error: {e}. Por favor, inténtelo de nuevo.")
            continue

def ingresar_datos():
    print("=== Ingreso de Datos ===")

    # Validar número de colonias
    validator_n = lambda x: x.isdigit() and int(x) > 0
    n_colonias = int(next(validate_input("Ingrese el número de colonias (N): ", validator_n)))

    # Validar matriz de distancias
    print("\nIngrese la matriz de distancias entre colonias (N x N):")
    distancias = []
    for i in range(n_colonias):
        validator_row = lambda x: len(list(map(int, x.split()))) == n_colonias
        fila = list(map(int, next(validate_input(f"Fila {i + 1}: ", validator_row)).split()))
        distancias.append(fila)

    # Validar matriz de capacidades
    print("\nIngrese la matriz de capacidades de transmisión de datos (N x N):")
    capacidades = []
    for i in range(n_colonias):
        validator_row = lambda x: len(list(map(int, x.split()))) == n_colonias
        fila = list(map(int, next(validate_input(f"Fila {i + 1}: ", validator_row)).split()))
        capacidades.append(fila)

    # Validar coordenadas de centrales
    print("\nIngrese las coordenadas de las centrales en formato (x, y):")
    centrales = []
    for i in range(n_colonias):
        validator_coords = lambda x: len(list(map(int, x.split()))) == 2
        coords = tuple(map(int, next(validate_input(f"Central {i + 1}: ", validator_coords)).split()))
        centrales.append(coords)

    return n_colonias, distancias, capacidades, centrales

def main():
    print("Bienvenido al sistema de planificación de red de colonias.\n")

    # Ingresar datos con validación
    n_colonias, distancias, capacidades, centrales = ingresar_datos()

    print("\n=== Resultado ===")

    # 1. Forma óptima de cablear con fibra
    print("\n1. Forma de cablear las colonias con fibra:")
    fibra_optica = prim_cableado.prim_mst(distancias)
    print(fibra_optica)

    # 2. Ruta más corta para visitar cada colonia (TSP)
    print("\n2. Ruta más corta para repartir correspondencia:")
    distancia, ruta = tsp_ruta.tsp(distancias)
    print(f"Ruta: {' -> '.join(ruta)}, Distancia total: {distancia}")

    # 3. Flujo máximo de información
    print("\n3. Flujo máximo de información:")
    flujo_max = flujo_maximo.edmonds_karp(capacidades, 0, n_colonias - 1)
    print(f"Flujo máximo: {flujo_max}")

    # 4. Central más cercana para nuevas contrataciones
    print("\n4. Central más cercana a una nueva contratación:")
    validator_coords = lambda x: len(list(map(int, x.split()))) == 2
    coords = tuple(map(int, next(validate_input("Ingrese la ubicación de la nueva contratación (x, y): ", validator_coords)).split()))
    central_cercana = cercania_central.closest_central(centrales, coords)
    print(f"Central más cercana: {central_cercana}")

if __name__ == "__main__":
    main()
