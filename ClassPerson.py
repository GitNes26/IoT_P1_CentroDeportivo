ListaMiembros = []
idL = 0

class Persona:

    def __init__(self, Id=None, name=None, email=None, cel=None):
      self.Id    = Id
      self.name  = name
      self.email = email
      self.cel   = cel
      self.prestamos  = 3
    
    def RegistroPersona(self, Id, nombre, correo, cel):
      newMiembro = Persona( Id, nombre, correo, cel)
      ListaMiembros.append(newMiembro)
      return newMiembro
    
    def VerPersonas(self):
      return ListaMiembros

    def ValidarDatosPrestamo(self, miembro):
      pase=False
      for m in ListaMiembros:
        if miembro == m.Id:
          if m.prestamos > 0:
            pase=True
            return
          else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
          break
      return pase #, print("| Prestamo Rechazado|Miembro no registrado"))

    def PrestamosDisponibles(self, miembro, n):
      for m in ListaMiembros:
        if miembro == m.Id:
          m.prestamos += n
          return
       