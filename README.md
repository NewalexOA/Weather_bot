### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Этот бот Telegram использует OpenWeatherMap API для получения прогноза погоды в трех форматах: минутный прогноз на 1 час, почасовой прогноз на 48 часов и дневной прогноз на 8 дней. Бот поддерживает установку города пользователем и сохранение его состояния с помощью Redis.

### Установка и требования

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/weather-forecast-bot.git
    cd weather-forecast-bot
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Убедитесь, что у вас установлен и запущен Redis:
    ```sh
    # Для macOS
    brew install redis
    brew services start redis

    # Для Ubuntu
    sudo apt update
    sudo apt install redis-server
    sudo systemctl enable redis-server.service
    sudo systemctl start redis-server.service

    # Для Windows скачайте и установите Redis с https://github.com/microsoftarchive/redis/releases
    ```

5. Создайте файл `config.py` и заполните его своими данными:
    ```python
    # config.py
    API_TOKEN = 'ВАШ_ТОКЕН'
    WEATHER_API_KEY = 'ВАШ_КЛЮЧ_ОТ_OPENWEATHERMAP'
    ```

6. Запустите бота:
    ```sh
    python main.py
    ```

### Объяснение кода

1. **weather.py**:
    * **get_weather_data**: Выполняет запрос к OpenWeatherMap API для получения данных о погоде.
    * **format_minutely_forecast, format_hourly_forecast, format_daily_forecast**: Форматируют данные для минутного, почасового и дневного прогнозов соответственно.
    * **get_weather_forecast**: Получает данные о погоде и возвращает форматированные строки для всех трех типов прогнозов.

2. **handlers.py**:
    * **WeatherStates**: Определяет состояния для машины состояний (FSM).
    * **send_welcome**: Отправляет приветственное сообщение при старте.
    * **send_help**: Отправляет сообщение с инструкциями при вызове команды /help.
    * **set_city, receive_city**: Обрабатывают команду /setcity и сохраняют введенный город.
    * **send_weather**: Преобразует введенный город в координаты, получает прогноз погоды и отправляет его пользователю.

3. **main.py**:
    * **main**: Инициализирует бота, подключает Redis для хранения состояний, устанавливает команды и запускает polling.

## <a name="english"></a>Description in English

### Description

This Telegram bot uses the OpenWeatherMap API to get weather forecasts in three formats: minutely forecast for 1 hour, hourly forecast for 48 hours, and daily forecast for 8 days. The bot supports setting the city by the user and saving its state using Redis.

### Installation and Requirements

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-forecast-bot.git
    cd weather-forecast-bot
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # For Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure you have Redis installed and running:
    ```sh
    # For macOS
    brew install redis
    brew services start redis

    # For Ubuntu
    sudo apt update
    sudo apt install redis-server
    sudo systemctl enable redis-server.service
    sudo systemctl start redis-server.service

    # For Windows, download and install Redis from https://github.com/microsoftarchive/redis/releases
    ```

5. Create a `config.py` file and fill it with your data:
    ```python
    # config.py
    API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
    WEATHER_API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
    ```

6. Run the bot:
    ```sh
    python main.py
    ```

### Code Explanation

1. **weather.py**:
    * **get_weather_data**: Makes a request to the OpenWeatherMap API to get weather data.
    * **format_minutely_forecast, format_hourly_forecast, format_daily_forecast**: Format data for minutely, hourly, and daily forecasts respectively.
    * **get_weather_forecast**: Fetches weather data and returns formatted strings for all three types of forecasts.

2. **handlers.py**:
    * **WeatherStates**: Defines states for the finite state machine (FSM).
    * **send_welcome**: Sends a welcome message on start.
    * **send_help**: Sends a help message when the /help command is called.
    * **set_city, receive_city**: Handle the /setcity command and save the entered city.
    * **send_weather**: Converts the entered city to coordinates, fetches the weather forecast, and sends it to the user.

3. **main.py**:
    * **main**: Initializes the bot, connects Redis for state storage, sets up commands, and starts polling.

---
