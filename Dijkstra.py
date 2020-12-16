import math
from grafo import Grafo


#Recibe por input un grafo conexo de tipo Grafo y un vertice distinguido en él, s.
#Devuelve un diccionario donde por cada vértice v se tiene un par ordenado (predecesor de v, distancia de v a s).

def Dijkstra(s, grafo):
  V =[s] + [x for x in grafo.vertices if x!=s] # V es la lista de todos los vertices, empezando en s.
  S = set()
  P=dict() # P será un diccionario conteniendo los predecesores
  dist=dict() # list será un diccionario conteniendo las distancias
  P[s]=s
  dist[s]=0
  for vertice in V[1:len(V)]:
    P[vertice]=s
    dist[vertice]=math.inf
  dist_aux=dist.copy() # list_aux será un diccionario auxiliar conteniendo las distancias de los vertices que no están en S
  while len(S) < len(V):
    visitado = min(dist_aux, key=lambda vertice: dist_aux[vertice]) #visito el vertice de distancia minima que no está en S
    S.add(visitado)
    vecinos = [v for v in grafo.vecinos_con_peso(visitado) if v[0] not in S]
    if len(vecinos) > 0:
      #para cada vecino del nodo "visitado", comparo su distancia a s con la distancia obtenida pasando por "visitado", y actualizo
      for v in vecinos:
        vertice=v[0]
        peso = v[1]
        if dist[vertice] > dist[visitado] + peso:
          dist[vertice] = dist[visitado] + peso
          dist_aux[vertice]=dist_aux[visitado] + peso
          P[vertice]=visitado 
    dist_aux.pop(visitado)
  D = dict()
  for vertice in V:
    D[vertice] = (P[vertice], dist[vertice])
  return D
