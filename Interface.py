import json
from ClassPerson import Persona as P

p=P()

data = {}
data['ListaMiembros'] = []
ListaMiembros = []
with open('dataPersonas.json') as f:
      listillaJSON = json.load(f)
      for li in listillaJSON['ListaMiembros']:
        newMiembro = p(li['Id'],li['name'],li['email'],li['cel'],li['prestamos'])
        ListaMiembros.append(newMiembro)
        
def __init__(self):
    # idd =