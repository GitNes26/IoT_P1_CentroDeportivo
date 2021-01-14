# encoding: utf-8
import datetime
from ClassPerson import Persona as P
from ClassArticle import Articulo as A
from ClassLoan import Prestamo as L
# import ClassLoan as L

p = P()
a = A()
l = L()

fecha = datetime.datetime.now()
now = str(fecha)
menu = True
idP = 0
idA = 0
idL = 0
# Miembros = []
# Articulos = []
# Prestamos = []

#Metodos de cada Opcion
def RegistrarPrestamo(folio, miembro, articulo, cantidad, fecha):
    newPrestamo = L.Prestamo(folio, miembro, articulo, cantidad, fecha)
    newPrestamo.devuelto = False
    newPrestamo.fDevolucion = ""
    print("|\n| Registro Exitoso|Folio del prestamo: "+str(folio)+"\n")
    Prestamos.append(newPrestamo)
    for p in Prestamos:
        if folio == p.folio:
            print("|------------- Resumen del prestamo -------------|")
            print("|-       Folio: "+str(p.folio)+"\t\t\t\t-|")
            print("|-     Miembro: "+str(p.miembro)+" - "+m.name+"\t\t-|")
            print("|-    Articulo: "+p.articulo+"\t\t\t\t-|")
            print("|-    Cantidad: "+str(p.cantidad)+"\t\t\t\t-|")
            print("|-   fPrestamo: "+p.fPrestamo+"\t-|")
            print("|-    Devuelto: "+str(p.devuelto)+"\t\t\t\t-|")
            print("|- fDevolucion: "+p.fDevolucion+"\t\t\t\t-|")
            break
    
def Devoluciones(folio):
    print("| Buscando prestamo...")
    i = 0
    encontrado = False
    for prestamo in Prestamos:
        if folio == prestamo.folio:
          prestamo.devuelto = True
          prestamo.fDevolucion = now
          encontrado = True
          break
        else: i += 1
    if encontrado:
        for m in Miembros:
            if miembro == m.Id:
                m.prestamos += 1
                print("| Prestamo Devuelto\n| ")
                print("|------------- Resumen del prestamo -------------|")
                print("|-       Folio: "+str(Prestamos[i].folio)+"\t\t\t\t-|")
                print("|-     Miembro: "+str(Prestamos[i].miembro)+" - "+m.name+"\t\t\t-|")
                print("|-    Articulo: "+Prestamos[i].articulo+"\t\t\t\t-|")
                print("|-    Cantidad: "+str(Prestamos[i].cantidad)+"\t\t\t\t-|")
                print("|-   fPrestamo: "+Prestamos[i].fPrestamo+"\t-|")
                print("|-    Devuelto: "+str(Prestamos[i].devuelto)+"\t\t\t\t-|")
                print("|- fDevolucion: "+Prestamos[i].fDevolucion+"\t-|")
                break
    else: print("| Devolucion invalida| El folio del prestamo no existe ")
     

# def RegistrarMiembro(Id, nombre, correo, cel):
#     newMiembro = P.Persona(Id, nombre, correo, cel)
#     newMiembro.prestamos = 3
#     print("|\n| Miembro Registrado")
#     print("| Bienvenido " + newMiembro.name)
#     print("| Su ID de miembro es: "+str(Id))
#     Miembros.append(newMiembro)

# def RegistrarArticulo(idA, articulo, inventario):
#     print("|\n| Articulo Registrado")

#     Articulos.append(newArticulo)

def VerInventario():
    print("|  ID   || ARTICULO\t\t|| INVENTARIO\t |")
    listaA= a.VerArticulos()
    for articulo in listaA:
        print("|"+str(articulo.Id)+"\t||"+articulo.articulo+"\t||"+str(articulo.inventario)+"\t\t |")
    
def VerMiembros():
    print("|  ID   || NOMBRE\t\t|| CORREO\t\t|| CELULAR\t|| PRESTAMOS DISPONIBLES|")
    ListaP = p.VerPersonas()
    for miembro in ListaP:
        print("|"+str(miembro.Id)+"\t||"+miembro.name+"\t||"+miembro.email+"\t||"+miembro.cel+"\t||"+str(miembro.prestamos)+"\t\t\t|")

