from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from weather import get_current_weather, get_daily_forecast, get_atmospheric_conditions  # Импорт функций из weather.py
import requests
import config

# Создание роутера для обработки команд
router = Router()

# Определение состояний для FSM (машины состояний)
class WeatherStates(StatesGroup):
    waiting_for_city = State()

# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Я WeatherBot, ваш персональный помощник по прогнозу погоды. "
        "Используйте команду /weather, чтобы получить актуальную информацию о погоде. "
        "Если у вас есть вопросы, воспользуйтесь командой /help. "
        "Чтобы установить ваш город, используйте команду /setcity."
    )

# Обработчик команды /help
@router.message(Command("help"))
async def send_help(message: Message):
    await message.answer(
        "Я здесь, чтобы помочь вам узнать текущую погоду. "
        "Используйте команду /weather, чтобы получить прогноз погоды. "
        "Если вам нужна помощь, просто напишите /help."
    )

# Обработчик команды /setcity для установки города
@router.message(Command("setcity"))
async def set_city(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, введите название вашего города:")
    await state.set_state(WeatherStates.waiting_for_city)

# Обработчик для получения названия города от пользователя
@router.message(WeatherStates.waiting_for_city)
async def receive_city(message: Message, state: FSMContext):
    city = message.text

    # Сохранение города в данные состояния
    await state.update_data(city=city)

    # Очищаем состояние, но сохраняем данные
    await state.set_state(None)

    await message.answer(
        f"Город установлен на {city}. Теперь вы можете использовать команду /weather для получения прогноза."
    )

# Обработчик команды /weather для получения прогноза погоды
@router.message(Command("weather"))
async def send_weather(message: Message, state: FSMContext):
    data = await state.get_data()

    city = data.get("city", None)

    if not city:
        await message.answer("Сначала установите город с помощью команды /setcity.")
        return

    # Преобразование города в координаты (широта и долгота) с использованием OpenCage Geocoder
    geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={config.OPENCAGE_API_KEY}"

    try:
        response = requests.get(geocode_url)
        response.raise_for_status()  # Проверка на успешный статус ответа
        geocode_response = response.json()

        if geocode_response['results']:
            lat = geocode_response['results'][0]['geometry']['lat']
            lon = geocode_response['results'][0]['geometry']['lng']

            current_weather = get_current_weather(lat, lon)
            daily_forecast = get_daily_forecast(lat, lon)
            atmospheric_conditions = get_atmospheric_conditions(lat, lon)

            # Формирование сообщения с заголовком
            weather_message = (
                f"Прогноз погоды в городе {city}:\n\n"
                f"{current_weather}\n\n"
                f"{daily_forecast}\n"
                f"{atmospheric_conditions}"
            )

            await message.answer(weather_message)
        else:
            await message.answer("Не удалось найти координаты города. Пожалуйста, проверьте название города.")
    except requests.exceptions.RequestException as e:
        await message.answer("Произошла ошибка при получении данных. Попробуйте позже.")
    except ValueError:
        await message.answer("Произошла ошибка при обработке данных. Попробуйте позже.")
