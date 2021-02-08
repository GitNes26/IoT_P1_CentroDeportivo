import pymongo
import json

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@sandbox.ek99h.mongodb.net/centro_deportivo?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')

'''CREANDO COLECCIONES'''
mydb = myclient["centro_deportivo"]
colM = mydb["miembros"]
colA = mydb["articulos"]
colP = mydb["prestamos"]

'''SEEDERS'''
# data = [
#     {"id":1 , "name":"Admin Deportivo" , "email":"admin@gmail.com" , "cel":"8711000000", "prestamos":3},
#     {"id":2 , "name":"Nestor Puentes" , "email":"nestor@gmail.com" , "cel":"8711000011", "prestamos":3},
#     {"id":3 , "name":"Daniela Jimenez" , "email":"daniela@gmail.com" , "cel":"8711000022" , "prestamos":3}
# ]
# m = colM.insert_many(data)
# print (m.inserted_ids)

# data = [
#     {"id":1 , "articulo":"Pelota de Beisbol" , "inventario":100},
#     {"id":2 , "articulo":"Bat de Beisbol No.5" , "inventario":100},
#     {"id":3 , "articulo":"Guante de Beisbol" , "inventario":100},
#     {"id":4 , "articulo":"Balon de Futbol" , "inventario":100},
#     {"id":5 , "articulo":"Guantes de Portero" , "inventario":100},
#     {"id":6 , "articulo":"Balon de Basketbol" , "inventario":100},
# ]
# a = colA.insert_many(data)
# print (a.inserted_ids)


'''METODOS'''

def MostrarID():
    x = colM
    print(x.inserted_id)


'''INSERTAR DOCUMENTO'''
def Insertar(tabla,name=None,email=None,cel=None,prestamo=None,miembro=None,articulo=None,inventario=None,cantidad=None,fPrestamo=None,devuelto=False,fDevolucion=None):
    if tabla == 'miembros':
      col = mydb["miembros"]
    elif tabla == 'articulos':
      col = mydb["articulos"]
    else:
      col = mydb["prestamos"]

    x = col.find({},{"_id":0, "id":1}).sort("id",-1)
    for i in x:
        d = int(i['id'])
        break
    if tabla == 'miembros':
        data = {
            "id"       : d+1,
            "name"     : name,
            "email"    : email,
            "cel"      : cel,
            "prestamos": 3
        }
        x = colM.insert_one(data)
        
    elif tabla == 'articulos':
        data = {
            "id"         : d+1,   
            "articulo"   : articulo,
            "inventario" : inventario
        }
        x = colA.insert_one(data)
    else:
        data = {
            "id"          : d+1,   
            "miembro"     : miembro,
            "articulo"    : articulo,
            "cantidad"    : cantidad,
            "fPrestamo"   : fPrestamo,
            "devuelto"    : devuelto,
            "fDevolucion" : fDevolucion
        }
        x = colP.insert_one(data)
    print("1 registro agregado")

'''MOSTRAR DOCUMENTO'''
def Mostrar(tabla):
    if tabla == 'miembros':
      col = mydb["miembros"]
    elif tabla == 'articulos':
      col = mydb["articulos"]
    else:
      col = mydb["prestamos"]
    
    c = col.find({},{"_id":0})
    # print(type(c))
    return c
    # for x in uno:
    #     print(x[2])

# Mostrar('miembros')
def MostrarUno(tabla):
    pass

'''ACTUALIZAR DOCUMENTO'''
def Actualizar(tabla,campoSet,valorSet,campoWhere,condicional,valorWhere):
    if tabla == 'miembros':
      col = mydb["miembros"]
    elif tabla == 'articulos':
      col = mydb["articulos"]
    else:
      col = mydb["prestamos"]

    condicional = '$set'
    query = {campoWhere : valorWhere}
    val = {condicional : {campoSet : valorSet}}

    x = col.update_many(query,val)
    print(x.modified_count, "documento(s) modificado(s)")

'''ELIMINAR DOCUMENTO'''
def Eliminar(tabla,campoWhere,valorWhere):
    if tabla == 'miembros':
      col = mydb["miembros"]
    elif tabla == 'articulos':
      col = mydb["articulos"]
    else:
      col = mydb["prestamos"]

    query = {campoWhere : valorWhere}
    x = col.delete_one(query)
    print(x.deleted_count, "documento(s) eliminado(s)")
    






# myclient = pymongo.MongoClient("mongodb+srv://toro:toro@sandbox.ek99h.mongodb.net/centro_deportivo?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
 
# mydb = myclient["centro_deportivo"]
# print(mydb)
# #print("Collection:", mydb.list_collection_names())
# mycol = mydb["tests"]
# print(mycol)
 
# post_data = {
#  'title': 'Python and MongoDB',
#  'content': 'PyMongo is fun, you guys',
#  'author': 'Scott'
# }
# result = mycol.insert_one(post_data)
 
# x = mycol.find_one({})
# print("Find_One",x)
 
# x = mycol.find({})
# print("Find:",x)
 
# for y in x:
#  print("X:",y)