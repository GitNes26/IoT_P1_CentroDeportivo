class Persona:
  idd = 0
  ListaMiembros = []

  def __init__(self, Id=None, name=None, email=None, cel=None):
    self.Id    = Id
    self.name  = name
    self.email = email
    self.cel   = cel
    self.prestamos  = 3
  
  def RegistroPersona(self, nombre, correo, cel):
    self.idd += 1
    newMiembro = Persona( self.idd, nombre, correo, cel)
    self.ListaMiembros.append(newMiembro)
    return newMiembro
  
  def VerPersonas(self):
    return self.ListaMiembros

  def ValidarDatosPersona(self, miembro):
    for m in self.ListaMiembros:
      if miembro == m.Id:
        if m.prestamos > 0:
          return True
        else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
        break
    return print("| Prestamo Rechazado|Miembro no registrado")

  def PrestamosDisponibles(self, miembro, prestamosD):
    for m in self.ListaMiembros:
      if miembro == m.Id:
        m.prestamos += prestamosD
        return True
    return False