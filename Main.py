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
mydb = ConexionMySQL
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
    mydb.Insertar('miembros', name=persona.name, email=persona.email, cel=persona.cel)
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

def SubMenu():
    print("|   1.- Mostrar                      3.- Modificar   |")
    print("|   2.- Registrar                    4.- Eliminar    |")
    print("|                                                    |")
    print("|                     0.- MENU                       |")
    print("|----------------------------------------------------|")
    accion = int(input("                Accion a Realizar => ")); print()
    return accion

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
    return (dbs,mydb)

def MostrarDB(tab):
    reg = mydb.Mostrar(tab)
    if tab == 'miembros':
        print("|  ID   || NOMBRE\t\t|| CORREO\t\t|| CELULAR\t|| PRESTAMOS DISPONIBLES|")
        for r in reg:
            if dbs[0] == '-MySQL-':
                print("|"+str(r[0])+"\t||"+r[1]+"\t||"+r[2]+"\t||"+str(r[3])+"\t||"+str(r[4])+"\t\t\t|")
            else:
                print("|"+str(r['id'])+"\t||"+r['name']+"\t||"+r['email']+"\t||"+str(r['cel'])+"\t||"+str(r['prestamos'])+"\t\t\t|")
    elif tab == 'articulos':
        print("|  ID   || ARTICULO\t\t|| INVENTARIO\t |")
        for r in reg:
            if dbs[0] == '-MySQL-':
                print("|"+str(r[0])+"\t||"+r[1]+"\t||"+str(r[2])+"\t\t |")
            else:
                print("|"+str(r['id'])+"\t||"+r['articulo']+"\t||"+str(r['inventario'])+"\t\t |")
    else:
        print("| FOLIO || MIEMBRO\t|| ARTICULO\t|| CANTIDAD\t|| F.PRESTAMO\t\t\t|| DEVUELTO\t|| F.ENTREGADO\t\t\t|")
        for r in reg:
            if dbs[0] == '-MySQL-':
                print("|"+str(r[0])+"\t||"+str(r[1])+"\t\t||"+str(r[2])+"\t\t||"+str(r[3])+"\t\t||"+r[4]+"\t||"+str(r[5])+"\t\t||"+r[6]+"\t|")
            else:
                print("|"+str(r['folio'])+"\t||"+str(r['miembro'])+"\t\t||"+str(r['articulo'])+"\t\t||"+str(r['cantidad'])+"\t\t||"+r['fPrestamo']+"\t||"+str(r['devuelto'])+"\t\t||"+r['fDevolucion']+"\t|")
def InsertarDB(tab):
    if tab == 'miembros':
        # print("|----- REGISTRAR MIEMBRO -----|")
        nombre = input("| Nombre: ")
        correo = input("| Correo: ")
        cel    = input("| Celular: ")
        # persona = p.RegistroPersona(nombre, correo, cel)
        mydb.Insertar(tab, name=nombre, email=correo, cel=cel)
        print("|\n| Miembro Registrado")
        print("| Bienvenido " + nombre)
        myID = mydb.MostrarID()
        print("| Su ID de miembro es: "+str(myID))
    elif tab == 'articulos':
        articulo   = input("|   Articulo: ")
        inventario = int(input("| Inventario: "))
        articulo = a.RegistroArticulo(articulo, inventario)
        mydb.Insertar(tab, articulo=articulo.articulo, inventario=articulo.inventario)
        print("|\n| Articulo Registrado")
    else:
        miembro  = int(input("| ID Miembro: "))
        articulo = int(input("|   Articulo: "))
        cantidad = int(input("|   Cantidad: "))
        datosValidados = l.ValidarDatosPrestamo(miembro,articulo,cantidad,mydb,dbs[0])
        if datosValidados:
            fecha = str(datetime.datetime.now())
            prestamo = l.RegistroPrestamo(miembro, articulo, cantidad, fecha)
            mydb.Insertar(tab, miembro=prestamo.miembro, articulo=prestamo.articulo, cantidad=prestamo.cantidad, fPrestamo=prestamo.fPrestamo)
            print("|\n| Registro Exitoso|Folio del prestamo: "+str(prestamo.folio)+"\n")
        else: print(datosValidados)

def ActualizarDB(tab, folio=None):
    if tab == 'miembros' or tab == 'articulos':
        t = tab
        cs= input("Cambiar el campo: ")
        vs= input("Por: ")
        w = input("Donde el campo: ")
        c = input("Sea: ")
        v = input("A...: ")
        mydb.Actualizar(tabla=t, campoSet=cs,valorSet=vs,
        campoWhere=w, condicional=c,valorWhere=v)
    else:
        folio = int(input("| Numero de Folio del Prestamo: "))
        t = 'prestamos'
        cs= 'devuelto'
        vs= True
        w = 'folio'
        c = '='
        v = folio
        mydb.Actualizar(tabla=t, campoSet=cs,valorSet=vs,
        campoWhere=w, condicional=c,valorWhere=v)
        cs = 'fDevolucion'
        vs = fecha = str(datetime.datetime.now())
        mydb.Actualizar(tabla=t, campoSet=cs,valorSet=vs,
        campoWhere=w, condicional=c,valorWhere=v)
        print("| Prestamo devuleto")

