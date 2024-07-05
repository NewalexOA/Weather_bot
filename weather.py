import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Функция для получения данных о погоде с Open-Meteo API
def get_weather_data(lat: float, lon: float, params: str):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&{params}"
    logging.info(f"Запрос данных погоды по URL: {url}")
    response = requests.get(url)
    logging.info(f"Ответ от API: {response.text}")
    return response.json()

# Функция для получения текущей погоды
def get_current_weather(lat: float, lon: float):
    params = "current_weather=true"
    data = get_weather_data(lat, lon, params)
    current_weather = data.get('current_weather', {})
    if current_weather:
        temp = current_weather.get('temperature')
        windspeed = current_weather.get('windspeed')
        weathercode = current_weather.get('weathercode')
        weather_desc = get_weather_description(weathercode)
        return f"Текущая температура: {temp}°C\nСкорость ветра: {windspeed} м/с\nПогодные условия: {weather_desc}"
    else:
        return "Не удалось получить данные о текущей погоде."

# Функция для получения дневного прогноза
def get_daily_forecast(lat: float, lon: float):
    params = "daily=temperature_2m_max,temperature_2m_min&timezone=Europe/Moscow"
    data = get_weather_data(lat, lon, params)
    daily = data.get('daily', {})
    if daily:
        max_temps = daily.get('temperature_2m_max', [])
        min_temps = daily.get('temperature_2m_min', [])
        times = daily.get('time', [])
        forecast = "Прогноз на неделю:\n"
        for date, max_temp, min_temp in zip(times, max_temps, min_temps):
            forecast += f"{date}: Макс. {max_temp}°C, Мин. {min_temp}°C\n"
        return forecast
    else:
        return "Не удалось получить дневной прогноз."

# Функция для получения данных об атмосферных явлениях
def get_atmospheric_conditions(lat: float, lon: float):
    params = "daily=precipitation_sum,weathercode&timezone=Europe/Moscow"
    data = get_weather_data(lat, lon, params)
    daily = data.get('daily', {})
    if daily:
        precipitations = daily.get('precipitation_sum', [])
        weathercodes = daily.get('weathercode', [])
        times = daily.get('time', [])
        conditions = "Атмосферные явления:\n"
        for date, precipitation, weathercode in zip(times, precipitations, weathercodes):
            weather_desc = get_weather_description(weathercode)
            precip_desc = f"{precipitation} мм" if precipitation > 0 else "нет"
            conditions += f"{date}: Осадки: {precip_desc}, {weather_desc}\n"
        return conditions
    else:
        return "Не удалось получить данные об атмосферных явлениях."

# Функция для получения почасового прогноза (на будущее)
def get_hourly_forecast(lat: float, lon: float):
    params = "hourly=temperature_2m,relative_humidity_2m,pressure_msl,wind_speed_10m,precipitation_sum&timezone=Europe/Moscow"
    data = get_weather_data(lat, lon, params)
    hourly = data.get('hourly', {})
    if hourly:
        temps = hourly.get('temperature_2m', [])
        humidities = hourly.get('relative_humidity_2m', [])
        pressures = hourly.get('pressure_msl', [])
        windspeeds = hourly.get('wind_speed_10m', [])
        precipitations = hourly.get('precipitation_sum', [])
        forecast = "Почасовой прогноз:\n"
        for temp, humidity, pressure, windspeed, precipitation in zip(temps, humidities, pressures, windspeeds, precipitations):
            forecast += f"Температура: {temp}°C, Влажность: {humidity}%, Давление: {pressure} гПа, Скорость ветра: {windspeed} м/с, Осадки: {precipitation} мм\n"
        return forecast
    else:
        return "Не удалось получить почасовой прогноз."

# Функция для получения данных о солнечной радиации и УФ-индексе (на будущее)
def get_solar_and_uv_index(lat: float, lon: float):
    params = "daily=uv_index_max,solar_radiation&timezone=Europe/Moscow"
    data = get_weather_data(lat, lon, params)
    daily = data.get('daily', {})
    if daily:
        uv_indexes = daily.get('uv_index_max', [])
        solar_radiations = daily.get('solar_radiation', [])
        solar_uv = "Солнечная радиация и УФ-индекс:\n"
        for uv_index, solar_radiation in zip(uv_indexes, solar_radiations):
            solar_uv += f"УФ-индекс: {uv_index}, Солнечная радиация: {solar_radiation} Вт/м²\n"
        return solar_uv
    else:
        return "Не удалось получить данные о солнечной радиации и УФ-индексе."

# Функция для получения описания погодных условий по коду
def get_weather_description(weathercode):
    weather_descriptions = {
        0: "Ясно",
        1: "Главным образом ясно",
        2: "Переменная облачность",
        3: "Пасмурно",
        45: "Туман",
        48: "Иней",
        51: "Легкий дождь",
        53: "Умеренный дождь",
        55: "Сильный дождь",
        56: "Ледяной дождь",
        57: "Сильный ледяной дождь",
        61: "Легкий снег",
        63: "Умеренный снег",
        65: "Сильный снег",
        66: "Легкий ледяной дождь",
        67: "Сильный ледяной дождь",
        71: "Легкий снег",
        73: "Умеренный снег",
        75: "Сильный снег",
        80: "Легкий дождь с грозой",
        81: "Умеренный дождь с грозой",
        82: "Сильный дождь с грозой",
        95: "Гроза",
        96: "Гроза с градом",
        99: "Сильная гроза с градом"
    }
    return weather_descriptions.get(weathercode, "Неизвестные погодные условия")
