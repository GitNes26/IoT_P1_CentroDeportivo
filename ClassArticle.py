class Articulo:
  idd = 0
  ListaArticulos = []

  def __init__(self, Id=None, articulo=None, inventario=None):
    self.Id             = Id
    self.articulo       = articulo
    self.inventario     = inventario
    # self.ListaArticulos = [
    #   '''{"Id":'1',
    #    "articulo":'Balon de Futbol',
    #    "inventario":50
    #   },
    #   {
    #    "Id":'2',
    #    "articulo":'Balon de Basketbol',
    #    "inventario":30
    #   }'''
    # ]

  def RegistroArticulo(self, articulo, inventario):
    self.idd += 1
    newArticulo = Articulo(self.idd, articulo, inventario)
    self.ListaArticulos.append(newArticulo)
    return newArticulo
  
  def VerArticulos(self):
    return self.ListaArticulos

  def ValidarDatosArticulo(self, articulo,cantidad):
    for a in self.ListaArticulos:
      if articulo == a.Id:
        if a.inventario > 0:
          if cantidad <= a.inventario:
            return True
          else: print("| Prestamo Rechazado|No se tiene la cantidad suficiente del articulo")
        else: print("| Prestamo Rechazado|Articulo solicitado agotado")
        break
    else: print("| Prestamo Rechazado|El articulo solicitado no existe")
  
  def CantidadInventario(self, articulo, cantidad):
    for a in self.ListaArticulos:
      if articulo == a.Id:
        a.inventario += cantidad
        return True
      break