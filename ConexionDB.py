import mysql.connector
import pymongo

class conexionDB:
    def conexion(self, db):
        if db == 'MySQL':
          dbMySQL()
        elif db == 'Mongo':
            pass
        else:
          pass

class dbMySQL:
    mydb = mysql.connector.connect(
        host     = 'localhost',
        user     = 'root',
        password = '',
        database = 'centro_deportivo'
    )
    print("MySQL -> conectado a la BD: "+mydb._database)

    myCursor = mydb.cursor()
    # myCursor.execute("CREATE DATABASE centro_deportivo")

    '''SETUP'''
    v = True
    myCursor.execute("SHOW TABLES")
    for x in myCursor:
        # print(x)
        v = False
    if v:
        myCursor.execute("CREATE TABLE miembros (id Int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), cel VARCHAR(255), prestamos Int)")
        myCursor.execute("CREATE TABLE articulos (id Int AUTO_INCREMENT PRIMARY KEY, articulo VARCHAR(255), inventario Int)")
        myCursor.execute("CREATE TABLE prestamos (folio Int AUTO_INCREMENT PRIMARY KEY, miembro Int, articulo Int, cantidad Int, fPrestamo VARCHAR(255), devuelto bool, fDevolucion VARCHAR(255))")
        myCursor.execute("SHOW TABLES")
        for x in myCursor:
            print(x)
        
        '''SEEDS'''
        sql = "INSERT INTO miembros (name, email, cel, prestamos) VALUES (%s, %s, %s, %s)"
        val = [
            ('Admin Deportivo', 'admin@gmail.com', '8711000000', 3),
            ('Nestor Puentes', 'nestor@gmail.com', '8711000011', 3),
            ('Daniela Jimenez', 'daniela@gmail.com', '8711000022', 3)
        ]
        myCursor.executemany(sql,val)
        mydb.commit()
        print(myCursor.rowcount, "registros fueron insertadas en Miembros")


        sql = "INSERT INTO articulos (articulo, inventario) VALUES (%s, %s)"
        val = [
            ('Pelota de Beisbol', 100),
            ('Bat de Beisbol (metalico)', 100),
            ('Guante de Beisbol', 100),
            ('Balon de Futbol', 100),
            ('Guantes de Portero', 100),
            ('Balon de Basketbol', 100)
        ]
        myCursor.executemany(sql,val)
        mydb.commit()
        print(myCursor.rowcount, "registros fueron insertadas en Articulos")
        # print("1 record inserted, ID:", myCursor.lastrowid)


        # sql = "INSERT INTO prestamos (miembro, articulo, cantidad, fPrestamo, devuelto, fDevolucion) VALUES (%s, %s, %s, %s, %s, %s)"
        # val = [
        #     (3, 1, 3, 'hoy', False, ''),
        #     (2, 2, 4, 'hoy', True, '')
        # ]
        # myCursor.executemany(sql,val)
        # mydb.commit()
        # print(myCursor.rowcount, "registros fueron insertadas en Articulos")
        # print("1 record inserted, ID:", myCursor.lastrowid)
        '''SEEDERS'''
        v = True
    else:
        pass
    '''SETUP'''

    # tabla = "articulos"
    # campoSet = "inventario"
    # valorSet = '100'
    # campoWhere = "inventario"
    # condicional = '='
    # valorWhere = '10'

    '''INSERTAR DATOS'''
    def Insertar(self, tabla,name=None,email=None,cel=None,prestamo=None,miembro=None,articulo=None,inventario=None,cantidad=None,fPrestamo=None,devuelto=None,fDevolucion=None):
        if tabla == 'miembros':
            sql = "INSERT INTO "+tabla+" (name, email, cel, prestamos) \
                VALUES (%s, %s, %s, %s)"
            val =(name, email, cel, 3)
        elif tabla == 'articulos':
            sql = "INSERT INTO "+tabla+" (articulo, inventario) \
                VALUES (%s, %s)"
            val =(articulo, inventario)
        else:
            sql = "INSERT INTO "+tabla+" (miembro, articulo, cantidad, fPrestamo, devuelto, fDevolucion) \
                VALUES (%s, %s, %s, %s, %s, %s)"
            val =(miembro, articulo, cantidad, fPrestamo, devuelto, fDevolucion)
        myCursor.execute(sql,val)
        mydb.commit()

    '''MOSTRAR DATOS'''
    def Mostrar(self, tabla):
        sql = ("SELECT * FROM "+tabla)
        myCursor.execute(sql)
        myResult = myCursor.fetchall()
        print(myResult)
        return myResult
        for x in myResult:
            print(x)

    '''ACTUALIZAR DATOS'''
    def Actualizar(self, tabla,campoSet,valorSet,campoWhere,condicional,valorWhere):
        sql = ("UPDATE "+tabla+
            " SET "+campoSet+" = %s"+
            " WHERE "+campoWhere+" "+condicional+" %s"
        )
        val = (valorSet,valorWhere)
        myCursor.execute(sql,val)
        mydb.commit()
        print(myCursor.rowcount,"fila(s) actualizadas")

    '''ELIMINAR DATOS'''
    def Eliminar(self, tabla,campoWhere,valorWhere):
        sql = ("DELETE FROM "+tabla+" WHERE "+campoWhere+" = %s")
        val = (valorWhere)
        myCursor.execute(sql,val)
        mydb.commit()
        print(myCursor.rowcount,"registro(s) eliminado(s)")
