from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from aiogram_i18n import I18nContext, I18nMiddleware, LazyProxy
from aiogram_i18n.cores import FluentRuntimeCore

from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from data.config import config

from handlers import routers

from loguru import logger


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    logger.info('[📦] Launching the bot...')
    # Webhook setup
    await bot.set_webhook(f'{config.webhook.base_url}{config.webhook.bot_path}')

    # Include routers
    dispatcher.include_router(routers.user_router)
    dispatcher.include_router(routers.admin_router)
    logger.info('[3] Routers included.')

    # Setup i18n
    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(
            path='locales/{locale}/LC_MESSAGES',
        ),
        default_locale=config.general.locale,
    )
    logger.info('[2] I18N middleware included.')

    # Setup middlewares
    i18n_middleware.setup(dispatcher)
    logger.info('[1] Other middlewares included.')

    logger.info(f'[!] Bot stated -- @{(await bot.get_me()).username}')


async def on_shutdown(bot: Bot) -> None:
    logger.info('[X] Stopping bot...')
    logger.info('[🤖] Bye!')
    await bot.delete_webhook()


def main() -> None:
    properties = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
    bot = Bot(token=config.telegram.token, default=properties)

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
    request_handler.register(app, path=config.webhook.bot_path)

    setup_application(app, dispatcher, bot=bot)

    web.run_app(app, host=config.webhook.listen_address, port=config.webhook.listen_port)


if __name__ == '__main__':
    main()
