from aiogram.filters.callback_data import CallbackData
from typing import Optional


class LanguageCallback(CallbackData, prefix='language'):
    action: str
    locale: Optional[str] = None
