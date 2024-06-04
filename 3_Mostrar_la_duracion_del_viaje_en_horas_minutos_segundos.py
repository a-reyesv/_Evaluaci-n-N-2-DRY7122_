#Mostrar la duración del viaje en horas, minutos y segundos#

import requests

route_url = "http://www.mapquestapi.com/directions/v2/route"
key = "OIjeA0ZpFdA4P4SgNKpjL8TykFnk4fUh"  #API KEY

def calcular_distancia_y_duracion(origen, destino, key):
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
        duracion_horas_auto = distancia_km / 60        #Si el vehiculo viaja a 60 km/h
        duracion_horas_caminando = distancia_km / 5    #Si se camina a 5 km/h aproximadamente
        return distancia_km, duracion_horas_auto, duracion_horas_caminando
    else:
        return "Error al obtener la distancia"

#Solicitar ciudad de origen y ciudad de destino
print("#######################################################################")
origen = input("  Por favor, ingrese la ciudad de origen: ")
destino = input("  Por favor, ingrese la ciudad de destino: ")

#Calculo de la distancia y la duración del viaje
resultado = calcular_distancia_y_duracion(origen, destino, key)
if isinstance(resultado, tuple):
    distancia_km, duracion_horas_auto, duracion_horas_caminando = resultado
    print("-----------------------------------------------------------------------")
    print("  La distancia entre {} y {} es de {} kilómetros".format(origen, destino, distancia_km))
    print("  El calculo de la duración del viaje considera : \n  1)Si el vehiculo viaja a 60 km/h y \n  2)Si se camina a 5 km/h aproximadamente")
    print("  La duración del viaje en auto es de: {:.2f} horas".format(duracion_horas_auto))
    print("  La duración del viaje caminando es de: {:.2f} horas".format(duracion_horas_caminando))
    print("#######################################################################")
else:
    print(resultado)