def EliminarDB(tab):
    t = tab
    c = input("Donde el campo:")
    v = input("Tenga el valor:")
    mydb.Eliminar(tabla=t, campoWhere=c, valorWhere=v)
    print('campo eliminado')


dbs = SeleccionarBD()
mydb = dbs[1]
while menu == True:
    print("|----------------------- MENU -------------"+dbs[0]+"---|")
    print("|   1.- Prestamos                3.- Articulos       |")
    print("|   2.- Miembros                 4.- Seleccionar DB  |")
    print("|                                                    |")
    print("|                     0.- Salir                      |")
    print("|                                                    |")
    accion = input("|                Ingresar a => ");
    print("|                                                    |")

    if accion in ("1","2","3","4","5","6","7","8","0"):
        accion = int(accion)
        if accion in (1,2,3,4):
            if accion == 1:
                print("|--------------------- PRESTAMOS --------------------|")
                tabla = 'prestamos'
            elif accion == 2:
                print("|---------------------- MIEMBROS --------------------|")
                tabla = 'miembros'
            elif accion == 3:
                print("|---------------------- ARTICULOS -------------------|")
                tabla = 'articulos'
            else:
                dbs = SeleccionarBD()
                mydb = dbs[1]
                tabla = 'miembros'
                pass
            accion = SubMenu()
            if accion == 1:
                print("|---------------------------------------------------------- MOSTRAR --------------------------------------------------------------|")
                MostrarDB(tabla)
                # VerPrestamos()
                print("|---------------------------------------------------------------------------------------------------------------------------------------|\n")
            elif accion == 2:
                print("|------------------ REGISTRAR -------------------|")
                InsertarDB(tabla)
                # Prestamos(miembro,articulo,cantidad)
                print("|------------------------------------------------|\n")
            elif accion == 3:
                print("|------------------- MODIFICAR ------------------|")
                if tabla == 'prestamos':
                    print("|----------------- DEVOLUCIONES -----------------|")
                # Devoluciones(folio)
                ActualizarDB(tabla)
                print("|------------------------------------------------|\n")
            elif accion == 4:
                print("|------------------- ELIMINAR -------------------|")
                EliminarDB(tabla)
                print("|------------------------------------------------|\n")
            else:
                pass
        else:
            print("Hasta Pronto\n")
            menu = False
            
        '''Codigo antiguo'''
            # elif accion == 2:
            #     print("|-------------------- MIEMBROS ------------------|")
            #     accion = SubMenu()
            #     if accion == 1:
            #         tabla = 'miembros'
            #         print("|---------------------------------------------------------- VER PRESTAMOS --------------------------------------------------------------|")
            #         MostrarDB(tabla)
            #         # VerPrestamos()
            #         print("|---------------------------------------------------------------------------------------------------------------------------------------|\n")
            #     elif accion == 2:
            #         print("|-------------- REGISTRAR PRESTAMO --------------|")
            #         miembro  = int(input("| ID Miembro: "))
            #         articulo = int(input("|   Articulo: "))
            #         cantidad = int(input("|   Cantidad: "))
            #         InsertarDB(tabla)
            #         # Prestamos(miembro,articulo,cantidad)
            #         print("|------------------------------------------------|\n")
            #     elif accion == 3:
            #         print("|-------------- MODIFICAR PRESTAMO --------------|")
            #         print("|----------------- DEVOLUCIONES -----------------|")
            #         folio = int(input("| Numero de Folio del Prestamo: "))
            #         # Devoluciones(folio)
            #         ActualizarDB(tabla,folio)
            #         print("|------------------------------------------------|\n")
            #     elif accion == 4:
            #         print("|-------------- MODIFICAR PRESTAMO --------------|")
            #         EliminarDB(tabla)
            #         print("|------------------------------------------------|\n")
            #     else:
            #       pass
            #     print("|------------------------------------------------|\n")
            # elif accion == 4:
            #     dbs = SeleccionarBD()
            # else:
                

            # elif accion == 3:
            #     print("|----- REGISTRAR MIEMBRO -----|")
            #     nombre = input("| Nombre: ")
            #     correo = input("| Correo: ")
            #     cel    = input("| Celular: ")
            #     RegistrarMiembro()
            #     print("|-----------------------------|\n") 

            # elif accion == 4:
            #     print("|----- REGISTRAR ARTICULO -----|")
            #     articulo   = input("|   Articulo: ")
            #     inventario = int(input("| Inventario: "))
            #     RegistrarArticulo()
            #     print("|------------------------------|\n")

            # elif accion == 5:
            #     print("|------------------ INVENTARIO ------------------|")
            #     VerInventario()
            #     print("|------------------------------------------------|\n")

            # elif accion == 6:
            #     print("|----------------------------------------- VER MIEMBRO -----------------------------------------|")
            #     VerMiembros()
            #     print("|-----------------------------------------------------------------------------------------------|\n")

            # elif accion == 8:
            #     dbs = SeleccionarBD()

            # else:
            #     print("Hasta Pronto\n")
            #     menu = False
        '''Codigo antiguio'''
                
    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-7\n")
else: print("Fin...")