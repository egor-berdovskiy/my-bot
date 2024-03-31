from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from ..routers import user_router


@user_router.message(CommandStart())
async def welcome(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('👋')
    await message.answer(f'Hello, {message.from_user.full_name}!')
