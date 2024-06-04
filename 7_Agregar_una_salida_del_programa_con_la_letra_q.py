#7_Agregar_una_salida_del_programa_con_la_letra_q#

import requests

route_url = "http://www.mapquestapi.com/directions/v2/route"
key = "OIjeA0ZpFdA4P4SgNKpjL8TykFnk4fUh"  #API KEY

def calcular_distancia_y_duracion(origen, destino, key):
    params = {
        "key": key,
        "from": origen,
        "to": destino,
        "unit": "k"  #Distancia en km
    }
    replydata = requests.get(route_url, params=params)
    if replydata.status_code == 200:
        json_data = replydata.json()
        distancia_km = json_data["route"]["distance"]   # Cálculo de la distancia en km
        duracion_horas_auto = distancia_km / 60         # Si el vehículo viaja a 60 km/h aprox.
        duracion_horas_caminando = distancia_km / 5     # Si se camina a 5 km/h aprox.
        return distancia_km, duracion_horas_auto, duracion_horas_caminando
    else:
        return "Error al obtener la distancia"

def calcular_combustible(distancia):
    rendimiento = 9  # Se considera 9 km/litro aprox.
    combustible = distancia / rendimiento
    return combustible

def main():
    while True:
        print("-----------------------------------------------------------------------")
        print("               Bienvenido al calculador de viajes")
        print("                   [Ingrese 'q' para salir]")
        print("#######################################################################")

        ciudad_origen = input("ciudad de Origen: ").strip()
        if ciudad_origen.lower() == 'q':
            print("¡Hasta luego!")
            break
        ciudad_destino = input("ciudad de Destino: ").strip()
        
        if ciudad_destino.lower() == 'q':
            print("¡Hasta luego!")
            break
        else:
            resultado = calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, key)
            if isinstance(resultado, tuple):
                distancia_km, duracion_horas_auto, duracion_horas_caminando = resultado
                combustible_auto = calcular_combustible(distancia_km)

                # Imprimir resultados
                print("-----------------------------------------------------------------------")
                print(" La distancia entre {} y {} es {:.2f} kilómetros".format(ciudad_origen, ciudad_destino, distancia_km))
                print("-----------------------------------------------------------------------")
                print(" El cálculo de la duración del viaje considera:")
                print("  1) Si el vehículo viaja a 60 km/h aprox.")
                print("  2) Si se camina a 5 km/h aprox.")
                print(" La duración del viaje en auto es: {:.2f} horas".format(duracion_horas_auto))
                print(" La duración del viaje caminando es: {:.2f} horas".format(duracion_horas_caminando))
                print("-----------------------------------------------------------------------")
                print(" Si se considera un gasto de 9 km/litro:")
                print(" El combustible requerido para el viaje en auto es: {:.2f} litros".format(combustible_auto))
                print("-----------------------------------------------------------------------")
            else:
                print("No se pudo obtener la información del viaje. Verifique las ciudades ingresadas y su conexión a internet.\n")

if __name__ == "__main__":
    main()
