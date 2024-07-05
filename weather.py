import requests
from datetime import datetime


# Функция для получения данных о погоде с OpenWeatherMap API
def get_weather_data(lat: float, lon: float, api_key: str):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=alerts&units=metric&lang=ru&appid={api_key}"
    response = requests.get(url)
    return response.json()


# Функция для форматирования минутного прогноза на 1 час
def format_minutely_forecast(minutely_data):
    result = ["Минутный прогноз на 1 час:"]
    for entry in minutely_data:
        time = datetime.utcfromtimestamp(entry['dt']).strftime('%H:%M')
        precipitation = entry['precipitation']
        result.append(f"Время: {time}, Осадки: {precipitation} мм")
    return "\n".join(result)


# Функция для форматирования почасового прогноза на 48 часов
def format_hourly_forecast(hourly_data):
    result = ["Почасовой прогноз на 48 часов:"]
    for entry in hourly_data[:48]:
        time = datetime.utcfromtimestamp(entry['dt']).strftime('%d-%m %H:%M')
        temp = entry['temp']
        weather_desc = entry['weather'][0]['description']
        result.append(f"Время: {time}, Температура: {temp}°C, Погода: {weather_desc}")
    return "\n".join(result)


# Функция для форматирования дневного прогноза на 8 дней
def format_daily_forecast(daily_data):
    result = ["Дневной прогноз на 8 дней:"]
    for entry in daily_data:
        date = datetime.utcfromtimestamp(entry['dt']).strftime('%d-%m')
        temp_day = entry['temp']['day']
        temp_night = entry['temp']['night']
        weather_desc = entry['weather'][0]['description']
        result.append(
            f"Дата: {date}, Дневная темп.: {temp_day}°C, Ночная темп.: {temp_night}°C, Погода: {weather_desc}")
    return "\n".join(result)


# Функция для получения полного прогноза погоды и его форматирования
def get_weather_forecast(lat: float, lon: float, api_key: str):
    data = get_weather_data(lat, lon, api_key)

    minutely_forecast = format_minutely_forecast(data['minutely'])
    hourly_forecast = format_hourly_forecast(data['hourly'])
    daily_forecast = format_daily_forecast(data['daily'])

    return f"{minutely_forecast}\n\n{hourly_forecast}\n\n{daily_forecast}"
