Este proyecto en Python proporciona una solución integral para optimizar la infraestructura y los servicios en redes de colonias urbanas. Diseñado para una empresa que incursiona en los servicios de Internet, aborda problemas clave relacionados con la planificación del cableado de fibra óptica, la logística de distribución, la eficiencia en la transmisión de datos y la asignación geográfica de recursos.

El sistema implementa algoritmos avanzados como Kruskal, Edmonds-Karp y el cálculo del Diagrama de Voronoi para resolver problemas de grafos y optimización, facilitando decisiones estratégicas con base en datos geográficos y de capacidad de red.

Características:

Cableado Óptimo de Fibra Óptica: Determina la forma más eficiente de conectar todas las colonias con fibra óptica usando un Árbol de Expansión Mínima (MST).
Logística de Correspondencia: Calcula la ruta más corta para visitar todas las colonias y regresar al origen, optimizando el reparto de estados de cuenta y notificaciones.
Flujo Máximo de Información: Evalúa la capacidad máxima de transmisión de datos entre colonias considerando interferencias electromagnéticas.
Asignación Geográfica de Centrales: Genera un Diagrama de Voronoi para asignar la central más cercana a nuevas contrataciones del servicio.
Entrada:

Matriz de distancias entre colonias.
Matriz de capacidades máximas de transmisión de datos.
Coordenadas geográficas de las centrales.
Salida:

Lista de conexiones óptimas de fibra óptica (MST).
Ruta más corta para logística (TSP).
Valor de flujo máximo entre colonias.
Visualización del Diagrama de Voronoi.
Tecnologías Usadas:

Python
NetworkX (para grafos y algoritmos de flujo)
SciPy/Matplotlib (para el cálculo y visualización del Diagrama de Voronoi)
