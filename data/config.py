from .config_objects import TelegramConfigObject, WebhookConfigObject
from enum import StrEnum
from configparser import ConfigParser


parser = ConfigParser()
parser.read(r'config.ini')


class Sections(StrEnum):
    telegram = 'Telegram'
    webhook = 'WebHook'


telegram = TelegramConfigObject(
    token=parser.get(Sections.telegram, 'token')
)

webhook = WebhookConfigObject(
    listen_address=parser.get(Sections.webhook, 'listen_address'),
    listen_port=parser.getint(Sections.webhook, 'listen_port'),
    base_url=parser.get(Sections.webhook, 'base_url'),
    bot_path=parser.get(Sections.webhook, 'bot_path'),
)