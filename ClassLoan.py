class Prestamo:
    def __init__(self, folio, miembro, articulo, cantidad, fPrestamo):
        self.folio     = folio
        self.miembro   = miembro
        self.articulo  = articulo
        self.cantidad  = cantidad
        self.fPrestamo = fPrestamo
        devuelto       : bool
        fDevolucion    : str