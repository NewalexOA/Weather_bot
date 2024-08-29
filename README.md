### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Этот проект представляет собой Telegram-бота WeatherBot, который предоставляет актуальную информацию о погоде. Бот позволяет пользователям устанавливать свой город и получать прогноз погоды, включая текущую температуру, дневной прогноз и атмосферные явления.

### Объяснение кода

1. **weather.py**:
    * **[`get_weather_data`](weather.py#L4)**: Выполняет запрос к Open-Meteo API для получения данных о погоде.
    * **[`get_current_weather`](weather.py#L10)**: Получает текущую погоду и форматирует данные для отображения.
    * **[`get_daily_forecast`](weather.py#L24)**: Получает дневной прогноз погоды и форматирует данные для отображения.
    * **[`get_atmospheric_conditions`](weather.py#L40)**: Получает данные об атмосферных явлениях и форматирует их.
    * **[`get_hourly_forecast`](weather.py#L58), [`get_solar_and_uv_index`](weather.py#L76)**: (На будущее) Получают почасовой прогноз и данные о солнечной радиации и УФ-индексе соответственно.
    * **[`get_weather_description`](weather.py#L91)**: Возвращает описание погодных условий на основе кода погоды.

2. **handlers.py**:
    * **[`WeatherStates`](handlers.py#L14)**: Класс. Определяет состояния для машины состояний (FSM).
    * **[`send_welcome`](handlers.py#L19)**: Отправляет приветственное сообщение при старте.
    * **[`send_help`](handlers.py#L29)**: Отправляет сообщение с инструкциями при вызове команды /help.
    * **[`set_city`](handlers.py#L38), [`receive_city`](handlers.py#L45)**: Обрабатывают команду /setcity и сохраняют введенный город.
    * **[`send_weather`](handlers.py#L55)**: Преобразует введенный город в координаты, получает прогноз погоды и отправляет его пользователю.

3. **main.py**:
    * **[`main`](main.py#L9)**: Инициализирует бота, подключает Redis для хранения состояний, устанавливает команды и запускает polling.

### Требования

- Python 3.8+
- aiogram 3.8.0
- requests
- redis-server

### Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/NewalexOA/Weather_bot.git
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd Weather_bot
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
    Для получения `YOUR_OPENCAGE_API_KEY`:
   - Перейдите на [сайт OpenCage](https://opencagedata.com/).
   - Зарегистрируйтесь или войдите в свой аккаунт.
   - Перейдите в раздел API-ключей на панели управления и создайте новый API-ключ.
   - Скопируйте полученный ключ и вставьте его в файл `config.py`.


6. Установите и запустите Redis:
   - Установите Redis (например, через Homebrew на macOS):
     ```sh
     brew install redis
     ```
   - Запустите Redis:
     ```sh
     brew services start redis
     ```

   Для других операционных систем установка Redis может различаться, пожалуйста, следуйте инструкциям на официальном сайте Redis.

---

## <a name="english"></a>Description in English

### Description

This project is a Telegram bot named WeatherBot that provides up-to-date weather information. The bot allows users to set their city and receive weather forecasts, including current temperature, daily forecast, and atmospheric conditions.

### Code Explanation

1. **weather.py**:
    * **[`get_weather_data`](weather.py#L4)**: Makes a request to the Open-Meteo API to get weather data.
    * **[`get_current_weather`](weather.py#L10)**: Gets current weather and formats the data for display.
    * **[`get_daily_forecast`](weather.py#L24)**: Gets daily weather forecast and formats the data for display.
    * **[`get_atmospheric_conditions`](weather.py#L40)**: Gets atmospheric conditions data and formats it.
    * **[`get_hourly_forecast`](weather.py#L58), [`get_solar_and_uv_index`](weather.py#L76)**: (Future) Get hourly forecast and solar radiation and UV index data respectively.
    * **[`get_weather_description`](weather.py#L91)**: Returns weather condition description based on the weather code.

2. **handlers.py**:
    * **[`WeatherStates`](handlers.py#L14)**: Defines states for the finite state machine (FSM).
    * **[`send_welcome`](handlers.py#L19)**: Sends a welcome message at the start.
    * **[`send_help`](handlers.py#L29)**: Sends an instruction message when the /help command is called.
    * **[`set_city`](handlers.py#L38), [`receive_city`](handlers.py#L45)**: Handle the /setcity command and save the entered city.
    * **[`send_weather`](handlers.py#L55)**: Converts the entered city to coordinates, gets the weather forecast, and sends it to the user.

3. **main.py**:
    * **[`main`](main.py#L9)**: Initializes the bot, connects Redis for state storage, sets commands, and starts polling.

### Requirements

- Python 3.8+
- aiogram 3.8.0
- requests
- redis-server

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NewalexOA/Weather_bot.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Weather_bot
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
    To obtain `YOUR_OPENCAGE_API_KEY`:
   - Visit the [OpenCage website](https://opencagedata.com/).
   - Sign up or log in to your account.
   - Navigate to the API keys section in the dashboard and create a new API key.
   - Copy the obtained key and paste it into the `config.py` file.


6. Install and start Redis:
   - Install Redis (e.g., via Homebrew on macOS):
     ```sh
     brew install redis
     ```
   - Start Redis:
     ```sh
     brew services start redis
     ```

   For other operating systems, the installation process for Redis may vary. Please follow the instructions on the official Redis website.
