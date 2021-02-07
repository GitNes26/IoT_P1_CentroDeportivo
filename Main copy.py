# encoding: utf-8
import datetime
from ClassPerson import Persona as P
from ClassArticle import Articulo as A
from ClassLoan import Prestamo as L
import ConexionMySQL
import ConexionMongoDB

# interface = Interf(bandera=1)
p = P(bandera =1)
a = A(bandera =1)
l = L(bandera =1)
menu = True
mydb = ''
dbs = ''

#Metodos de cada Opcion

def Prestamos(miembro,articulo,cantidad):
    datosValidados = l.ValidarDatosPrestamo(miembro,articulo,cantidad)
    if datosValidados:
        fecha = str(datetime.datetime.now())
        prestamo = l.RegistroPrestamo(miembro, articulo, cantidad, fecha)
        print("|\n| Registro Exitoso|Folio del prestamo: "+str(prestamo.folio)+"\n")
        # for pr in prestamo:
        #     if folio == pr.folio:
        #         print("|------------- Resumen del prestamo -------------|")
        #         print("|-       Folio: "+str(pr.folio)+"\t\t\t\t-|")
        #         print("|-     Miembro: "+str(pr.miembro)+" - "+m.name+"\t\t-|")
        #         print("|-    Articulo: "+pr.articulo+"\t\t\t\t-|")
        #         print("|-    Cantidad: "+str(pr.cantidad)+"\t\t\t\t-|")
        #         print("|-   fPrestamo: "+pr.fPrestamo+"\t-|")
        #         print("|-    Devuelto: "+str(pr.devuelto)+"\t\t\t\t-|")
        #         print("|- fDevolucion: "+pr.fDevolucion+"\t\t\t\t-|")
        #         break
    else: print(datosValidados)

def Devoluciones(folio):
    devolucion = l.RegistroDevolucion(folio)
    if devolucion:
      print('| Devolucion Exitosa | Que tenga buen dia')
    else: print('| Devolucion Fallida | Verifique su folio')

def RegistrarMiembro():
    persona = p.RegistroPersona(nombre, correo, cel)
    # mydb.Insertar('miembros', name=persona.name, email=persona.email, cel=persona.cel)
    print("|\n| Miembro Registrado")
    print("| Bienvenido " + persona.name)
    print("| Su ID de miembro es: "+str(persona.Id))

def RegistrarArticulo():
    articulo = a.RegistroArticulo(articulo, inventario)
    mydb.Insertar('articulos', articulo=articulo.articulo, inventario=articulo.inventario)

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
        print("|"+str(pres.folio)+"\t||"+str(pres.miembro)+"\t\t||"+str(pres.articulo)+"\t\t||"+str(pres.cantidad)+"\t\t||"+pres.fPrestamo+"\t||"+str(pres.devuelto)+"\t\t||"+pres.fDevolucion+"\t|")
        # print("|"+str(pres.folio)+"\t||"+str(pres.miembro)+"\t||"+str(pres.articulo)+"\t||"+str(pres.cantidad)+"\t||"+pres.fPrestamo+"||"+str(pres.devuelto)+"\t||"+pres.fDevolucion+"|")

def SeleccionarBD():
    print("|------------------- Base de Datos ------------------|")
    print("|       1.- MySQL                    2.- MongoDB     |")
    mydb = input("| Elige que base de datos desea utilizar: ")
    if mydb == '1':
        mydb = ConexionMySQL
        print("|                BD -> MySQL                         |")
        dbs = "-MySQL-"
    else:
        mydb = ConexionMongoDB
        print("|                BD -> MongoDB                       |")
        dbs = "MongoDB"
    print("|                                                    |")
    return dbs


dbs = SeleccionarBD()
while menu == True:
    print("|----------------------- MENU -------------"+dbs+"---|")
    print("|   1.- Nuevo Prestamo        5.- Ver inventario     |")
    print("|   2.- Devolucion            6.- Ver Miembros       |")
    print("|   3.- Registrar Miembro     7.- Ver Prestamos      |")
    print("|   4.- Registrar Articulo    8.- Seleccionar BD     |")
    print("|                                                    |")
    print("|                     0.- Salir                      |")
    print("|----------------------------------------------------|")
    accion = input("                Accion a Realizar => "); print()
    if accion in ("1","2","3","4","5","6","7","8","0"):
        accion = int(accion)
        if accion == 1:
            print("|-------------- REGISTRAR PRESTAMO --------------|")
            miembro  = int(input("| ID Miembro: "))
            articulo = int(input("|   Articulo: "))
            cantidad = int(input("|   Cantidad: "))
            Prestamos(miembro,articulo,cantidad)
            print("|------------------------------------------------|\n")
        
        elif accion == 2:
            print("|----------------- DEVOLUCIONES -----------------|")
            folio = int(input("| Numero de Folio del Prestamo: "))
            Devoluciones(folio)
            print("|------------------------------------------------|\n")

        elif accion == 3:
            print("|----- REGISTRAR MIEMBRO -----|")
            nombre = input("| Nombre: ")
            correo = input("| Correo: ")
            cel    = input("| Celular: ")
            RegistrarMiembro()
            print("|-----------------------------|\n")  

        elif accion == 4:
            print("|----- REGISTRAR ARTICULO -----|")
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

        elif accion == 8:
            dbs = SeleccionarBD()

        else:
            print("Hasta Pronto\n")
            menu = False
                
    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-7\n")
else: print("Fin...")