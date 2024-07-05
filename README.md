### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Этот проект представляет собой Telegram-бота WeatherBot, который предоставляет актуальную информацию о погоде. Бот позволяет пользователям устанавливать свой город и получать прогноз погоды, включая текущую температуру, дневной прогноз и атмосферные явления.

### Объяснение кода

1. **weather.py**:
    * **[`get_weather_data`](weather.py#L8)**: Выполняет запрос к Open-Meteo API для получения данных о погоде.
    * **[`get_current_weather`](weather.py#L16)**: Получает текущую погоду и форматирует данные для отображения.
    * **[`get_daily_forecast`](weather.py#L28)**: Получает дневной прогноз погоды и форматирует данные для отображения.
    * **[`get_atmospheric_conditions`](weather.py#L41)**: Получает данные об атмосферных явлениях и форматирует их.
    * **[`get_hourly_forecast`](weather.py#L55), [`get_solar_and_uv_index`](weather.py#L69)**: (На будущее) Получают почасовой прогноз и данные о солнечной радиации и УФ-индексе соответственно.
    * **[`get_weather_description`](weather.py#L83)**: Возвращает описание погодных условий на основе кода погоды.

2. **handlers.py**:
    * **[`WeatherStates`](handlers.py#L16)**: Определяет состояния для машины состояний (FSM).
    * **[`send_welcome`](handlers.py#L22)**: Отправляет приветственное сообщение при старте.
    * **[`send_help`](handlers.py#L30)**: Отправляет сообщение с инструкциями при вызове команды /help.
    * **[`set_city`](handlers.py#L38), [`receive_city`](handlers.py#L47)**: Обрабатывают команду /setcity и сохраняют введенный город.
    * **[`send_weather`](handlers.py#L56)**: Преобразует введенный город в координаты, получает прогноз погоды и отправляет его пользователю.

3. **main.py**:
    * **[`main`](main.py#L12)**: Инициализирует бота, подключает Redis для хранения состояний, устанавливает команды и запускает polling.

### Требования

- Python 3.8+
- aiogram 3.8.0
- requests
- redis-server

### Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/username/TG01_Weather_bot.git
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd TG01_Weather_bot
    ```
3. Создайте и активируйте виртуальное окружение:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```
5. Настройте переменные окружения в файле `config.py`:

    ```python
    API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
    OPENCAGE_API_KEY = 'YOUR_OPENCAGE_API_KEY'
    ```

---

## <a name="english"></a>Description in English

### Description

This project is a Telegram bot named WeatherBot that provides up-to-date weather information. The bot allows users to set their city and receive weather forecasts, including current temperature, daily forecast, and atmospheric conditions.

### Code Explanation

1. **weather.py**:
    * **[`get_weather_data`](weather.py#L8)**: Makes a request to the Open-Meteo API to get weather data.
    * **[`get_current_weather`](weather.py#L16)**: Gets current weather and formats the data for display.
    * **[`get_daily_forecast`](weather.py#L28)**: Gets daily weather forecast and formats the data for display.
    * **[`get_atmospheric_conditions`](weather.py#L41)**: Gets atmospheric conditions data and formats it.
    * **[`get_hourly_forecast`](weather.py#L55), [`get_solar_and_uv_index`](weather.py#L69)**: (Future) Get hourly forecast and solar radiation and UV index data respectively.
    * **[`get_weather_description`](weather.py#L83)**: Returns weather condition description based on the weather code.

2. **handlers.py**:
    * **[`WeatherStates`](handlers.py#L16)**: Defines states for the finite state machine (FSM).
    * **[`send_welcome`](handlers.py#L22)**: Sends a welcome message at the start.
    * **[`send_help`](handlers.py#L30)**: Sends an instruction message when the /help command is called.
    * **[`set_city`](handlers.py#L38), [`receive_city`](handlers.py#L47)**: Handle the /setcity command and save the entered city.
    * **[`send_weather`](handlers.py#L56)**: Converts the entered city to coordinates, gets the weather forecast, and sends it to the user.

3. **main.py**:
    * **[`main`](main.py#L12)**: Initializes the bot, connects Redis for state storage, sets commands, and starts polling.

### Requirements

- Python 3.8+
- aiogram 3.8.0
- requests
- redis-server

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/username/TG01_Weather_bot.git
    ```
2. Navigate to the project directory:
    ```sh
    cd TG01_Weather_bot
    ```
3. Create and activate a virtual environment:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Set up environment variables in the `config.py` file:

    ```python
    API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
    OPENCAGE_API_KEY = 'YOUR_OPENCAGE_API_KEY'
    ```
