from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from helpers.fabrics.language import LanguageCallback

from models.enum import AvaiableLanguages


def markup_language():
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text='Switch language? 🇬🇧', callback_data=LanguageCallback(action='avaiable_language').pack()))

    return builder.as_markup()


def markup_avaiable_lanuages():
    builder = InlineKeyboardBuilder()

    avaiable_languages = [e.value for e in AvaiableLanguages]
    for language in avaiable_languages:
        builder.add(
            InlineKeyboardButton(
                text=f'{language.locale} {language.flag}',
                callback_data=LanguageCallback(action='switch_language', locale=language.locale.lower()).pack()
            )
        )
    
    return builder.as_markup()