def VerPrestamos():
    # print("| FOLIO || MIEMBRO\t\t|| ARTICULO\t\t|| CANTIDAD\t|| F.PRESTAMO\t\t|| DEVUELTO\t|| F.ENTREGADO\t\t|")
    print("| FOLIO || MIEMBRO\t|| ARTICULO\t|| CANTIDAD\t|| F.PRESTAMO\t\t\t|| DEVUELTO\t|| F.ENTREGADO\t\t\t|")
    ListaL = l.VerPrestamos()
    for pres in ListaL:
        print("|"+str(pres.folio)+"\t||"+str(pres.miembro)+"\t\t||"+str(pres.articulo)+"\t\t||"+str(pres.cantidad)+"\t\t||"+pres.fPrestamo+"\t||"+str(pres.devuelto)+"\t||"+pres.fDevolucion+"\t|")
        # print("|"+str(pres.folio)+"\t||"+str(pres.miembro)+"\t||"+str(pres.articulo)+"\t||"+str(pres.cantidad)+"\t||"+pres.fPrestamo+"||"+str(pres.devuelto)+"\t||"+pres.fDevolucion+"|")


def RegistrarPrestamo(miembro,articulo,cantidad,folio=None,fecha=None):
    datosValidados = l.ValidarDatosPrestamo(miembro,articulo,cantidad)
    if datosValidados:
        prestamo = l.RegistroPrestamo(folio, miembro, articulo, cantidad, fecha)
        print("|\n| Registro Exitoso|Folio del prestamo: "+str(prestamo.folio)+"\n")
        # for pr in prestamo:
        #     if folio == pr.folio:
        #         print("|------------- Resumen del prestamo -------------|")
        #         print("|-       Folio: "+str(pr.folio)+"\t\t\t\t-|")
        #         # print("|-     Miembro: "+str(pr.miembro)+" - "+m.name+"\t\t-|")
        #         print("|-    Articulo: "+pr.articulo+"\t\t\t\t-|")
        #         print("|-    Cantidad: "+str(pr.cantidad)+"\t\t\t\t-|")
        #         print("|-   fPrestamo: "+pr.fPrestamo+"\t-|")
        #         print("|-    Devuelto: "+str(pr.devuelto)+"\t\t\t\t-|")
        #         print("|- fDevolucion: "+pr.fDevolucion+"\t\t\t\t-|")
        #         break
    else: print("| Prestamo Rechazado|Miembro no registrado")
    
def RegistrarMiembro():
    persona = p.RegistroPersona(idP, nombre, correo, cel)
    print("|\n| Miembro Registrado")
    print("| Bienvenido " + persona.name)
    print("| Su ID de miembro es: "+str(persona.Id))

def RegistrarArticulo():
    a.RegistroArticulo(idA, articulo, inventario)

while menu == True:
    print("|----------------------- MENU -----------------------|")
    print("|   1.- Nuevo Prestamo        5.- Ver inventario     |")
    print("|   2.- Devolucion            6.- Ver Miembros       |")
    print("|   3.- Registrar Miembro     7.- Ver Prestamos      |")
    print("|   4.- Registrar Articulo                           |")
    print("|                                                    |")
    print("|                     0.- Salir                      |")
    print("|----------------------------------------------------|")
    accion = input("                Accion a Realizar => "); print()
    if accion in ("1","2","3","4","5","6","7","0"):
        accion = int(accion)
        if accion >= 0 and accion <= 7:
            if accion == 1:
                print("|-------------- REGISTRAR PRESTAMO --------------|")
                idL += 1
                miembro  = int(input("| ID Miembro: "))
                articulo = int(input("|   Articulo: "))
                cantidad = int(input("|   Cantidad: "))
                RegistrarPrestamo(miembro,articulo,cantidad,idL,now)
                print("|------------------------------------------------|\n")
            
            elif accion == 2:
                print("|----------------- DEVOLUCIONES -----------------|")
                folio = int(input("| Numero de Folio del Prestamo: "))
                Devoluciones(folio)
                print("|------------------------------------------------|\n")

            elif accion == 3:
                print("|----- REGISTRAR MIEMBRO -----|")
                idP += 1
                nombre = input("| Nombre: ")
                correo = input("| Correo: ")
                cel    = input("| Celular: ")
                RegistrarMiembro()
                print("|-----------------------------|\n")
                
            
            elif accion == 4:
                print("|----- REGISTRAR ARTICULO -----|")
                idA += 1
                articulo   = input("|   Articulo: ")
                inventario = int(input("| Inventario: "))
                RegistrarArticulo()
                print("|------------------------------|\n")

            elif accion == 5:
                print("|------------------ INVENTARIO ------------------|")
                VerInventario()
                print("|------------------------------------------------|\n")

            elif accion == 6:
                print("|----------------------------------------- VER MIEMBRO -----------------------------------------|")
                VerMiembros()
                print("|-----------------------------------------------------------------------------------------------|\n")

            elif accion == 7:
                print("|---------------------------------------------------------- VER PRESTAMOS --------------------------------------------------------------|")
                VerPrestamos()
                print("|---------------------------------------------------------------------------------------------------------------------------------------|\n")

            else:
                print("Hasta Pronto\n")
                menu = False
        else: print("Opcion invalida|intenta con un numero del 0-7\n")
    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-7\n")
else: print("Fin...")