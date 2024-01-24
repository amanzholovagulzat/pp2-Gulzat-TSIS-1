print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")

import json


with open('C:/Users/a.akram/Desktop/PP2/TSIS4/JSON/sample.json', 'r') as file:
    data = json.load(file)

for obj in data['imdata']:
    print(obj['l1PhysIf']['attributes']['dn'], "                              inherit   9150 ")