class Grafo:  

  ## Representacion de un grafo por lista de adyacencia ##

  def __init__(self):
    self.lista_adyacencia = {}
    self.vertices = set()
    
  def agregar_vertice(self,vertice):
    self.vertices.add(vertice)
    
  def cantidad_de_vertices(self):
    return len(self.vertices)

  def vecinos_con_peso(self,vertice):
    if vertice not in self.lista_adyacencia:
      return set()
    else:
      return self.lista_adyacencia[vertice]

  def vecinos(self,vertice):
    if vertice not in self.lista_adyacencia:
      return set()
    else:
      return {u[0] for u in self.lista_adyacencia[vertice]}

  def agregar_arista(self,arista): 
    peso = 1
    if len(arista) == 3:
      salida,llegada,peso = arista
    elif len(arista) == 2:
      salida,llegada = arista
    else:
      print("Uso invalido. Ingresar [salida,llegada,peso]")
    self.vertices.add(salida)
    self.vertices.add(llegada)
    if salida not in self.lista_adyacencia:
      self.lista_adyacencia[salida] = set()
    self.lista_adyacencia[salida].add((llegada,peso))

  def agregar_lista_aristas(self,lista_aristas):
    for arista in lista_aristas:
      self.agregar_arista(arista)
