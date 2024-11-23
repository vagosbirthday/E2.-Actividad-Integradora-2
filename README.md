# Optimizador de Redes y Logística Urbana

## Descripción  
Este proyecto en Python proporciona una solución integral para optimizar la infraestructura y los servicios en redes de colonias urbanas. Diseñado para una empresa que incursiona en los servicios de Internet, aborda problemas clave relacionados con:  
- Planificación del cableado de fibra óptica.  
- Logística de distribución.  
- Eficiencia en la transmisión de datos.  
- Asignación geográfica de recursos.  

El sistema implementa algoritmos avanzados como **Kruskal**, **Edmonds-Karp** y el cálculo del **Diagrama de Voronoi** para resolver problemas de grafos y optimización, facilitando decisiones estratégicas basadas en datos geográficos y capacidades de red.  

---

## Características  
### 1. Cableado Óptimo de Fibra Óptica  
Determina la forma más eficiente de conectar todas las colonias utilizando un **Árbol de Expansión Mínima (MST)**.  

### 2. Logística de Correspondencia  
Calcula la **ruta más corta** para visitar todas las colonias y regresar al origen, optimizando el reparto de correspondencia y notificaciones.  

### 3. Flujo Máximo de Información  
Evalúa la capacidad máxima de transmisión de datos entre colonias, considerando interferencias electromagnéticas.  

### 4. Asignación Geográfica de Centrales  
Genera un **Diagrama de Voronoi** para asignar la central más cercana a nuevas contrataciones del servicio.  

---

## Entrada  
El programa requiere:  
1. Matriz de distancias entre colonias.  
2. Matriz de capacidades máximas de transmisión de datos.  
3. Coordenadas geográficas de las centrales en formato `(x, y)`.  
