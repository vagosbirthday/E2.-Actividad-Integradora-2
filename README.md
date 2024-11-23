# Optimizador de Redes y Logística Urbana

## Descripción  
Este proyecto en Python proporciona una solución integral para optimizar la infraestructura y los servicios en redes de colonias urbanas. Diseñado para una empresa que incursiona en los servicios de Internet, aborda problemas clave relacionados con:  
- Planificación del cableado de fibra óptica.  
- Logística de distribución.  
- Eficiencia en la transmisión de datos.  
- Asignación geográfica de recursos.  

---

## Entrada  
El programa requiere:  
1. Matriz de distancias entre colonias.  
2. Matriz de capacidades máximas de transmisión de datos.  
3. Coordenadas geográficas de las centrales en formato `(x, y)`.  


### Explicacion de entradas

#### **Primer entrada**

Se pide el numero de colonias que existe, (e.g. 4)

#### **Segunda entrada**

Matriz de distancias entre colonias

Cada linea de la matriz representa la distancia desde el punto de origen hasta los demas nodos, en el ejemplo

0  16 45 32
16  0 18 21
45 18  0  7
32 21  7  0

para ir del "pueblo 0" al "pueblo 1", la distancia es 16 kilometros
para ir del "pueblo 0" al "pueblo 2", la distancia es 45 kilometros
para ir del "pueblo 0" al "pueblo 3", la distancia es 32 kilometros

de igual manera, si quieres ir del "pueblo 2" al "pueblo 0" [0,2], la distancia es 45 kilometros, representado en la matriz [2,0]

Naturalmente esta matriz es simetrica ya que las distancias entre pueblo y pueblo son las mismas

#### **Tercer entrada**

Matriz de maxima trasmision de datos entre colonias (capacidad de banda ancha entre colonias)

El problema, al estar relacionado tambien con servicio de internet, aparte de la cantidad necesaria de fibra optica para conectar los pueblos, tambien es necesario conocer el ancho de banda entre los pueblos, este no necesariamente debe de ser simetrico

Ejemplo:

0  48 12 18
52  0 42 32
18 46  0 56
24 36 52  0

Entonces sabemos que para llegar del "pueblo 0" al "pueblo 1", la distancia es 16 kilometros y la cantidad de informacion que pueden intercambiar es de 48

#### **Cuarta entrada**

Solamente se piden pares de coordenadas X y Y para la cantidad de pueblos que se puso en la primer entrada

En este caso, para n = 4, se requieren 4 sets de coordenadas

se deben de ingresar de esta manera

200,500
300,100
450,150
520,480




#TODO 

### Punto Numero 1
    [] Encontrar la distribucion optima para conectar colonioas con fibra optica (Algoritmo MST)

### Punto Numero 2
    [] Implementacion del algoritmo del comerciante (problema del viajante), Algoritmo TSP

### Punto Numero 3
    [] Implementacion de algoritmo de flujo maximo de informacion del nodo inicial al nodo final (Flujo Máximo)
    [] Preguntar a betty como implementar este algoritmo, si es necesario que todas las colonias se puedan interconectar y si es necesario especificar nodo de inicio y nodo final.
 
    Requerimientos
    Se debe de especificar nodo inicial y nodo final

### Punto Numero 4
    [] Determinar que central esta mas cerca de una nueva casa (Geometria computacional)

### Salida

#### **Primer salida**

Lista del orden en el cual se deben de conectar las colonias (A,B,C)

#### **Segunda salida**

Salida del algoritmo de el algoritmo TSP

#### **Tercer salida**

lista de poligonos
    [] Preguntar a betty con que se refiere a esto

