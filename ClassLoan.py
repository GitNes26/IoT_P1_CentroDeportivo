import ClassPerson as P
import ClassArticle as A 

ListaPrestamos = []

class Prestamo:
    def __init__(self, folio=None, miembro=None, articulo=None, cantidad=None, fPrestamo=None):
        self.folio     = folio
        self.miembro   = miembro
        self.articulo  = articulo
        self.cantidad  = cantidad
        self.fPrestamo = fPrestamo
        self.devuelto       = False
        self.fDevolucion    = None

    def RegistroPrestamo(self, folio, miembro, articulo, cantidad, fecha):
        newPrestamo = Prestamo(folio, miembro, articulo, cantidad, fecha)
        ListaPrestamos.append(newPrestamo)
        for p in ListaPrestamos:
            if folio == p.folio:
                return newPrestamo
    
    def VerPrestamos(self):
        return ListaPrestamos