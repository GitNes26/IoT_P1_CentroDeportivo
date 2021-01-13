import ClassPerson as P
import ClassArticle as A 

class Prestamo:
    def __init__(self, folio, miembro, articulo, cantidad, fPrestamo):
        self.folio     = folio
        self.miembro   = miembro
        self.articulo  = articulo
        self.cantidad  = cantidad
        self.fPrestamo = fPrestamo
        devuelto       : bool
        fDevolucion    : str
    
    def __init__(self):
      self.Prestamos = []

    def RegistrarPrestamo(folio, miembro, articulo, cantidad, fecha):
        newPrestamo = Prestamo(folio, miembro, articulo, cantidad, fecha)
        newPrestamo.devuelto = False
        newPrestamo.fDevolucion = ""
        Prestamos.append(newPrestamo)
        for p in Prestamos:
            if folio == p.folio:
                return Prestamo