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

    print("| Registro Exitoso|Folio del prestamo: "+str(folio)+"\n")
    Prestamos.append(newPrestamo)

    print("|----- Resumen del prestamo -----|")
    print("|- Folio: "+str(Prestamos[0].folio)+" -|")
    print("|- Meimbro: "+Prestamos[0].miembro+" -|")
    print("|- Articulo: "+Prestamos[0].articulo+" -|")
    print("|- Cantidad: "+str(Prestamos[0].cantidad)+" -|")
    print("|- fPrestamo: "+Prestamos[0].fPrestamo+" -|")
    print("|- Devuelto: "+str(Prestamos[0].devuelto)+" -|")
    print("|- fDevolucion: "+Prestamos[0].fDevolucion+" -|")
    
def Devolucion():
    pass

def RegistrarMiembro(Id, nombre, correo, cel):
    newMiembro = P.Persona(Id, nombre, correo, cel)
    print("|\n| Miembro Registrado")
    print("| Bienvenido " + newMiembro.name)
    print("| Su ID de miembro es: "+str(Id))

    Miembros.append(newMiembro)
    # print(Miembros[0].name)

def VerInventario():
    pass

def VerMiembros():
    print("|  ID   ||NOMBRE\t\t||CORREO\t\t||CELULAR\t|")
    for miembro in Miembros:
        print("|"+str(miembro.Id)+"\t||"+miembro.name+"\t||"+miembro.email+"\t||"+miembro.cel+"\t|")


def VerPrestamos():
    pass

while menu == True:
    print("|----------------------- MENU -----------------------|")
    print("|   1.- Nuevo Prestamo        4.- Ver inventario     |")
    print("|   2.- Devolucion            5.- Ver Miembros       |")
    print("|   3.- Registrar Miembro     6.- Ver Prestamos      |")
    print("|                                                    |")
    print("|                     0.- Salir                      |")
    print("|----------------------------------------------------|")
    accion = input("Accion a Realizar => ")
    print()
    if accion == "1" or accion == "2" or accion == "3" or accion == "4" or accion == "5" or accion == "6" or accion == "0":
        accion = int(accion)
        if accion >= 0 and accion <= 6:
            if accion == 1:
                print("|----- REGISTRAR PRESTAMO -----|")
                idL += 1
                miembro  = input("| Miembro: ")
                articulo = input("| Articulo: ")
                cantidad = int(input("| Cantidad: "))
                fPedido  = now
                RegistrarPrestamo(idL, miembro, articulo, cantidad, fPedido)
                print("|------------------------------|\n")
            
            elif accion == 2:
                print("|----- DEVOLUCIONES -----|")

                print("|------------------------|\n")

            elif accion == 3:
                print("|----- REGISTRAR MIEMBRO -----|")
                idP += 1
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                cel    = input("Celular: ")
                RegistrarMiembro(idP, nombre, correo, cel)
                print("|-----------------------------|\n")

            elif accion == 4:
                print("|----- INVENTARIO -----|")

                print("|----------------------|\n")

            elif accion == 5:
                print("|----------------------------- VER MIEMBRO -----------------------------|")
                VerMiembros()
                print("|-----------------------------------------------------------------------|\n")

            elif accion == 6:
                print("|----- VER PRESTAMOS -----|")

                print("|-------------------------|\n")

            else:
                print("Hasta Pronto\n")
                menu = False
        else:
            print("Opcion invalida|intenta con un numero del 0-6\n")
    else: print("Opcion Invalida|debe de ser un numero entero entre el 0-6\n")
else:
    print("Fin...")

