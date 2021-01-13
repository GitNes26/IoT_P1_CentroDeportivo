import datetime
import ClassPerson as P
import ClassArticle as A
import ClassLoan as L

fecha = datetime.datetime.now()
now = str(fecha)
menu = True
idP = 0
idA = 0
idL = 0
Miembros = []
Articulos = []
Prestamos = []

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
    
def Devoluciones(folio):
    print("| Buscando prestamo...")
    i = 0
    encontrado = False
    for prestamo in Prestamos:
        if folio == prestamo.folio:
          prestamo.devuelto = True
          prestamo.fDevolucion = now
          encontrado = True
        else: i += 1
    if encontrado:
        print("| Prestamo Devuelto\n| ")
        print("|------------- Resumen del prestamo -------------|")
        print("|-       Folio: "+str(Prestamos[i].folio)+"\t\t\t\t-|")
        print("|-     Miembro: "+str(Prestamos[i].miembro)+"\t\t\t\t-|")
        print("|-    Articulo: "+Prestamos[i].articulo+"\t\t\t\t-|")
        print("|-    Cantidad: "+str(Prestamos[i].cantidad)+"\t\t\t\t-|")
        print("|-   fPrestamo: "+Prestamos[i].fPrestamo+"\t-|")
        print("|-    Devuelto: "+str(Prestamos[i].devuelto)+"\t\t\t\t-|")
        print("|- fDevolucion: "+Prestamos[i].fDevolucion+"\t-|")
    else: print("| Prestamo invalido")
     

def RegistrarMiembro(Id, nombre, correo, cel):
    newMiembro = P.Persona(Id, nombre, correo, cel)
    newMiembro.prestamos = 3
    print("|\n| Miembro Registrado")
    print("| Bienvenido " + newMiembro.name)
    print("| Su ID de miembro es: "+str(Id))

    Miembros.append(newMiembro)

def RegistrarArticulo(idA, articulo, inventario):
    newArticulo = A.Articulo(idA, articulo, inventario)
    print("|\n| Articulo Registrado")

    Articulos.append(newArticulo)

def VerInventario():
    print("|  ID   || ARTICULO\t\t|| INVENTARIO\t |")
    for articulo in Articulos:
        print("|"+str(articulo.Id)+"\t||"+articulo.articulo+"\t||"+str(articulo.inventario)+"\t\t |")
    
def VerMiembros():
    print("|  ID   || NOMBRE\t\t|| CORREO\t\t|| CELULAR\t|| PRESTAMOS DISPONIBLES|")
    for miembro in Miembros:
        print("|"+str(miembro.Id)+"\t||"+miembro.name+"\t||"+miembro.email+"\t||"+miembro.cel+"\t||"+str(miembro.prestamos)+"\t\t\t|")

def VerPrestamos():
    print("|FOLIO || MIEMBRO\t\t|| ARTICULO\t\t|| CANTIDAD\t|| F.PRESTAMO\t\t|| DEVUELTO\t|| F.ENTREGADO\t\t|")
    for pres in Prestamos:
        print("|"+str(pres.folio)+"\t||"+str(pres.miembro)+"\t||"+pres.articulo+"\t||"+str(pres.cantidad)+"\t||"+pres.fPrestamo+"||"+str(pres.devuelto)+"\t||"+pres.fDevolucion+"|")

    

while menu == True:
    print("|----------------------- MENU -----------------------|")
    print("|   1.- Nuevo Prestamo        5.- Ver inventario     |")
    print("|   2.- Devolucion            6.- Ver Miembros       |")
    print("|   3.- Registrar Miembro     7.- Ver Prestamos      |")
    print("|   4.- Registrar Articulo                           |")
    print("|                                                    |")
    print("|                     0.- Salir                      |")
    print("|----------------------------------------------------|")
    accion = input("Accion a Realizar => ")
    print()
    if accion == "1" or accion == "2" or accion == "3" or accion == "4" or accion == "5" or accion == "6" or accion == "7" or accion == "0":
        accion = int(accion)
        if accion >= 0 and accion <= 7:
            if accion == 1:
                print("|-------------- REGISTRAR PRESTAMO --------------|")
                miembro  = int(input("| ID Miembro: "))
                for m in Miembros:
                    if miembro == m.Id:
                        if m.prestamos < 0:
                            idL += 1
                            articulo = input("|   Articulo: ")
                            cantidad = int(input("|   Cantidad: "))
                            RegistrarPrestamo(idL, miembro, articulo, cantidad, now)
                            m.prestamos -= 1
                        else: print("Prestamo Rechazado| Ya no te quedan más prestamos disponibles")
                    break
                else: print("| Prestamo Rechazado| Miembro no registrado")
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
                RegistrarMiembro(idP, nombre, correo, cel)
                print("|-----------------------------|\n")
            
            elif accion == 4:
                print("|----- REGISTRAR ARTICULO -----|")
                idA += 1
                articulo   = input("|   Articulo: ")
                inventario = int(input("| Inventario: "))
                RegistrarArticulo(idA, articulo, inventario)
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
                print("|--------------------------------------------------------- VER PRESTAMOS --------------------------------------------------------------|")
                VerPrestamos()
                print("|--------------------------------------------------------------------------------------------------------------------------------------|\n")

            else:
                print("Hasta Pronto\n")
                menu = False
        else: print("Opcion invalida|intenta con un numero del 0-6\n")
    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-6\n")
else: print("Fin...")