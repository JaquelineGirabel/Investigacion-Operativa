from Grafo import Grafo
from Dijkstra import Dijkstra
import math

#La función camino_minimo recibe por input vertices s y v de un grafo conexo pesado dado,
#y un diccionario D conteniendo, por cada vertice en el grafo, su predecesor en el camino minimo a s y la distancia a s.
#Devuelve el camino minimo de s a v.

def camino_minimo(s, v, D):
  camino=[v]
  predecesor=D[v][0]
  while predecesor != s:
    camino.append(predecesor)
    predecesor=D[predecesor][0]
  if v!= s:
    camino.append(s)
  camino.reverse()
  return camino


#Recibe por input una lista de tuplas de dos coordenadas (entrada, salida) o de tres coordenadas (entrada, salida, peso),
#representando las conexiones de un nodo central con el resto de los nodos. 
#Devuelve la ruta de conexiones más segura desde el nodo central a cada uno del resto de los nodos.

def rutas_seguras(lista_aristas):
  G=Grafo()
  G.agregar_lista_aristas(lista_aristas)
  G_aux=Grafo() # G_aux es el grafo que se obtiene del grafo G de entrada cambiando el peso w de cada arista por -log(w)
  for vertice in G.vertices:
    G_aux.vertices.add(vertice)
  for vertice in G.lista_adyacencia:
    vecinos_aux=set()
    for arista in G.lista_adyacencia[vertice]:
      nueva_arista=(arista[0], -math.log(arista[1]))
      vecinos_aux.add(nueva_arista)
    G_aux.lista_adyacencia[vertice]=vecinos_aux
  D = Dijkstra(0, G_aux) # D es el diccionario obtenido con el algoritmo de Dijkstra,
  #cuyos elementos son de la forma (vertice, predecesor, distancia a 0) aplicado a G_aux
  Caminos=dict()
  for vertice in D:
    Caminos[vertice]=camino_minimo(0, vertice, D)
  for vertice in D:
    print (vertice, Caminos[vertice], math.exp(-D[vertice][1]))




rutas_seguras([(0, 1, 0.9), (0, 2, 0.95), (1, 2, 0.8), (1, 3, 0.9), (3, 1, 0.99), (2, 3, 0.85)])

