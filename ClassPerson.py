class Persona:
    def __init__(self, Id=None, name=None, email=None, cel=None):
      self.Id = Id
      self.name  = name
      self.email = email
      self.cel   = cel
      self.ListaMiembros = []
      # prestamos  : int
    
    def __init__(self):
      self.ListaMiembros = []
    
    def RegistrarMiembro(self, Id, nombre, correo, cel):
      newMiembro = Persona(Id, nombre, correo, cel)
      # newMiembro.prestamos = 3
      self.ListaMiembros.append(newMiembro)
      return newMiembro
