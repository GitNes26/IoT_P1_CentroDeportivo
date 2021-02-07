import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb://admin:admin@sandbox.ek99h.mongodb.net:27017/centro_deportivo?retryWrites=true&w=majority")
# myclient = pymongo.MongoClient("mongodb://admin:admin@sandbox.ek99h.mongodb.net:27017")
#("mongodb://admin:admin@sandbox.ek99h.mongodb.net:27017/")
#("mongodb://admin:admin@sandbox.ek99h.mongodb.net:27017/")
# myclient = pymongo.MongoClient(host='mongodb://admin:admin@sandbox.ek99h.mongodb.net', port=27017, document_class=dict, tz_aware=False, connect=True)
mydb = myclient["centro_deportivo"]
# print(myclient.list_database_names())
db=myclient.centro_deportivo
print(db)
print(mydb)
col=db.tests
print(col)
# data=col.find({'name':'gus'})
# print(col.find())
# print("DATA")
# for item in data:
#     print("ENtra")
#     print(item)
 
# collection = myclient.centro_deportivo.tests
# for x in collection: 
#     print(x)
# print(myclient)
'''CREANDO UNA COLECCION'''
# mycoleccion =  mydb["miembros"]


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