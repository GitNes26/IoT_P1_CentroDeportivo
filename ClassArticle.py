import json
import ConexionMySQL
import ConexionMongoDB

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
    for la in self.ListaArticulos:
      self.data['ListaArticulos'].append(encoderArticulo(la))
      with open('dataArticulos.json', 'w') as file:
        json.dump(self.data, file, indent=4)
    return newArticulo
  
  def VerArticulos(self):
    return self.ListaArticulos

  def ValidarDatosArticulo(self, articulo,cantidad, mydb,dbs):
    lista = mydb.Mostrar('articulos')
    if dbs == '-MySQL-':
      x = 0
      y = 2
    else:
      x = 'id'
      y = 'inventario'
    for a in lista:
      if articulo == a[x]:
        if int(a[y]) > 0:
          if cantidad <= int(a[y]):
            return True
          else: print("| Prestamo Rechazado|No se tiene la cantidad suficiente del articulo")
        else: print("| Prestamo Rechazado|Articulo solicitado agotado")
        break
    else: print("| Prestamo Rechazado|El articulo solicitado no existe")
  
  def CantidadInventario(self, articulo, cantidad, mydb,dbs):
    lista = mydb.Mostrar('articulos')
    if dbs == '-MySQL-':
      x = 0
      y = 2
    else:
      x = 'id'
      y = 'inventario'
    for a in lista:
      if articulo == a[x]:
        inv = int(a[y]) + cantidad
        mydb.Actualizar(tabla='articulos', campoSet='inventario',valorSet=inv,
        campoWhere='id', condicional='=',valorWhere=articulo)
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