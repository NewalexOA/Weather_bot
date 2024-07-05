from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from weather import get_weather_forecast
import config
import requests

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
    # Установка состояния ожидания ввода города
    await state.set_state(WeatherStates.waiting_for_city)

# Обработчик для получения названия города от пользователя
@router.message(WeatherStates.waiting_for_city)
async def receive_city(message: Message, state: FSMContext):
    city = message.text
    # Сохранение города в данные состояния
    await state.update_data(city=city)
    await message.answer(f"Город установлен на {city}. Теперь вы можете использовать команду /weather для получения прогноза.")
    # Очистка состояния после получения города
    await state.clear()

# Обработчик команды /weather для получения прогноза погоды
@router.message(Command("weather"))
async def send_weather(message: Message, state: FSMContext):
    data = await state.get_data()
    city = data.get("city", "Москва")

    # Преобразование города в координаты (широта и долгота)
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={config.WEATHER_API_KEY}"
    geocode_response = requests.get(geocode_url).json()
    if geocode_response:
        lat = geocode_response[0]['lat']
        lon = geocode_response[0]['lon']
        weather_info = get_weather_forecast(lat, lon, config.WEATHER_API_KEY)
        await message.answer(weather_info)
    else:
        await message.answer("Не удалось найти координаты города. Пожалуйста, проверьте название города.")
