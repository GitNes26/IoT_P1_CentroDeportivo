from ClassPerson import Persona as P
import ClassPerson as p
import ClassArticle as a

# p=P
# a=A

ListaPrestamos = []

class Prestamo:
    def __init__(self, folio=None, miembro=None, articulo=None, cantidad=None, fPrestamo=None):
        self.folio     = folio
        self.miembro   = miembro
        self.articulo  = articulo
        self.cantidad  = cantidad
        self.fPrestamo = fPrestamo
        self.devuelto       = False
        self.fDevolucion    = ""

    def RegistroPrestamo(self, folio, miembro, articulo, cantidad, fecha):
        newPrestamo = Prestamo(folio, miembro, articulo, cantidad, fecha)
        ListaPrestamos.append(newPrestamo)
        for p in ListaPrestamos:
            if folio == p.folio:
                return newPrestamo
    
    def VerPrestamos(self):
        return ListaPrestamos

    def ValidarDatosPrestamo(self, miembro,articulo,cantidad):
        #Validar que haya usuarios y tengan prestamos disponibles
        for m in p.ListaMiembros:
            if miembro == m.Id:
                if m.prestamos > 0:
                    #Validar que haya articulos y cantidad requerida
                    for ar in a.ListaArticulos:
                        if articulo == ar.Id:
                            if ar.inventario > 0:
                                if cantidad <= ar.inventario:
                                    return True
                                else: print("| Prestamo Rechazado|No se tiene la cantidad suficiente del ariticulo")
                                break
                            else: print("| Prestamo Rechazado|Articulo solicitado agotado")
                            break
                    else: print("| Prestamo Rechazado|El articulo solicitado no existe")
                    break
                else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
                break
            else: print("| Prestamo Rechazado|Miembro no registrado")
        return False