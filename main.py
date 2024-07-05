import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram.types import BotCommand
import config
from handlers import router


async def main():
    # Создание экземпляра бота с токеном из config
    bot = Bot(token=config.API_TOKEN)

    # Создание экземпляра Redis
    redis = Redis(host='localhost', port=6379, db=5)

    # Использование RedisStorage для хранения данных FSM
    storage = RedisStorage(redis)

    # Создание экземпляра Dispatcher с указанным хранилищем
    dp = Dispatcher(storage=storage)

    # Регистрация роутера из handlers
    dp.include_router(router)

    # Установка команд бота
    await bot.set_my_commands([
        BotCommand(command="/start", description="Начало работы"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/setcity", description="Установить город"),
        BotCommand(command="/weather", description="Получить прогноз погоды")
    ])

    # Запуск polling
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
