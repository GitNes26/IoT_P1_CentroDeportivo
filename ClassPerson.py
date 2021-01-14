ListaMiembros = []

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

    def ValidarPrestamoMiembro(self, miembro):
      for m in ListaMiembros:
        if miembro in m.Id:
          if m.prestamos > 0:
            return
          else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
          break
      return print("| Prestamo Rechazado|Miembro no registrado")

    def PrestamosDisponibles(self, miembro, n):
      for m in ListaMiembros:
        if miembro in m.Id:
          m.prestamos += n
          break
       