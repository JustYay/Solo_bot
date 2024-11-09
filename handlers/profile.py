import os

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loguru import logger

from bot import bot
from config import (CHANNEL_URL, FREEKASSA_ENABLE, PAYMENT_METHOD,
                    YOOKASSA_ENABLE)
from database import get_balance, get_key_count, get_referral_stats
from handlers.texts import (get_referral_link, invite_message_send,
                            profile_message_send)

router = Router()


async def process_callback_view_profile(
    callback_query: types.CallbackQuery, state: FSMContext
):
    chat_id = callback_query.from_user.id
    username = callback_query.from_user.full_name

    image_path = os.path.join(os.path.dirname(__file__), "pic.jpg")

    try:
        key_count = await get_key_count(chat_id)
        balance = await get_balance(chat_id)
        if balance is None:
            balance = 0

        profile_message = profile_message_send(username, chat_id, balance, key_count)

        if key_count == 0:
            profile_message += (
                "\n<i>Нажмите ➕Устройство снизу, чтобы добавить устройство в VPN</i>"
            )

        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text="📢 Наш канал", url=CHANNEL_URL))
        builder.row(
            InlineKeyboardButton(text="➕ Устройство", callback_data="create_key"),
            InlineKeyboardButton(text="📱 Мои устр-ва", callback_data="view_keys"),
        )
        if YOOKASSA_ENABLE or FREEKASSA_ENABLE:
            builder.row(
                InlineKeyboardButton(
                    text="💳 Пополнить баланс",
                    callback_data=(
                        "pay_freekassa"
                        if PAYMENT_METHOD == "freekassa"
                        else "replenish_balance"
                    ),
                )
            )
        builder.row(
            InlineKeyboardButton(text="👥 Пригласить", callback_data="invite"),
            InlineKeyboardButton(text="📘 Инструкции", callback_data="instructions"),
        )
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu"))

        # Попробуем удалить предыдущее сообщение
        try:
            await callback_query.message.delete()
        except Exception as e:
            logger.error(
                f"Ошибка при удалении сообщения: {e}"
            )  # Логируем ошибку, если удаление не удалось

        if os.path.isfile(image_path):
            with open(image_path, "rb") as image_file:
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=BufferedInputFile(image_file.read(), filename="pic.jpg"),
                    caption=profile_message,
                    parse_mode="HTML",
                    reply_markup=builder.as_markup(),
                )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=profile_message,
                parse_mode="HTML",
                reply_markup=builder.as_markup(),
            )

    except Exception as e:
        await bot.send_message(chat_id, f"❗️ Ошибка при получении данных профиля: {e}")

    await callback_query.answer()


@router.callback_query(F.data == "invite")
async def invite_handler(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    referral_link = get_referral_link(chat_id)

    referral_stats = await get_referral_stats(chat_id)

    invite_message = invite_message_send(referral_link, referral_stats)

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="view_profile"))

    await callback_query.message.delete()

    await bot.send_message(
        chat_id=chat_id,
        text=invite_message,
        parse_mode="HTML",
        reply_markup=builder.as_markup(),
    )

    await callback_query.answer()


@router.callback_query(F.data == "view_profile")
async def view_profile_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await process_callback_view_profile(callback_query, state)
