from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext

from typing import Any

from ..routers import user_router

from helpers.keyboards.language import markup_language

import random


@user_router.message(CommandStart())
async def welcome(message: Message, state: FSMContext, i18n: I18nContext) -> Any:
    welcome_emoji = '🤖 👋 💎 🖖 🤙 👀 👻 👾'.split(' ')

    await state.clear()
    await message.answer(random.choice(welcome_emoji))
    await message.answer(
        text=i18n.hello(user=message.from_user.mention_html()),
        reply_markup=markup_language(),
    )
