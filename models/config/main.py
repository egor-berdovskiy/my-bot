from dataclasses import dataclass, field


@dataclass
class TelegramConfigObject:
    '''Class for storing settings related to Telegram.\n
    attributes:\n
    * token -- telegram bot token from botfather.
    '''
    token: str


@dataclass
class WebhookConfigObject:
    '''Class for storing settings related to webhooks.\n
    attributes:\n
    * listen_address -- localhost.
    * listen_port -- port on which the application will be launched.
    * base_url -- server address.
    * bot_path -- path to bot on server address.
    '''
    base_url: str
    bot_path: str
    listen_address: str = field(default='localhost')
    listen_port: int = field(default=5000)


@dataclass
class GeneralConfigObject:
    locale: str


@dataclass
class Config:
    '''Summary storage class for sections.\n
    attributes:\n
    * telegram
    * webhook
    * general
    '''
    telegram: TelegramConfigObject
    webhook: WebhookConfigObject
    general: GeneralConfigObject
