import json
import ConexionMySQL
import ConexionMongoDB

# mydb = mysqlDB
# listaPersonas = Interface.ListaMiembros

class Persona:
  idd = 0
  ListaMiembros = []
  # data = {}
  # data['ListaMiembros'] = []

  def __init__(self, Id=None, name=None, email=None, cel=None, prestamo=None, bandera=0):
    self.Id    = Id
    self.name  = name
    self.email = email
    self.cel   = cel
    self.prestamos  = 3
    # self.bandera = 0
    # if bandera == 1:
    #   with open('dataPersonas.json') as f:
    #     listillaJSON = json.load(f)
    #     for li in listillaJSON['ListaMiembros']:
    #       newMiembro = Persona(li['Id'],li['name'],li['email'],li['cel'],li['prestamos'])
    #       self.ListaMiembros.append(newMiembro)
    #       self.idd = li['Id']
  
  def RegistroPersona(self, nombre, correo, cel):
    u=0
    # self.idd += 1
    newMiembro = Persona(nombre, correo, cel)
    self.ListaMiembros.append(newMiembro)
    # mysqlDB.Insertar('miembros', name=newMiembro.name, email=newMiembro.email, cel=newMiembro.cel)
    # self.data['ListaMiembros'].append(encoderPersona(newMiembro))
    # with open('dataPersonas.json','w') as f:
    #   json.dump(self.data,f,indent=4)
    #   # for la in self.ListaMiembros:
    #     # self.idd = la.Id
    # for lp in self.ListaMiembros:
    #   self.data['ListaMiembros'].append(encoderPersona(lp))
    #   with open('dataPersonas.json', 'w') as file:
    #     json.dump(self.data, file, indent=4)
    #     self.idd = lp.Id

    return newMiembro
  
  def VerPersonas(self):
    # return listaPersonas
    return self.ListaMiembros

  def ValidarDatosPersona(self, miembro, mydb,dbs):
    lista = mydb.Mostrar('miembros')
    if dbs == '-MySQL-':
      x = 0
      y = 4
    else:
      x = 'id'
      y = 'prestamos'
    for m in lista:
      if miembro == m[x]:
        if int(m[y]) > 0:
          return True
        else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
        break
    return print("| Prestamo Rechazado|Miembro no registrado")

  def PrestamosDisponibles(self, miembro, prestamosD, mydb,dbs):
    lista = mydb.Mostrar('miembros')
    if dbs == '-MySQL-':
      x = 0
      y = 4
    else:
      x = 'id'
      y = 'prestamos'
    for m in lista:
      if miembro == m[x]:
        pd = int(m[y]) + prestamosD
        mydb.Actualizar(tabla='miembros', campoSet='prestamos',valorSet=pd,
        campoWhere='id', condicional='=',valorWhere=miembro)
        return True
    return False



def encoderPersona(persona):
  if isinstance(persona,Persona):
    return {
      'Id'        : persona.Id,
      'name'      : persona.name,
      'email'     : persona.email,
      'cel'       : persona.cel,
      'prestamos' : 3
    }
  raise TypeError(f'El objeto {persona} no es de tipo Persona')