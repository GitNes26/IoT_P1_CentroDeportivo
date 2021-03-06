import json

class Articulo:
  idd = 0
  ListaArticulos = []
  data = {}
  data['ListaArticulos'] = []

  def __init__(self, Id=None, articulo=None, inventario=None, bandera=0):
    self.Id             = Id
    self.articulo       = articulo
    self.inventario     = inventario
    self.bandera = 0
    if bandera == 1:
      with open('dataArticulos.json') as f:
        listillaJSON = json.load(f)
        for li in listillaJSON['ListaArticulos']:
          newArticulo = Articulo(li['Id'],li['articulo'],li['inventario'])
          self.ListaArticulos.append(newArticulo)
          self.idd = li['Id']

  def RegistroArticulo(self, articulo, inventario):
    self.idd += 1
    newArticulo = Articulo(self.idd, articulo, inventario)
    self.ListaArticulos.append(newArticulo)
    for la in self.ListaArticulose:
      self.data['ListaArticulos'].append(encoderArticulo(la))
      with open('dataArticulos.json', 'w') as file:
        json.dump(self.data, file, indent=4)
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

def encoderArticulo(articulo):
  if isinstance(articulo,Articulo):
    return {
      'Id'         : articulo.Id,
      'articulo'   : articulo.articulo,
      'inventario' : articulo.inventario
    }
  raise TypeError(f'El objeto {articulo} no es de tipo Persona')