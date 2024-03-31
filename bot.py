from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from data.config import telegram, webhook

from handlers import routers

from loguru import logger


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    # WebHook setup
    await bot.set_webhook(f'{webhook.base_url}{webhook.bot_path}')

    # Include routers
    dispatcher.include_router(routers.user_router)
    dispatcher.include_router(routers.admin_router)


async def on_shutdown(bot: Bot) -> None:
    logger.info('[i] Stopping bot...')
    logger.info('[i] Bye!')
    await bot.delete_webhook()


def main() -> None:
    properties = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
    bot = Bot(token=telegram.token, default=properties)

    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    # Lifetime handlers
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    app = web.Application()
    request_handler = SimpleRequestHandler(
        dispatcher,
        bot
    )
    request_handler.register(app, path=webhook.bot_path)

    setup_application(app, dispatcher, bot=bot)

    web.run_app(app, host=webhook.listen_address, port=webhook.listen_port)


if __name__ == '__main__':
    main()
