# import json
# import ClassPerson
# from ClassArticle import Articulo as a
# from ClassLoan import Prestamo as l

# P=ClassPerson.Persona()
# A=a()
# L=l()
# ListaMiembros = []

# class Interf:
#   def __init__(self, bandera=0):
#     self.bandera = 0
#     if (bandera == 1):
#       data = {}
#       data['ListaMiembros'] = []
#       ListaMiembros = []
#       with open('dataPersonas.json') as f:
#             listillaJSON = json.load(f)
#             for li in listillaJSON['ListaMiembros']:
#               newMiembro = P(li['Id'],li['name'],li['email'],li['cel'],li['prestamos'])
#               ListaMiembros.append(newMiembro)


{
    "ListaMiembros": [
        {
            "Id": 1,
            "name": "Admin Deportivo",
            "email": "admin@deportivo.com",
            "cel": "8711226655",
            "prestamos": 3
        },
        {
            "Id": 2,
            "name": "Nestor Puentes",
            "email": "nestor@gmail.com",
            "cel": "8711776622",
            "prestamos": 3
        },
        {
            "Id": 3,
            "name": "Daniela Jimenez",
            "email": "daniela@gmail.com",
            "cel": "8766554433",
            "prestamos": 3
        }
    ]
}