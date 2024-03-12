import streamlit as st
import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8e4daf7cddd52c13aa9b45429d0ed1a0&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


st.title("METEO")
city = st.text_input("Ville：")

if st.button("Recherche"):
    if city:
        weather_data = get_weather(city)
        if weather_data["cod"] == 200:
            st.write(f"Ville: {city}")
            st.write(f"Météo: {weather_data['weather'][0]['description']}")
            st.write(f"Température: {weather_data['main']['temp']} °C")
            st.write(f"Humidité: {weather_data['main']['humidity']} %")
            st.Write(f"Vent: {weather_data['main']['wind']} %")
        else:
            st.write("Les informations météorologiques pour cette ville n'ont pas été trouvées, veuillez les saisir à nouveau.")
