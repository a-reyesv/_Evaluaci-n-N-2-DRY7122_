#Solicitar ciudad de origen y ciudad de destino#

import requests

route_url = "http://www.mapquestapi.com/directions/v2/route"
key = "OIjeA0ZpFdA4P4SgNKpjL8TykFnk4fUh"  #API KEY

def calcular_distancia_kilometros(origen, destino, key):
    params = {
        "key": key,
        "from": origen,
        "to": destino,
        "unit": "k"  #Distancia en kilómetros
    }
    replydata = requests.get(route_url, params=params)
    if replydata.status_code == 200:
        json_data = replydata.json()
        distancia_km = json_data["route"]["distance"]  #Cálculo de la distancia en km
        return distancia_km
    else:
        return "Error al obtener la distancia"

#Solicitar_Ciudad_de_Origen_y_Ciudad_de_Destino#
print("#######################################################################")
origen = input("  Por favor, ingrese la ciudad de origen: ")
destino = input("  Por favor, ingrese la ciudad de destino: ")

#Imprimir la distancia y mostrar el resultado
distancia = calcular_distancia_kilometros(origen, destino, key)
if isinstance(distancia, float):
    print("-----------------------------------------------------------------------")
    print("  La distancia entre {} y {} es de {} kilómetros".format(origen, destino, distancia))
    print("#######################################################################")
else:
    print(distancia)