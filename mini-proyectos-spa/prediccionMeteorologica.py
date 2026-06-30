import requests
from datetime import datetime

def informacion_meteorologica(ciudad):
    # 1. GEOLOCALIZACIÓN: Convertimos el nombre de la ciudad en coordenadas
    # S'han eliminat els claudàtors i enllaços duplicats del Markdown
    url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es"
    geo_res = requests.get(url_geo).json()

    if not geo_res.get('results'):
        return "No se ha encontrado la ciudad."

    lat = geo_res['results'][0]['latitude']
    lon = geo_res['results'][0]['longitude']
    nom = geo_res['results'][0]['name']

    # 2. CONSULTA DEL TIEMPO: Actual y previsión de 7 días
    url_tiempo = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto"
    res = requests.get(url_tiempo).json()

    # Datos actuales
    actual = res['current_weather']
    print(f"\n--- EL TIEMPO EN {nom.upper()} AHORA MISMO ---")
    print(f"Temperatura: {actual['temperature']}°C")
    print(f"Viento: {actual['windspeed']} km/h")

    # Datos semanales (Previsión)
    prevision = res['daily']
    print(f"\n--- PREVISIÓN PARA LOS PRÓXIMOS DÍAS ---")

    for i in range(len(prevision['time'])):
        # Formateamos la fecha para que sea legible
        data_obj = datetime.strptime(prevision['time'][i], "%Y-%m-%d")
        data_text = data_obj.strftime("%d/%m (%A)")

        t_max = prevision['temperature_2m_max'][i]
        t_min = prevision['temperature_2m_min'][i]
        lluvia = prevision['precipitation_probability_max'][i]

        # Añadimos un pequeño icono según la lluvia
        icono = "☔" if lluvia > 50 else "☀️"

        print(f"{data_text}: {t_min}°C a {t_max}°C | Lluvia: {lluvia}% {icono}")

# Ejecución
ciudad_usuario = input("Escribe el nombre de una ciudad: ")
informacion_meteorologica(ciudad_usuario)
