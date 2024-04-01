from aiogram import Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from aiogram_i18n import I18nContext

from typing import Any

from ..routers import user_router

from helpers.keyboards.language import markup_language, markup_avaiable_lanuages
from helpers.fabrics.language import LanguageCallback


@user_router.message(Command(commands=['language']))
async def language(message: Message, i18n: I18nContext) -> Any:
    await message.answer(
        text=i18n.get('current_language', language=i18n.locale.upper()),
        reply_markup=markup_language()
    )


@user_router.callback_query(LanguageCallback.filter(F.action == 'avaiable_language'))
async def avaiable_languages(callback_query: CallbackQuery, i18n: I18nContext, bot: Bot) -> Any:
    await callback_query.message.answer('Chooise your language', reply_markup=markup_avaiable_lanuages())
    await bot.answer_callback_query(callback_query.id)


@user_router.callback_query(LanguageCallback.filter(F.action == 'switch_language'))
async def switch_language(callback_query: CallbackQuery, callback_data: LanguageCallback, bot: Bot, i18n: I18nContext):
    selected_language = callback_data.locale

    await i18n.set_locale(selected_language)
    await callback_query.message.answer(i18n.language_changed())

    await bot.answer_callback_query(callback_query.id)
